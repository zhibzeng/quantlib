"""A股股票每日收盘行情"""
from ....common.db.sql import BaseModel, Column, VARCHAR, Numeric, DateTime


class AShareEODPrices(BaseModel):
    """A股股票每日收盘行情

    Attributes
    ----------
    object_id
        主键
    s_info_windcode
        万得代码， eg. 600030.SH
    trade_dt
        日期 YYYYMMDD
    crncy_code

    s_dq_preclose
        前收盘价
    s_dq_open
        开盘价
    s_dq_high
        最高价
    s_dq_low
        最低价
    s_dq_close
        收盘价
    s_dq_change
        涨跌
    s_dq_pctchange
        涨跌幅
    s_dq_volume
        成交量
    s_dq_amount
        成交额
    s_dq_adjpreclose
        复权前收盘价
    s_dq_adjopen
        复权开盘价
    s_dq_adjhigh
        复权最高价
    s_dq_adjlow
        复权最低价
    s_dq_adjclose
        复权收盘价
    s_dq_adjfactor
        复权因子
    s_dq_avgprice
        平均价格
    s_dq_tradestatus

    sec_id

    opdate

    opmode

    """
    __tablename__ = "AShareEODPrices".upper()
    object_id = Column(VARCHAR(100), primary_key=True)
    s_info_windcode = Column(VARCHAR(40))
    trade_dt = Column(VARCHAR(8))
    crncy_code = Column(VARCHAR(10))
    s_dq_preclose = Column(Numeric(20, 4, asdecimal=False))
    s_dq_open = Column(Numeric(20, 4, asdecimal=False))
    s_dq_high = Column(Numeric(20, 4, asdecimal=False))
    s_dq_low = Column(Numeric(20, 4, asdecimal=False))
    s_dq_close = Column(Numeric(20, 4, asdecimal=False))
    s_dq_change = Column(Numeric(20, 4, asdecimal=False))
    s_dq_pctchange = Column(Numeric(20, 4, asdecimal=False))
    s_dq_volume = Column(Numeric(20, 4, asdecimal=False))
    s_dq_amount = Column(Numeric(20, 4, asdecimal=False))
    s_dq_adjpreclose = Column(Numeric(20, 4, asdecimal=False))
    s_dq_adjopen = Column(Numeric(20, 4, asdecimal=False))
    s_dq_adjhigh = Column(Numeric(20, 4, asdecimal=False))
    s_dq_adjlow = Column(Numeric(20, 4, asdecimal=False))
    s_dq_adjclose = Column(Numeric(20, 4, asdecimal=False))
    s_dq_adjfactor = Column(Numeric(20, 6, asdecimal=False))
    s_dq_avgprice = Column(Numeric(20, 4, asdecimal=False))
    s_dq_tradestatus = Column(VARCHAR(10))
    opdate = Column(DateTime)
    opmode = Column(VARCHAR(1))
