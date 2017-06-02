"""处理Universe的Mod"""
from datetime import timedelta
import pandas as pd
from ..common.mods import AbstractMod
from ..common.events import EventType
from ...data.wind import get_wind_rawdata, get_wind_data


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
        st = get_wind_rawdata("AShareST", parse_dates={"entry_dt": "%Y%m%d", "remove_dt": "%Y%m%d"})
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
        self.ipo = get_wind_rawdata("AShareIPO", parse_dates={"s_ipo_listdate": "%Y%m%d"})
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
class ActivelyTraded(AbstractMod):
    """ActivelyTraded模块
    会自动将universe中交易额小于阈值的股票去除。
    """
    def __init__(self, threshold=10000):
        self.strategy = None
        self.threshold = threshold
        self.amount = get_wind_data("AShareEODPrices", "s_dq_amount")

    def __plug_in__(self, caller):
        self.strategy = caller
        self.strategy.event_manager.register(EventType.GET_UNIVERSE, self.handle_universe)

    def handle_universe(self, universe):
        today = self.strategy.today
        today_amount = self.amount.loc[today]
        for stock in universe:
            if today_amount[stock] < self.threshold:
                universe.remove(stock)

