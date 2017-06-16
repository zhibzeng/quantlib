import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay
from ...common.localize import LOCALIZER
from ...data.wind import get_wind_data

__all__ = ["TradingCalendar"]


class TradingCalendar:
    """中国金融市场交易日历"""
    def __init__(self):
        self.__holidays = None

    # @staticmethod
    # @LOCALIZER.wrap("holiday")
    # def get_holidays():
    #     """到上期所网站获取期货市场休市日期"""
    #     import lxml.etree
    #     url = 'http://www.cffex.com.cn/sj/jyrl/index_6782.xml'
    #     tree = lxml.etree.parse(url)
    #     root = tree.getroot()
    #     holidays = root.xpath("doc[contains(title/text(), '休市')]/pubDate/text()")
    #     return pd.Series(holidays)

    @staticmethod
    @LOCALIZER.wrap("holiday")
    def get_holidays():
        index_data = get_wind_data("AIndexEODPrices", "s_dq_close")["000905.SH"].dropna()
        index_trading_days = list(index_data.index)
        all_days = pd.date_range(start=index_trading_days[0], end=index_trading_days[-1])
        holidays = sorted(filter(lambda day: day.weekday() < 5, set(all_days) - set(index_trading_days)))
        return pd.Series(holidays)

    @property
    def holidays(self):
        """
        中国期货市场休市日期

        type: List[str]
        """
        if not self.__holidays:
            self.__holidays = list(self.get_holidays())
        return self.__holidays

    @property
    def TradingDay(self):
        """根据获取的节假日信息生成pd.tseries.offsets.CustomBusinessDay对象"""
        return CustomBusinessDay(holidays=self.holidays)

trading_calendar = TradingCalendar()
TDay = trading_calendar.TradingDay
"""Trading Day, as pd.tseries.offset.CustomBusinessDay"""
