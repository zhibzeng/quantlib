from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CFuturesmarginratio(BaseModel):
    """
    中国期货保证金比例

    Attributes
    ----------
    object_id: VARCHAR2(38)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        合约Wind代码   

    """
    object_id = Column(VARCHAR2(38))
    s_info_windcode = Column(VARCHAR2(40))
    
