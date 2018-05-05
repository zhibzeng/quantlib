"""处理Universe的Mod"""
from datetime import timedelta
import numpy as np
import pandas as pd
from ..common.mods import AbstractMod
from ..common.events import EventType
from ...data import wind
from ...common.logging import Logger
from ...utils.calendar import TDay


@AbstractMod.register
class NoSTUniverse(AbstractMod):
    """NoSTUniverse模块
    会自动将universe中ST的股票去除。
    将持有的已经进入ST的股票主动卖出。
    """
    def __init__(self):
        self.st = wind.arange_entry_table("AShareST").fillna(False)
        self.st_stocks = set()
        super(NoSTUniverse, self).__init__()

    def on_get_universe(self, universe):
        """
        把待选股票池中ST的股票去除
        """
        today = self.strategy.today
        self.st_stocks = set(self.st.columns[self.st.loc[today]])
        universe.difference_update(self.st_stocks)
    
    def on_backtest_after_handle(self):
        """
        把买入目标（由于未知原因产生的）或已购持仓中的ST股票卖出
        """
        fund = self.strategy.fund
        if self.st_stocks is None:
            return
        tobuy = fund.tobuy
        if tobuy is not None:
            for stock in self.st_stocks:
                if stock in tobuy:
                    tobuy[stock] = 0
            self.strategy.change_position(tobuy)
        else:
            position = fund.position.iloc[fund.today_idx, :-1].to_dict()
            to_sell = [stock for stock in self.st_stocks if position[stock] > 0]
            if to_sell:
                today = self.strategy.today.strftime("%Y-%m-%d")
                for stock in to_sell:
                    Logger.debug("Sell {} @ {} because it's listed as ST".format(stock, today))
                fund.exceptional_sell(to_sell)


@AbstractMod.register
class NoIPOUniverse(AbstractMod):
    """
    把新上市60天内的股票去除
    """
    def __init__(self, days=60):
        self.ipo = wind.get_wind_table("AShareIPO", ["s_ipo_listdate", "s_info_windcode"]).dropna()
        self.ipo["s_ipo_listdate"] += timedelta(days=days)
        super(NoIPOUniverse, self).__init__()

    def on_get_universe(self, universe: set):
        today = self.strategy.today
        invalid_stock = list(self.ipo[self.ipo.s_ipo_listdate > today].s_info_windcode)
        universe.difference_update(invalid_stock)


@AbstractMod.register
class NoSmallUniverse(AbstractMod):
    """
    去除市值50亿以下的股票
    """
    def __init__(self):
        self.size = wind.get_wind_data("AShareEODDerivativeIndicator", "s_val_mv")

    def on_get_universe(self, universe: set):
        today = self.strategy.today
        size = self.size.loc[today]
        stocks = set(size.index[size > 500000])
        universe.intersection_update(stocks)


@AbstractMod.register
class NoUpLimitUniverse(AbstractMod):
    """从可交易股票池中去除涨停股票"""
    def __init__(self):
        self.open_prices = None
        self.preclose_prices = None
        super(NoUpLimitUniverse, self).__init__()

    def __plug_in__(self, caller):
        super(NoUpLimitUniverse, self).__plug_in__(caller)
        self.open_prices = caller.market.open_prices
        self.preclose_prices = caller.market.preclose_prices

    def on_get_universe(self, universe: set):
        today = self.strategy.today
        next_trading_day = today + TDay
        if next_trading_day not in self.strategy.market.market_data.index:
            return
        next_open = self.open_prices.loc[next_trading_day]
        this_close = self.preclose_prices.loc[next_trading_day]
        change = next_open / this_close - 1
        no_up_limit = set(change[change <= 0.09].index)
        universe.intersection_update(no_up_limit)


@AbstractMod.register
class ActivelyTraded(AbstractMod):
    """ActivelyTraded模块
    会自动将universe中交易额小于阈值的股票去除。
    """
    def __init__(self, threshold=10000):
        self.strategy = None
        self.threshold = threshold
        self.amount = wind.get_wind_data("AShareEODPrices", "s_dq_amount")
        super(ActivelyTraded, self).__init__()

    def on_get_universe(self, universe: set):
        today = self.strategy.today
        today_amount = self.amount.loc[today]
        valid = set(today_amount.index[today_amount >= self.threshold])
        universe.intersection_update(valid)

