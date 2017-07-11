from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CGoldSpotEODPrices(BaseModel):
    """
    中国黄金现货日行情

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        日期   
    s_dq_open: NUMBER(20,4)
        开盘价(元)   
    s_dq_high: NUMBER(20,4)
        最高价(元)   
    s_dq_low: NUMBER(20,4)
        最低价(元)   
    s_dq_close: NUMBER(20,4)
        收盘价(元)   
    s_dq_avgprice: NUMBER(20,4)
        均价(元)   
    s_dq_volume: NUMBER(20,4)
        成交量(千克)   
    s_dq_amount: NUMBER(20,4)
        成交金额(元)   
    s_dq_oi: NUMBER(20,4)
        持仓量(手)   
    del_amt: NUMBER(20,4)
        交收量(手)   

    """
    __tablename__ = "CGoldSpotEODPrices"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    s_dq_open = Column(NUMBER(20,4))
    s_dq_high = Column(NUMBER(20,4))
    s_dq_low = Column(NUMBER(20,4))
    s_dq_close = Column(NUMBER(20,4))
    s_dq_avgprice = Column(NUMBER(20,4))
    s_dq_volume = Column(NUMBER(20,4))
    s_dq_amount = Column(NUMBER(20,4))
    s_dq_oi = Column(NUMBER(20,4))
    del_amt = Column(NUMBER(20,4))
    
