import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay
from ...common.localize import LOCALIZER

__all__ = ["TradingCalendar"]


class TradingCalendar:
    """中国金融市场交易日历"""
    def __init__(self):
        self.__holidays = None

    @staticmethod
    @LOCALIZER.wrap("holiday")
    def get_holidays():
        """到上期所网站获取期货市场休市日期"""
        import lxml.etree
        url = 'http://www.cffex.com.cn/sj/jyrl/index_6782.xml'
        tree = lxml.etree.parse(url)
        root = tree.getroot()
        holidays = root.xpath("doc[contains(title/text(), '休市')]/pubDate/text()")
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
