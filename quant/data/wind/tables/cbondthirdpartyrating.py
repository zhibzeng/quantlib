from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondThirdPartyRating(BaseModel):
    """
    中国债券第三方信用评级

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_compname: VARCHAR2(100)
        公司名称   
    s_info_compcode: VARCHAR2(10)
        公司id   

    """
    object_id = Column(VARCHAR2(100))
    s_info_compname = Column(VARCHAR2(100))
    s_info_compcode = Column(VARCHAR2(10))
    
