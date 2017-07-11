from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CFuturesmarginratio(BaseModel):
    """
    中国期货保证金比例

    Attributes
    ----------
    object_id: VARCHAR2(38)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        合约Wind代码   
    marginratio: VARCHAR2(40)
        保证金比例   
    trade_dt: VARCHAR2(8)
        变动日期   

    """
    __tablename__ = "CFuturesmarginratio"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    marginratio = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    
