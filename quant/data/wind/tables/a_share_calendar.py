"""A股交易日历"""
from ....common.db.sql import BaseModel, Column, VARCHAR, Numeric, DateTime


class AShareCalendar(BaseModel):
    """A股交易日历

    Attributes
    ----------
    object_id
        主键
    trade_days
        交易日
    s_info_exchmarket
        交易所英文简称
    opdate

    opmode
    """
    __tablename__ = "AIndexCalendar"
    object_id = Column(VARCHAR(100), primary_key=True)
    trade_days = Column(VARCHAR(8))
    s_info_exchmarket = Column(VARCHAR(40))
    opdate = Column(DateTime)
    opmode = Column(VARCHAR(1))
