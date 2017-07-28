from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class ASharePreviousName(BaseModel):
    """
    4.8 中国A股证券曾用名

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    begindate: VARCHAR2(8)
        起始日期   
    enddate: VARCHAR2(8)
        截止日期   
    ann_dt: VARCHAR2(8)
        公告日期   
    s_info_name: VARCHAR2(40)
        证券简称   
    changereason: NUMBER(9,0)
        变动原因代码   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "ASharePreviousName"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    begindate = Column(VARCHAR2(8))
    enddate = Column(VARCHAR2(8))
    ann_dt = Column(VARCHAR2(8))
    s_info_name = Column(VARCHAR2(40))
    changereason = Column(NUMBER(9,0))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
