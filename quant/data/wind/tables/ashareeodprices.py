from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareEODPrices(BaseModel):
    """
    中国A股日行情

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    crncy_code: VARCHAR2(10)
        货币代码   
    s_dq_preclose: NUMBER(20,4)
        昨收盘价(元)   
    s_dq_open: NUMBER(20,4)
        开盘价(元)   
    s_dq_high: NUMBER(20,4)
        最高价(元)   
    s_dq_low: NUMBER(20,4)
        最低价(元)   
    s_dq_close: NUMBER(20,4)
        收盘价(元)   
    s_dq_change: NUMBER(20,4)
        涨跌(元)   
    s_dq_pctchange: NUMBER(20,4)
        涨跌幅(%)   
    s_dq_volume: NUMBER(20,4)
        成交量(手)   
    s_dq_amount: NUMBER(20,4)
        成交金额(千元)   
    s_dq_adjpreclose: NUMBER(20,4)
        复权昨收盘价(元)   昨收盘价*复权因子
    s_dq_adjopen: NUMBER(20,4)
        复权开盘价(元)   开盘价*复权因子
    s_dq_adjhigh: NUMBER(20,4)
        复权最高价(元)   最高价*复权因子
    s_dq_adjlow: NUMBER(20,4)
        复权最低价(元)   最低价*复权因子
    s_dq_adjclose: NUMBER(20,4)
        复权收盘价(元)   收盘价*复权因子
    s_dq_adjfactor: NUMBER(20,6)
        复权因子   初始值为1；当日复权因子=前一交易日收盘价/当日昨收盘价*前一交易日复权因子。
    s_dq_avgprice: NUMBER(20,4)
        均价(VWAP)   成交金额/成交量
    s_dq_tradestatus: VARCHAR2(10)
        交易状态   

    """
    __tablename__ = "AShareEODPrices"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    crncy_code = Column(VARCHAR2(10))
    s_dq_preclose = Column(NUMBER(20,4))
    s_dq_open = Column(NUMBER(20,4))
    s_dq_high = Column(NUMBER(20,4))
    s_dq_low = Column(NUMBER(20,4))
    s_dq_close = Column(NUMBER(20,4))
    s_dq_change = Column(NUMBER(20,4))
    s_dq_pctchange = Column(NUMBER(20,4))
    s_dq_volume = Column(NUMBER(20,4))
    s_dq_amount = Column(NUMBER(20,4))
    s_dq_adjpreclose = Column(NUMBER(20,4))
    s_dq_adjopen = Column(NUMBER(20,4))
    s_dq_adjhigh = Column(NUMBER(20,4))
    s_dq_adjlow = Column(NUMBER(20,4))
    s_dq_adjclose = Column(NUMBER(20,4))
    s_dq_adjfactor = Column(NUMBER(20,6))
    s_dq_avgprice = Column(NUMBER(20,4))
    s_dq_tradestatus = Column(VARCHAR2(10))
    
