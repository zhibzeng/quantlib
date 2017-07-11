from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


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
    __tablename__ = "CBIndexWeightCNBD"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_con_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    i_weight = Column(NUMBER(20,8))
    
