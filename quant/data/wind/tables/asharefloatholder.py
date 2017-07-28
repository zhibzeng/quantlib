from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareFloatHolder(BaseModel):
    """
    4.39 中国A股流通股东

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
        持有人   
    s_holder_quantity: NUMBER(20,4)
        数量(股)   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareFloatHolder"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    s_holder_enddate = Column(VARCHAR2(8))
    s_holder_holdercategory = Column(VARCHAR2(1))
    s_holder_name = Column(VARCHAR2(100))
    s_holder_quantity = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
