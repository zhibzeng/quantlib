import numpy as np
import pandas as pd
from ...common.settings import CONFIG
from ...common.logging import Logger
from ...utils.calendar import TDay


class Fund:
    def __init__(self, strategy):
        self.strategy = strategy
        self.market = strategy.market
        # self.strategy.event_manager.register(EventType.BACKTEST_NEWDAY, self.on_newday, 5)
        self.universe = self.market.market_data.columns[:-1]
        self.trading_calendar = self.market.trading_days
        self.today_idx = 0
        self.sheet = pd.DataFrame(np.zeros([len(self.trading_calendar), 2]),
                                  index=self.trading_calendar,
                                  columns=["net_value", "fee"])
        self.position = pd.DataFrame(np.zeros(self.market.market_data.shape),
                                     index=self.trading_calendar,
                                     columns=list(self.universe)+["CASH"])
        self.delayed = {}
        self.__tobuy = {}
        self.initialize()

    def initialize(self):
        self.today_idx = -1
        self.sheet = pd.DataFrame(np.zeros([len(self.trading_calendar), 2]),
                                  index=self.trading_calendar,
                                  columns=["net_value", "fee"])
        self.position = pd.DataFrame(np.zeros(self.market.market_data.shape),
                                     index=self.trading_calendar,
                                     columns=list(self.universe)+["CASH"])
        self.position["CASH"].iloc[0] = 1.0
        self.sheet["net_value"].iloc[0] = 1.0

    def on_newday(self, today):
        self.today_idx += 1
        assert self.trading_calendar[self.today_idx] == today
        self.settle()
        self.do_transactions()
        self.handle_delayed_stocks()

    def settle(self):
        """
        Only settle the net value and the
        positions based on market price change.
        This doesn't trade stocks.
        """
        assert self.strategy.today == self.market.today
        today = self.strategy.today
        if self.today_idx != 0:
            self.position.iloc[self.today_idx] = \
                np.nan_to_num(self.position.iloc[self.today_idx-1] \
                              * (1 + self.market.today_market.fillna(0)))
            self.position.loc[today, "CASH"] = self.position["CASH"].iloc[self.today_idx-1]
            self.sheet.loc[today, "net_value"] = self.position.iloc[self.today_idx].sum()
            self.sheet.loc[today, "fee"] = 0


    def do_transactions(self):
        """
        Trade the stocks
        """
        if not self.__tobuy:
            return
        today = self.strategy.today
        old_position = self.position.iloc[self.today_idx, :-1]
        new_position = self.handle_position(old_position)
        fee = abs(new_position - old_position).sum() * CONFIG.FEE_RATE
        self.position.iloc[self.today_idx, :-1] = new_position
        self.__tobuy = None
        self.sheet.loc[today, "net_value"] -= fee
        self.sheet.loc[today, "fee"] = fee
        self.position.loc[today, "CASH"] = \
            self.net_value - self.position.iloc[self.today_idx, :-1].sum()


    def handle_position(self, old_position):
        """
        Calculate the new position based on the
        target, old position and market status (
        halt, up/down-limit, etc.)
        """
        today = self.strategy.today.strftime("%Y%m%d")
        new_position = old_position.copy()
        tobuy = pd.Series(np.zeros_like(old_position), index=old_position.index)
        tobuy.update(pd.Series(self.__tobuy))
        uplimit, downlimit = self.get_limits()
        halt = list(self.market.today_market[self.market.today_market.isnull()].index)
        uplimit += halt
        downlimit += halt
        wanted_position = tobuy * self.net_value
        overflow_position = 0
        effected_by_limit = []
        for stock in uplimit:
            if wanted_position[stock] > old_position[stock]:
                overflow_position += wanted_position[stock] - old_position[stock]
                effected_by_limit.append(stock)
                if stock in halt:
                    Logger.debug("Trying to buy halt stock: {date} - {stock}".format(date=today, stock=stock))
                else:
                    Logger.debug("Trying to buy up-limit stock: {date} - {stock}".format(date=today, stock=stock))
        for stock in downlimit:
            if wanted_position[stock] < old_position[stock]:
                overflow_position += wanted_position[stock] - old_position[stock]
                effected_by_limit.append(stock)
                self.delayed[stock] = wanted_position[stock]
                if stock in halt:
                    Logger.debug("Trying to sell halt stock: {date} - {stock}".format(date=today, stock=stock))
                else:
                    Logger.debug("Trying to sell down-limit stock: {date} - {stock}".format(date=today, stock=stock))
        others = [stock for stock in old_position.index if stock not in effected_by_limit + ["CASH"]]
        # tobuy[others] += tobuy[others] * overflow_position / tobuy[others].sum()
        tobuy[others] *= 1 + overflow_position / self.net_value
        new_position.update(tobuy[others] * self.net_value)
        return new_position

    def handle_delayed_stocks(self):
        """
        When trying to sell a stock at halt or down-limit, it's
        put in a delayed list. Then the trading system will try
        to sell it when possible.
        """
        today = self.strategy.today
        _, downlimit = self.get_limits()
        halt = list(self.market.today_market[self.market.today_market.isnull()].index)
        limited = downlimit + halt
        for stock, wanted_position in self.delayed.copy().items():
            real_position = self.position.loc[today, stock]
            if  real_position < wanted_position:
                Logger.warn("%s with position %0.3f is less than target %0.3f, "
                            "which is not supposed to happen." % (stock, real_position, wanted_position))
            if stock not in limited:
                fee = abs(real_position - wanted_position) * CONFIG.FEE_RATE
                self.sheet.loc[today, "net_value"] -= fee
                self.position.loc[today, "CASH"] += real_position - wanted_position - fee
                self.position.loc[today, stock] = wanted_position
                self.sheet.loc[today, "fee"] += fee
                del self.delayed[stock]
                Logger.debug("Sold delayed stock %s @ %s" % (stock, today.strftime("%Y-%m-%d")))

    def get_limits(self):
        """
        Returns
        -------
        two lists of stocks that reaches up-limit and down-limit at next-day open
        """
        today = self.strategy.today
        today_open = self.market.open_prices.loc[today]
        try:
            yesterday_close = self.market.close_prices.loc[today - TDay]
        except (KeyError, IndexError):
            return [], []
        pct_change = today_open / yesterday_close - 1
        uplimit = list(pct_change[pct_change > 0.09].index)
        downlimit = list(pct_change[pct_change < -0.09].index)
        return uplimit, downlimit

    def change_position(self, tobuy_pct):
        self.__tobuy = tobuy_pct

    @property
    def net_value(self):
        return self.sheet.loc[self.strategy.today, "net_value"]

    @property
    def tobuy(self):
        return self.__tobuy.copy()

