from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondHolder(BaseModel):
    """
    中国债券持有人

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    s_info_enddate: VARCHAR2(8)
        截止日期   
    s_fa_latelyrd: VARCHAR2(8)
        报告期   
    b_info_holder: VARCHAR2(100)
        持有人   
    b_info_holdamount: NUMBER(20,4)
        持有数量(张)   
    b_issuer_sharecategory: VARCHAR2(1)
        持有人类型   1个人；2公司

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    s_info_enddate = Column(VARCHAR2(8))
    s_fa_latelyrd = Column(VARCHAR2(8))
    b_info_holder = Column(VARCHAR2(100))
    b_info_holdamount = Column(NUMBER(20,4))
    b_issuer_sharecategory = Column(VARCHAR2(1))
    
