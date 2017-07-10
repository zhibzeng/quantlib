from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareMergersAcquisitions(BaseModel):
    """
    中国A股收购兼并

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        信息披露方万得代码   
    targetofacquisn: VARCHAR2(100)
        被收购方名称   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    targetofacquisn = Column(VARCHAR2(100))
    
