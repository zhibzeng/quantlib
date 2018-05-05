import calendar
from datetime import timedelta
from dateutil.parser import parse
from .trading_calendar import trading_calendar


class MonthCalendar:
    """
    应对python自带的timedelta不能以月为单位加减的问题。
    自带
    """
    def __init__(self, year: int, month: int):
        """
        Parameters
        ==========
        year: int
            年份
        month: int
            月份
        """
        self.year = year
        self.month = month

    def last_day(self, format_str=True):
        """
        返回当前年月最后一天的日期

        Parameters
        ==========
        format_str: bool
            如果为真，把日期转换成字符串，否则返回datetime
        """
        _, last_day = calendar.monthrange(self.year, self.month)
        day = "%d-%02d-%02d" % (self.year, self.month, last_day)
        if format_str:
            return day
        else:
            return parse(day)

    def first_day(self, format_str=True):
        """
        返回当前年月第一天的日期

        Parameters
        ==========
        format_str: bool
            如果为真，把日期转换成字符串，否则返回datetime
        """
        day = "%d-%02d-01" % (self.year, self.month)
        if format_str:
            return day
        else:
            return parse(day)

    def first_trading_day(self, format_str=True):
        """
        返回当前年月第一个交易日的日期

        Parameters
        ==========
        format_str: bool
            如果为真，把日期转换成字符串，否则返回datetime
        """
        holidays = trading_calendar.holidays
        day = parse(self.first_day())
        while day in holidays:
            day += timedelta(days=1)
        if format_str:
            return day.strftime("%Y-%m-%d")
        else:
            return day

    def last_trading_day(self, format_str=True):
        """
        返回当前年月最后一个交易日的日期

        Parameters
        ==========
        format_str: bool
            如果为真，把日期转换成字符串，否则返回datetime
        """
        holidays = trading_calendar.holidays
        day = parse(self.last_day())
        while day in holidays:
            day -= timedelta(days=1)
        if format_str:
            return day.strftime("%Y-%m-%d")
        else:
            return day

    def add_months(self, n: int):
        """
        返回当前年月的n个月之后。n为负数表示n个月之前。

        Parameters
        ==========
        n: int
            移动的月份数
        """
        year = self.year
        month = self.month + n
        while month > 12:
            month -= 12
            year += 1
        while month < 1:
            month += 12
            year -= 1
        return Calendar(year, month)

    @staticmethod
    def iterate(start_date: str, end_date: str, months: int=1):
        """
        返回从起始日期到结束日期间的每个月

        Parameters
        ----------
        start_date: str
            起始日期
        end_date: str
            结束日期
        months: int
            间隔

        Yields
        ------
        Calendar
        """
        start_date = parse(start_date)
        end_date = parse(end_date)
        year, month = start_date.year, start_date.month
        while (year, month) <= (end_date.year, end_date.month):
            yield Calendar(year, month)
            month += months
            while month > 12:
                month -= 12
                year += 1
