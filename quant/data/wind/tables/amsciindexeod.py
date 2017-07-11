from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AMSCIIndexEOD(BaseModel):
    """
    MSCI指数行情

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        指数Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    s_dq_close_std_: NUMBER(20,6)
        收盘价(STD)   
    s_dq_close_grs_: NUMBER(20,6)
        收盘价(GRS)   
    s_dq_close_net_: NUMBER(20,6)
        收盘价(NET)   
    s_dq_clomktcap: NUMBER(20,6)
        收盘市值(百万元)   
    s_dq_adjmktcap: NUMBER(20,6)
        调整市值(百万元)   
    s_dq_islocalcrncy: NUMBER(1,0)
        是否本地货币   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    s_dq_close_std_ = Column(NUMBER(20,6))
    s_dq_close_grs_ = Column(NUMBER(20,6))
    s_dq_close_net_ = Column(NUMBER(20,6))
    s_dq_clomktcap = Column(NUMBER(20,6))
    s_dq_adjmktcap = Column(NUMBER(20,6))
    s_dq_islocalcrncy = Column(NUMBER(1,0))
    
