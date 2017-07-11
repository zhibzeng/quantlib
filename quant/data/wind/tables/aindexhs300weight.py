from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AIndexHS300Weight(BaseModel):
    """
    沪深300指数成份股权重

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        指数Wind代码   
    s_con_windcode: VARCHAR2(40)
        成份股Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    i_weight: NUMBER(20,4)
        权重   
    s_in_index: NUMBER(20,2)
        计算用股本(股)   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_con_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    i_weight = Column(NUMBER(20,4))
    s_in_index = Column(NUMBER(20,2))
    
