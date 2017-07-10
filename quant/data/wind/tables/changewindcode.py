from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class ChangeWindcode(BaseModel):
    """
    Wind代码变更表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   

    """
    object_id = Column(VARCHAR2(100))
    
