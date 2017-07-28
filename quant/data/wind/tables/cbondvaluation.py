from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondValuation(BaseModel):
    """
    4.155 中国债券衍生指标

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    b_anal_duration: NUMBER(24,8)
        久期   麦考利久期
    b_anal_modifiedduration: NUMBER(24,8)
        修正久期   
    b_anal_bduration: NUMBER(24,8)
        基准久期   
    b_anal_sduration: NUMBER(24,8)
        利差久期   
    b_anal_convexity: NUMBER(24,8)
        凸性   
    b_anal_accrueddays: NUMBER(20,4)
        已计息时间   
    b_anal_accruedinterest: NUMBER(24,8)
        应计利息   
    b_anal_ytc: NUMBER(24,8)
        赎回收益率(%)   
    b_anal_ytp: NUMBER(24,8)
        回售收益率(%)   
    b_anal_ptmyear: NUMBER(20,4)
        剩余期限(年)   
    b_anal_ytm: NUMBER(24,8)
        到期收益率(%)   
    b_info_weightedrt: NUMBER(24,8)
        加权剩余期限(年)   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondValuation"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    b_anal_duration = Column(NUMBER(24,8))
    b_anal_modifiedduration = Column(NUMBER(24,8))
    b_anal_bduration = Column(NUMBER(24,8))
    b_anal_sduration = Column(NUMBER(24,8))
    b_anal_convexity = Column(NUMBER(24,8))
    b_anal_accrueddays = Column(NUMBER(20,4))
    b_anal_accruedinterest = Column(NUMBER(24,8))
    b_anal_ytc = Column(NUMBER(24,8))
    b_anal_ytp = Column(NUMBER(24,8))
    b_anal_ptmyear = Column(NUMBER(20,4))
    b_anal_ytm = Column(NUMBER(24,8))
    b_info_weightedrt = Column(NUMBER(24,8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
