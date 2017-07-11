from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CBondIBRMBMonDMarQuotation(BaseModel):
    """
    银行间本币货币市场日行情

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    b_dq_type: VARCHAR2(80)
        交易品种   
    trade_dt: VARCHAR2(8)
        交易日期   
    b_dq_open: NUMBER(20,8)
        开盘利率   
    b_dq_high: NUMBER(20,8)
        最高利率   
    b_dq_low: NUMBER(20,8)
        最低利率   
    b_dq_originclose: NUMBER(20,8)
        收盘利率   
    b_dq_waveragerate: NUMBER(20,8)
        加权平均利率   
    b_dq_bpchange: NUMBER(20,8)
        升降(基点)   
    b_dq_volume: NUMBER(20,8)
        成交量(手)   
    b_dq_amount: NUMBER(20,8)
        成交金额(亿元)   
    b_dq_amountchange: NUMBER(20,8)
        成交金额增减(亿元)   

    """
    __tablename__ = "CBondIBRMBMonDMarQuotation"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    b_dq_type = Column(VARCHAR2(80))
    trade_dt = Column(VARCHAR2(8))
    b_dq_open = Column(NUMBER(20,8))
    b_dq_high = Column(NUMBER(20,8))
    b_dq_low = Column(NUMBER(20,8))
    b_dq_originclose = Column(NUMBER(20,8))
    b_dq_waveragerate = Column(NUMBER(20,8))
    b_dq_bpchange = Column(NUMBER(20,8))
    b_dq_volume = Column(NUMBER(20,8))
    b_dq_amount = Column(NUMBER(20,8))
    b_dq_amountchange = Column(NUMBER(20,8))
    
