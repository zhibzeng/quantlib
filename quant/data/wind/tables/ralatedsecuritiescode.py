from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class RalatedSecuritiesCode(BaseModel):
    """
    证券关系表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_ralatedcode: VARCHAR2(40)
        关联证券Wind代码   
    s_relation_typcode: VARCHAR2(10)
        关系类型代码   
    s_info_effective_dt: VARCHAR2(8)
        生效日期   
    s_info_invalid_dt: VARCHAR2(8)
        失效日期   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_info_ralatedcode = Column(VARCHAR2(40))
    s_relation_typcode = Column(VARCHAR2(10))
    s_info_effective_dt = Column(VARCHAR2(8))
    s_info_invalid_dt = Column(VARCHAR2(8))
    
