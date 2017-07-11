from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareCalendar(BaseModel):
    """
    中国A股交易日历

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    trade_days: VARCHAR2(8)
        交易日   
    s_info_exchmarket: VARCHAR2(40)
        交易所英文简称   

    """
    object_id = Column(VARCHAR2(100))
    trade_days = Column(VARCHAR2(8))
    s_info_exchmarket = Column(VARCHAR2(40))
    
