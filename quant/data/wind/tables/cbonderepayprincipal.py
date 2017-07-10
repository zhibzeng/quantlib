from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CbondERepayPrincipal(BaseModel):
    """
    中国债券本金提前偿还明细

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    b_info_repaypridt: VARCHAR2(8)
        本金偿还日期   
    b_info_repayprirate: NUMBER(20,4)
        本金偿还比例   
    b_info_erepaytpe: NUMBER(1,0)
        提前还本方式代码   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    b_info_repaypridt = Column(VARCHAR2(8))
    b_info_repayprirate = Column(NUMBER(20,4))
    b_info_erepaytpe = Column(NUMBER(1,0))
    
