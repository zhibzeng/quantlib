"""回测时使用的行情接口"""
from .events import EventType
from ...data import wind


class AShareMarket:
    """回测中的行情接口，用这个代替wind.get_wind_data，避免使用未来数据"""
    def __init__(self, strategy):
        self.strategy = strategy
        self.market_data = None
        self.trading_days = None
        self.today = None
        self.today_market = None
        self.strategy.event_manager.register(EventType.BACKTEST_NEWDAY, self.on_newday, 1)

    def initalize_market(self, start_date, end_date):
        self.market_data = wind.get_wind_data("AShareEODPrices",
                                              "s_dq_pctchange").truncate(start_date, end_date) / 100
        self.market_data["CASH"] = 0
        self.trading_days = self.market_data.index

    def on_newday(self, today):
        self.today = today
        self.today_market = self.market_data.loc[today][:-1]

    def get_wind_data(self, *args, **kwargs):
        """封装wind.get_wind_data,避免未来数据"""
        data = wind.get_wind_data(*args, **kwargs)
        return data.truncate(None, self.today)

    def get_wind_rawdata(self, *args, **kwargs):
        """封装wind.get_wind_rawdata,避免未来数据"""
        today = self.strategy.today
        data = wind.get_wind_rawdata(*args, **kwargs)
        return data.truncate(None, today)
