from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CGBbenchmark(BaseModel):
    """
    中国国债基准收益率

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        日期   
    s_dq_close: NUMBER(20,4)
        利率(%)   
    s_dq_open: NUMBER(20,4)
        开盘利率(%)   
    s_dq_high: NUMBER(20,4)
        最高利率(%)   
    s_dq_low: NUMBER(20,4)
        最低利率(%)   

    """
    __tablename__ = "CGBbenchmark"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    s_dq_close = Column(NUMBER(20,4))
    s_dq_open = Column(NUMBER(20,4))
    s_dq_high = Column(NUMBER(20,4))
    s_dq_low = Column(NUMBER(20,4))
    
