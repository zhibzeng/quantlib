from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondAccruedInterest(BaseModel):
    """
    4.142 中国债券应计利息

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    b_anal_accrueddays: NUMBER(20,4)
        已计息时间   
    b_anal_accruedinterest: NUMBER(20,8)
        应计利息   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondAccruedInterest"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    b_anal_accrueddays = Column(NUMBER(20,4))
    b_anal_accruedinterest = Column(NUMBER(20,8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
