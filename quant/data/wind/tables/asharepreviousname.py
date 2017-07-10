from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class ASharePreviousName(BaseModel):
    """
    中国A股证券曾用名

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

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    begindate = Column(VARCHAR2(8))
    enddate = Column(VARCHAR2(8))
    ann_dt = Column(VARCHAR2(8))
    s_info_name = Column(VARCHAR2(40))
    changereason = Column(NUMBER(9,0))
    
