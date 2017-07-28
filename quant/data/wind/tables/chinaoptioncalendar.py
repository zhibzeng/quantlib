from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class ChinaOptionCalendar(BaseModel):
    """
    4.194 中国期权交易日历

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    trade_days: VARCHAR2(8)
        交易日   
    s_info_exchmarket: VARCHAR2(40)
        交易所英文简称   DCE:大连商品交易所SSE:上海证券交易所SZSE:深圳证券交易所
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "ChinaOptionCalendar"
    object_id = Column(VARCHAR2(100), primary_key=True)
    trade_days = Column(VARCHAR2(8))
    s_info_exchmarket = Column(VARCHAR2(40))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
