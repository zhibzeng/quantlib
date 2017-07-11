from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class ChinaOptionCalendar(BaseModel):
    """
    中国期权交易日历

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    trade_days: VARCHAR2(8)
        交易日   
    s_info_exchmarket: VARCHAR2(40)
        交易所英文简称   DCE:大连商品交易所SSE:上海证券交易所SZSE:深圳证券交易所

    """
    object_id = Column(VARCHAR2(100))
    trade_days = Column(VARCHAR2(8))
    s_info_exchmarket = Column(VARCHAR2(40))
    
