from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondPrices(BaseModel):
    """
    4.152 中国债券行情-全价

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    b_dq_open: NUMBER(20,8)
        开盘价(元)   
    b_dq_high: NUMBER(20,8)
        最高价(元)   
    b_dq_low: NUMBER(20,8)
        最低价(元)   
    b_dq_originclose: NUMBER(20,8)
        收盘价(元)   
    b_dq_volume: NUMBER(20,8)
        成交量(手)   
    b_dq_amount: NUMBER(20,8)
        成交金额(千元)   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondPrices"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    b_dq_open = Column(NUMBER(20,8))
    b_dq_high = Column(NUMBER(20,8))
    b_dq_low = Column(NUMBER(20,8))
    b_dq_originclose = Column(NUMBER(20,8))
    b_dq_volume = Column(NUMBER(20,8))
    b_dq_amount = Column(NUMBER(20,8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
