import numpy as np
import pandas as pd
from .events import EventType


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
        if self.today_idx != 0:
            self.position.iloc[self.today_idx] = \
                np.nan_to_num(self.position.iloc[self.today_idx-1] \
                              * (1 + self.market.today_market.fillna(0)))
            self.position["CASH"].iloc[self.today_idx] = self.position["CASH"].iloc[self.today_idx-1]
            assert self.position["CASH"].iloc[self.today_idx-1] > 0, "CASH"
            self.sheet.loc[self.strategy.today, "net_value"] = self.position.iloc[self.today_idx].sum()
            assert self.net_value > 0.8, (self.position["CASH"].iloc[self.today_idx], self.position.iloc[self.today_idx].sum())
            self.sheet.loc[self.strategy.today, "fee"] = 0

    def do_transactions(self):
        # TODO: trade with average prices
        if not self.__tobuy:
            return
        old_position = self.position.iloc[self.today_idx - 1, :-1]
        self.position.iloc[self.today_idx].update(pd.Series(self.__tobuy))
        self.position.iloc[self.today_idx, :-1] *= self.net_value
        new_position = self.position.iloc[self.today_idx, :-1]
        fee = abs(new_position - old_position).sum() * self.strategy.fee_rate
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

