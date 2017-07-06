"""处理Universe的Mod"""
from datetime import timedelta
import numpy as np
import pandas as pd
from ..common.mods import AbstractMod
from ..common.events import EventType
from ...data import wind
from ...utils.calendar import TDay


@AbstractMod.register
class NoSTUniverse(AbstractMod):
    """NoSTUniverse模块
    会自动将universe中ST的股票去除。
    """
    def __init__(self):
        self.strategy = None
        self.st = self.get_st_list()

    @staticmethod
    def get_st_list():
        st = wind.get_wind_table("AShareST")
        st["entry_dt"] = pd.to_datetime(st["entry_dt"])
        st["remove_dt"] = pd.to_datetime(st["remove_dt"])
        return st

    def __plug_in__(self, caller):
        self.strategy = caller
        self.strategy.event_manager.register(EventType.GET_UNIVERSE, self.handle_universe)

    def handle_universe(self, universe):
        today = self.strategy.today
        st = self.st.query("(entry_dt<'%(dt)s')&(remove_dt>'%(dt)s')" % {"dt": str(today)})
        st_stocks = list(st.s_info_windcode)
        for stock in st_stocks:
            if stock in universe:
                universe.remove(stock)


@AbstractMod.register
class NoIPOUniverse(AbstractMod):
    def __init__(self, days=30):
        self.strategy = None
        self.ipo = wind.get_wind_table("AShareIPO")
        self.ipo["s_ipo_listdate"] += timedelta(days=days)

    def __plug_in__(self, caller):
        self.strategy = caller
        self.strategy.event_manager.register(EventType.GET_UNIVERSE, self.handle_universe)

    def handle_universe(self, universe):
        today = self.strategy.today
        invalid_stock = list(self.ipo[self.ipo.s_ipo_listdate > today].s_info_windcode)
        for stock in invalid_stock:
            if stock in universe:
                universe.remove(stock)


@AbstractMod.register
class NoUpLimitUniverse(AbstractMod):
    """从可交易股票池中去除涨停股票"""
    def __init__(self):
        self.strategy = None
        self.open_prices = None
        self.close_prices = None

    def __plug_in__(self, caller):
        self.strategy = caller
        self.strategy.event_manager.register(EventType.GET_UNIVERSE, self.handle_universe)
        self.open_prices = caller.market.open_prices
        self.close_prices = caller.market.close_prices

    def handle_universe(self, universe):
        today = self.strategy.today
        next_trading_day = today + TDay
        if next_trading_day not in self.strategy.market.market_data.index:
            return
        next_open = self.open_prices.loc[next_trading_day]
        this_close = self.close_prices.loc[today]
        change = next_open / this_close - 1
        up_limit = change[change > 0.09].index
        for stock in up_limit:
            if stock in universe:
                universe.remove(stock)


@AbstractMod.register
class ActivelyTraded(AbstractMod):
    """ActivelyTraded模块
    会自动将universe中交易额小于阈值的股票去除。
    """
    def __init__(self, threshold=10000):
        self.strategy = None
        self.threshold = threshold
        self.amount = wind.get_wind_data("AShareEODPrices", "s_dq_amount")

    def __plug_in__(self, caller):
        self.strategy = caller
        self.strategy.event_manager.register(EventType.GET_UNIVERSE, self.handle_universe)

    def handle_universe(self, universe):
        today = self.strategy.today
        today_amount = self.amount.loc[today]
        for stock in universe:
            if today_amount[stock] < self.threshold:
                universe.remove(stock)

