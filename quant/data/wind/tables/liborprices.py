from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class LiborPrices(BaseModel):
    """
    4.172 Libor行情

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    b_info_rate: NUMBER(20,4)
        利率(%)   
    crncy_code: VARCHAR2(40)
        货币代码   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "LiborPrices"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    b_info_rate = Column(NUMBER(20,4))
    crncy_code = Column(VARCHAR2(40))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
