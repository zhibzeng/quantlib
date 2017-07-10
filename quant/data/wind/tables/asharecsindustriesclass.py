from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareCSIndustriesClass(BaseModel):
    """
    中国A股中证行业成分明细

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   

    """
    object_id = Column(VARCHAR2(100))
    
