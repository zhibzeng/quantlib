from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondInsideHolder(BaseModel):
    """
    中国债券内部人持股变动

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_compcode: VARCHAR2(40)
        公司ID   
    s_info_compname: VARCHAR2(200)
        公司名称   
    ann_dt: VARCHAR2(8)
        公告日期   
    b_holder_enddate: VARCHAR2(8)
        截止日期   
    b_holder_holdercategory: VARCHAR2(1)
        股东类型   1：个人；2：公司
    b_holder_name: VARCHAR2(200)
        股东名称   容错后的名称
    b_holder_quantity: NUMBER(20,4)
        持股数量   
    b_holder_pct: NUMBER(20,4)
        持股比例   
    b_holder_sharecategory: VARCHAR2(40)
        持股性质   
    b_holder_aname: VARCHAR2(100)
        股东名称   公布的名称

    """
    object_id = Column(VARCHAR2(100))
    s_info_compcode = Column(VARCHAR2(40))
    s_info_compname = Column(VARCHAR2(200))
    ann_dt = Column(VARCHAR2(8))
    b_holder_enddate = Column(VARCHAR2(8))
    b_holder_holdercategory = Column(VARCHAR2(1))
    b_holder_name = Column(VARCHAR2(200))
    b_holder_quantity = Column(NUMBER(20,4))
    b_holder_pct = Column(NUMBER(20,4))
    b_holder_sharecategory = Column(VARCHAR2(40))
    b_holder_aname = Column(VARCHAR2(100))
    
