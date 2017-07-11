from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareTypeCode(BaseModel):
    """
    类型编码表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_typname: VARCHAR2(300)
        类型名称   
    s_typcode: VARCHAR2(40)
        类型代码   
    s_origin_typcode: VARCHAR2(40)
        原始类型代码   对应9位代码
    s_classification: VARCHAR2(40)
        分类   对应不规则代码1.万得代码后缀2.评级分类代码3.信用评级机构

    """
    object_id = Column(VARCHAR2(100))
    s_typname = Column(VARCHAR2(300))
    s_typcode = Column(VARCHAR2(40))
    s_origin_typcode = Column(VARCHAR2(40))
    s_classification = Column(VARCHAR2(40))
    
