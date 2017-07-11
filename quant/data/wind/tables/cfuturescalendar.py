from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


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
    __tablename__ = "CFuturesCalendar"
    object_id = Column(VARCHAR2(100), primary_key=True)
    trade_days = Column(VARCHAR2(8))
    s_info_exchmarket = Column(VARCHAR2(40))
    
