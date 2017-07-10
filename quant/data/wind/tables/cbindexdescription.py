from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBIndexDescription(BaseModel):
    """
    中国债券指数基本资料

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_code: VARCHAR2(40)
        交易代码   
    s_info_name: VARCHAR2(50)
        证券简称   
    s_info_compname: VARCHAR2(100)
        指数名称   
    s_info_exchmarket: VARCHAR2(40)
        交易所   SSE:上交所SZSE:深交所NIB:银行间市场Others:其他

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_info_code = Column(VARCHAR2(40))
    s_info_name = Column(VARCHAR2(50))
    s_info_compname = Column(VARCHAR2(100))
    s_info_exchmarket = Column(VARCHAR2(40))
    
