from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class HS300IEODPrices(BaseModel):
    """
    沪深300指数日行情

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
    pre_close: NUMBER(20,4)
        昨收盘价(点)   
    s_dq_open: NUMBER(20,4)
        开盘价(点)   
    s_dq_high: NUMBER(20,4)
        最高价(点)   
    s_dq_low: NUMBER(20,4)
        最低价(点)   
    s_dq_close: NUMBER(20,4)
        收盘价(点)   
    chg: NUMBER(20,4)
        涨跌(点)   
    pct_chg: NUMBER(20,4)
        涨跌幅(%)   
    volume: NUMBER(20,4)
        成交量(手)   
    amt: NUMBER(20,4)
        成交金额(千元)   

    """
    __tablename__ = "HS300IEODPrices"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    crncy_code = Column(VARCHAR2(10))
    pre_close = Column(NUMBER(20,4))
    s_dq_open = Column(NUMBER(20,4))
    s_dq_high = Column(NUMBER(20,4))
    s_dq_low = Column(NUMBER(20,4))
    s_dq_close = Column(NUMBER(20,4))
    chg = Column(NUMBER(20,4))
    pct_chg = Column(NUMBER(20,4))
    volume = Column(NUMBER(20,4))
    amt = Column(NUMBER(20,4))
    
