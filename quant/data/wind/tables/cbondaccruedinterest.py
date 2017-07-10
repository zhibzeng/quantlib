from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondAccruedInterest(BaseModel):
    """
    中国债券应计利息

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   

    """
    object_id = Column(VARCHAR2(100))
    
