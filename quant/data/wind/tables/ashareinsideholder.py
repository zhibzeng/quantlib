from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareInsideHolder(BaseModel):
    """
    中国A股内部人持股变动(中国A股前十大股东)

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    s_holder_enddate: VARCHAR2(8)
        截止日期   
    s_holder_holdercategory: VARCHAR2(1)
        股东类型   1：个人；2：公司
    s_holder_name: VARCHAR2(100)
        股东名称   容错后的名称
    s_holder_quantity: NUMBER(20,4)
        持股数量   
    s_holder_pct: NUMBER(20,4)
        持股比例   
    s_holder_sharecategory: VARCHAR2(40)
        持股性质代码   
    s_holder_restrictedquantity: NUMBER(20,4)
        持有限售股份(非流通股)数量   
    s_holder_aname: VARCHAR2(100)
        股东名称   公布的名称
    s_holder_sequence: VARCHAR2(10)
        关联方序号   同一组关联股东为同一序号
    s_holder_sharecategoryname: VARCHAR2(200)
        持股性质   

    """
    __tablename__ = "AShareInsideHolder"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    s_holder_enddate = Column(VARCHAR2(8))
    s_holder_holdercategory = Column(VARCHAR2(1))
    s_holder_name = Column(VARCHAR2(100))
    s_holder_quantity = Column(NUMBER(20,4))
    s_holder_pct = Column(NUMBER(20,4))
    s_holder_sharecategory = Column(VARCHAR2(40))
    s_holder_restrictedquantity = Column(NUMBER(20,4))
    s_holder_aname = Column(VARCHAR2(100))
    s_holder_sequence = Column(VARCHAR2(10))
    s_holder_sharecategoryname = Column(VARCHAR2(200))
    
