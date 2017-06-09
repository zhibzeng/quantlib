import numpy as np
import pandas as pd
from .events import EventType
from ...common.settings import CONFIG


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

    def settle(self):
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
        # TODO: trade with average prices
        if not self.__tobuy:
            return
        old_position = self.position.iloc[self.today_idx, :-1].copy()
        new_position = pd.Series(np.zeros(len(self.universe)), index=self.universe)
        tobuy = pd.Series(self.__tobuy) * self.net_value
        new_position.update(tobuy)
        for stock, pct in old_position[self.market.today_market > 0.09].iteritems():
            new_position[stock] = min(pct, new_position[stock])   # cannot buy stocks reach up-limit
        for stock, pct in old_position[self.market.today_market < -0.09].iteritems():
            new_position[stock] = max(pct, new_position[stock])   # cannot buy stocks reach up-limit
        self.position.iloc[self.today_idx, :-1] = new_position
        fee = abs(new_position - old_position).sum() * CONFIG.FEE_RATE
        self.__tobuy = None
        self.sheet.loc[self.strategy.today, "net_value"] -= fee
        self.sheet.loc[self.strategy.today, "fee"] = fee
        self.position.loc[self.strategy.today, "CASH"] = \
            self.net_value - self.position.iloc[self.today_idx, :-1].sum()

    def change_position(self, tobuy_pct):
        self.__tobuy = tobuy_pct

    @property
    def net_value(self):
        return self.sheet.loc[self.strategy.today, "net_value"]

