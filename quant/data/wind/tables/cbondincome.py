from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondIncome(BaseModel):
    """
    中国债券发行主体利润表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_compcode: VARCHAR2(40)
        公司ID   None

    """
    object_id = Column(VARCHAR2(100))
    s_info_compcode = Column(VARCHAR2(40))
    
