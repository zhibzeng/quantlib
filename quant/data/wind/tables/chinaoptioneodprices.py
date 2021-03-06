from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class ChinaOptionEODPrices(BaseModel):
    """
    4.195 中国期权日行情

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    s_dq_open: NUMBER(20,4)
        开盘价(元)   
    s_dq_high: NUMBER(20,4)
        最高价(元)   
    s_dq_low: NUMBER(20,4)
        最低价(元)   
    s_dq_close: NUMBER(20,4)
        收盘价(元)   
    s_dq_settle: NUMBER(20,4)
        结算价(元)   
    s_dq_volume: NUMBER(20,4)
        成交量(手)   
    s_dq_amount: NUMBER(20,4)
        成交金额(万元)   
    s_dq_oi: NUMBER(20,4)
        持仓量(手)   
    s_dq_oichange: NUMBER(20,4)
        持仓量变化(手)   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "ChinaOptionEODPrices"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    s_dq_open = Column(NUMBER(20,4))
    s_dq_high = Column(NUMBER(20,4))
    s_dq_low = Column(NUMBER(20,4))
    s_dq_close = Column(NUMBER(20,4))
    s_dq_settle = Column(NUMBER(20,4))
    s_dq_volume = Column(NUMBER(20,4))
    s_dq_amount = Column(NUMBER(20,4))
    s_dq_oi = Column(NUMBER(20,4))
    s_dq_oichange = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
