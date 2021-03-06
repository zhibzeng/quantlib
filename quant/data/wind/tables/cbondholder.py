from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondHolder(BaseModel):
    """
    4.123 中国债券持有人

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
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondHolder"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    s_info_enddate = Column(VARCHAR2(8))
    s_fa_latelyrd = Column(VARCHAR2(8))
    b_info_holder = Column(VARCHAR2(100))
    b_info_holdamount = Column(NUMBER(20,4))
    b_issuer_sharecategory = Column(VARCHAR2(1))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
