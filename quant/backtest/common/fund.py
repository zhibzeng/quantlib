import numpy as np
import pandas as pd
from .events import EventType


class Fund:
    def __init__(self, strategy):
        self.strategy = strategy
        self.market = strategy.market
        self.strategy.event_manager.register(EventType.BACKTEST_NEWDAY, self.on_newday, 5)
        self.universe = self.market.market_data.columns[:-1]
        self.trading_calendar = self.market.trading_days
        self.today_idx = 0
        self.__sheet = pd.DataFrame(np.zeros([len(self.trading_calendar), 2]),
                                    index=self.trading_calendar,
                                    columns=["net_value", "fee"])
        self.__position = pd.DataFrame(np.zeros(self.market.market_data.shape),
                                       index=self.trading_calendar,
                                       columns=list(self.universe)+["CASH"])
        self.__tobuy = {}
        self.initialize()

    def initialize(self):
        self.today_idx = -1
        self.__sheet = pd.DataFrame(np.zeros([len(self.trading_calendar), 2]),
                                    index=self.trading_calendar,
                                    columns=["net_value", "fee"])
        self.__position = pd.DataFrame(np.zeros(self.market.market_data.shape),
                                       index=self.trading_calendar,
                                       columns=list(self.universe)+["CASH"])
        self.__position["CASH"].iloc[0] = 1.0

    def on_newday(self, today):
        self.today_idx += 1
        assert self.trading_calendar[self.today_idx] == today
        self.settle()
        self.do_transactions()

    def settle(self):
        assert self.strategy.today == self.market.today
        net_value = self.__position["CASH"].iloc[self.today_idx-1]
        self.__position.iloc[self.today_idx] = \
            np.nan_to_num(self.__position.iloc[self.today_idx-1] * self.market.today_market)
        net_value += self.__position.iloc[self.today_idx].sum()
        self.__sheet.loc[self.strategy.today, "net_value"] = net_value
        self.__sheet.loc[self.strategy.today, "fee"] = 0

    def do_transactions(self):
        # TODO: trade with average prices
        if not self.__tobuy:
            return
        fee = 0
        for stock in self.universe:
            old_position = self.__position[stock].iloc[self.today_idx-1]
            new_position = self.__tobuy.get(stock, 0) * self.net_value
            fee += abs(new_position - old_position) * self.strategy.fee_rate
            if new_position != 0:
                self.__position[self.strategy.today, stock] = new_position
        self.__tobuy = None
        self.__sheet.loc[self.strategy.today, "net_value"] -= fee
        self.__sheet.loc[self.strategy.today, "fee"] += fee
        self.__position.loc[self.strategy.today, "CASH"] = \
            self.net_value - self.__position.iloc[:-1, self.today_idx].sum()

    def change_position(self, tobuy_pct):
        self.__tobuy = tobuy_pct

    @property
    def net_value(self):
        return self.__sheet.loc[self.strategy.today, "net_value"]

