from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBIndexWeightCNBD(BaseModel):
    """
    中债登指数权重

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        指数Wind代码   
    s_con_windcode: VARCHAR2(40)
        成份债Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    i_weight: NUMBER(20,8)
        权重   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_con_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    i_weight = Column(NUMBER(20,8))
    
