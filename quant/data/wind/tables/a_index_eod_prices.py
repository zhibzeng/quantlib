"""A股指数每日收盘行情"""
from ....common.db.sql import BaseModel, Column, VARCHAR, Numeric, DateTime


class AIndexEODPrices(BaseModel):
    """A股指数每日收盘行情
    Fields:
        object_id: 主键
        s_info_windcode: 万得代码， eg. 600030.SH
        trade_dt: 日期 YYYYMMDD
        crnry_code:
        s_dq_preclose: 前收盘价
        s_dq_open: 开盘价
        s_dq_high: 最高价
        s_dq_low: 最低价
        s_dq_close: 收盘价
        s_dq_change: 涨跌
        s_dq_pctchange: 涨跌幅
        s_dq_volume: 成交量
        s_dq_amount: 成交额
        sec_id:
        opdata:
        opmode:
    """
    __tablename__ = "AIndexEODPrices"
    object_id = Column(VARCHAR(100), primary_key=True)
    s_info_windcode = Column(VARCHAR(40))
    trade_dt = Column(VARCHAR(8))
    crnry_code = Column(VARCHAR(10))
    s_dq_preclose = Column(Numeric(20, 4, asdecimal=False))
    s_dq_open = Column(Numeric(20, 4, asdecimal=False))
    s_dq_high = Column(Numeric(20, 4, asdecimal=False))
    s_dq_low = Column(Numeric(20, 4, asdecimal=False))
    s_dq_close = Column(Numeric(20, 4, asdecimal=False))
    s_dq_change = Column(Numeric(20, 4, asdecimal=False))
    s_dq_pctchange = Column(Numeric(20, 4, asdecimal=False))
    s_dq_volume = Column(Numeric(20, 4, asdecimal=False))
    s_dq_amount = Column(Numeric(20, 4, asdecimal=False))
    sec_id = Column(VARCHAR(10))
    opdate = Column(DateTime)
    opmode = Column(VARCHAR(1))
