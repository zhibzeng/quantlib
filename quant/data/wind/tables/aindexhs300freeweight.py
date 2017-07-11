from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AIndexHS300FreeWeight(BaseModel):
    """
    沪深300免费指数权重

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        指数Wind代码   包含沪深300以外的其他交易所指数
    s_con_windcode: VARCHAR2(40)
        成份股Wind代码   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_con_windcode = Column(VARCHAR2(40))
    
