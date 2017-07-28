from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareCalendar(BaseModel):
    """
    4.26 中国A股交易日历

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    trade_days: VARCHAR2(8)
        交易日   
    s_info_exchmarket: VARCHAR2(40)
        交易所英文简称   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareCalendar"
    object_id = Column(VARCHAR2(100), primary_key=True)
    trade_days = Column(VARCHAR2(8))
    s_info_exchmarket = Column(VARCHAR2(40))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
