import calendar
from datetime import timedelta
from dateutil.parser import parse
from .trading_calendar import trading_calendar


class MonthlyCalendar:
    """
    Only contains year and month
    """
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def last_day(self, format_str=True):
        _, last_day = calendar.monthrange(self.year, self.month)
        day = "%d-%02d-%02d" % (self.year, self.month, last_day)
        if format_str:
            return day
        else:
            return parse(day)

    def first_day(self, format_str=True):
        day = "%d-%02d-01" % (self.year, self.month)
        if format_str:
            return day
        else:
            return parse(day)

    def first_trading_day(self, format_str=True):
        holidays = trading_calendar.holidays
        day = parse(self.first_day())
        while day in holidays:
            day += timedelta(days=1)
        if format_str:
            return day.strftime("%Y-%m-%d")
        else:
            return day

    def last_trading_day(self, format_str=True):
        holidays = trading_calendar.holidays
        day = parse(self.last_day())
        while day in holidays:
            day -= timedelta(days=1)
        if format_str:
            return day.strftime("%Y-%m-%d")
        else:
            return day

    def add_months(self, n):
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
    def iterate(start_date, end_date, months=1):
        """
        Parameters
        ----------
        start_date: str
            start date
        end_date: str
            end date
        months: int
            step

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
