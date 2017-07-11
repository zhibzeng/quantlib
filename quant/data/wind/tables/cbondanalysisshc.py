from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondAnalysisSHC(BaseModel):
    """
    中国债券上海清算所债券估值

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    b_anal_matu_cnbd: NUMBER(20,4)
        待偿期(年)   
    b_anal_dirty_cnbd: NUMBER(20,4)
        日间估价全价   
    b_anal_accrint_cnbd: NUMBER(20,4)
        日间应计利息   
    b_anal_net_cnbd: NUMBER(20,4)
        估价净价   
    b_anal_yield_cnbd: NUMBER(20,4)
        估价收益率(%)   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    b_anal_matu_cnbd = Column(NUMBER(20,4))
    b_anal_dirty_cnbd = Column(NUMBER(20,4))
    b_anal_accrint_cnbd = Column(NUMBER(20,4))
    b_anal_net_cnbd = Column(NUMBER(20,4))
    b_anal_yield_cnbd = Column(NUMBER(20,4))
    
