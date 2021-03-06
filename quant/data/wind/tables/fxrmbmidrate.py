from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class FXRMBMidRate(BaseModel):
    """
    4.197 中国外汇市场汇率

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    crncy_code: VARCHAR2(40)
        货币代码   
    trade_dt: VARCHAR2(8)
        日期   
    crncy_midrate: NUMBER(20,6)
        中间价   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "FXRMBMidRate"
    object_id = Column(VARCHAR2(100), primary_key=True)
    crncy_code = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    crncy_midrate = Column(NUMBER(20,6))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
