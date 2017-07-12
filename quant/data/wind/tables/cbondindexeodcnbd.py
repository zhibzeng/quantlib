from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondIndexEODCNBD(BaseModel):
    """
    中债登指数行情

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        日期   
    s_dq_close: NUMBER(20,4)
        指数值   
    s_val_pe: NUMBER(20,4)
        指数总市值(亿元)   
    avgmvduration: NUMBER(20,4)
        平均市值法久期   

    """
    __tablename__ = "CBondIndexEODCNBD"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    s_dq_close = Column(NUMBER(20,4))
    s_val_pe = Column(NUMBER(20,4))
    avgmvduration = Column(NUMBER(20,4))
    
