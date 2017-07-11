from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AIndexHS300CloseWeight(BaseModel):
    """
    沪深300指数成份股收盘权重

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
    i_weight_11: NUMBER(20,2)
        总股本(股)   
    i_weight_12: NUMBER(20,4)
        自由流通比例(%)(归档后)   
    i_weight_14: NUMBER(20,8)
        权重因子   
    i_weight_15: NUMBER(20,4)
        收盘   
    i_weight_16: NUMBER(20,4)
        调整后开盘参考价   
    i_weight_17: NUMBER(20,2)
        总市值   
    i_weight_18: NUMBER(20,2)
        计算用市值   

    """
    __tablename__ = "AIndexHS300CloseWeight"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_con_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    i_weight = Column(NUMBER(20,4))
    s_in_index = Column(NUMBER(20,2))
    i_weight_11 = Column(NUMBER(20,2))
    i_weight_12 = Column(NUMBER(20,4))
    i_weight_14 = Column(NUMBER(20,8))
    i_weight_15 = Column(NUMBER(20,4))
    i_weight_16 = Column(NUMBER(20,4))
    i_weight_17 = Column(NUMBER(20,2))
    i_weight_18 = Column(NUMBER(20,2))
    
