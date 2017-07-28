from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondIBRMBMonDMarOview(BaseModel):
    """
    4.156 银行间本币货币市场日统计

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    trade_dt: VARCHAR2(8)
        交易日期   
    s_info_typecode: VARCHAR2(40)
        交易品种代码   
    b_dq_type: VARCHAR2(80)
        交易品种   
    b_dq_number: NUMBER(20,8)
        成交笔数   
    b_dq_nochange: NUMBER(20,8)
        成交笔数增减   
    b_dq_tradingvalue: NUMBER(20,8)
        成交额(亿元)   
    b_dq_vchange: NUMBER(20,8)
        成交额增减(亿元)   
    b_dq_wavrate: NUMBER(20,8)
        加权平均利率   
    b_dq_bpchange: NUMBER(20,8)
        升降基点   
    b_dq_nomembersinvo: NUMBER(20,8)
        参与成员家数   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondIBRMBMonDMarOview"
    object_id = Column(VARCHAR2(100), primary_key=True)
    trade_dt = Column(VARCHAR2(8))
    s_info_typecode = Column(VARCHAR2(40))
    b_dq_type = Column(VARCHAR2(80))
    b_dq_number = Column(NUMBER(20,8))
    b_dq_nochange = Column(NUMBER(20,8))
    b_dq_tradingvalue = Column(NUMBER(20,8))
    b_dq_vchange = Column(NUMBER(20,8))
    b_dq_wavrate = Column(NUMBER(20,8))
    b_dq_bpchange = Column(NUMBER(20,8))
    b_dq_nomembersinvo = Column(NUMBER(20,8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
