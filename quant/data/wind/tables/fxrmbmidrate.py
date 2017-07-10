from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class FXRMBMidRate(BaseModel):
    """
    中国外汇市场汇率

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

    """
    object_id = Column(VARCHAR2(100))
    crncy_code = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    crncy_midrate = Column(NUMBER(20,6))
    
