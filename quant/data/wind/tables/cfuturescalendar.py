from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CFuturesCalendar(BaseModel):
    """
    中国期货交易日历

    Attributes
    ----------
    object_id: VARCHAR2(38)
        对象ID   
    trade_days: VARCHAR2(8)
        日期   交易日
    s_info_exchmarket: VARCHAR2(40)
        交易所英文简称   

    """
    object_id = Column(VARCHAR2(38))
    trade_days = Column(VARCHAR2(8))
    s_info_exchmarket = Column(VARCHAR2(40))
    
