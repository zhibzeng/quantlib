from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


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
    trade_dt: VARCHAR2(8)
        交易日期   
    i_weight: NUMBER(20,4)
        权重   

    """
    __tablename__ = "AIndexHS300FreeWeight"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_con_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    i_weight = Column(NUMBER(20,4))
    
