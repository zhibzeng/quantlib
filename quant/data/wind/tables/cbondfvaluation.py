from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondFValuation(BaseModel):
    """
    中国国债期货可交割券衍生指标

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   

    """
    object_id = Column(VARCHAR2(100))
    
