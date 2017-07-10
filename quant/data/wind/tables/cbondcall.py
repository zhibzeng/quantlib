from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondCall(BaseModel):
    """
    中国债券赎回条款执行说明

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    b_info_redemptiondate: VARCHAR2(8)
        赎回日   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    b_info_redemptiondate = Column(VARCHAR2(8))
    
