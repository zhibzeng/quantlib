from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareWeeklyYield(BaseModel):
    """
    中国A股周收益率

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        截至日期   
    crncy_code: VARCHAR2(10)
        货币代码   CNY人民币
    s_wq_pctchange: NUMBER(20,4)
        周收益率   
    s_wq_turn: NUMBER(20,4)
        周换手率(合计)   
    s_wq_avgturn: NUMBER(20,4)
        周换手率(算术平均)   
    s_wq_amount: NUMBER(20,4)
        周成交金额(万元)   
    s_risk_betar100: NUMBER(20,4)
        BETA(100周)   
    s_wq_varpctchange100: NUMBER(20,4)
        周收益率方差(100周)   
    s_wq_devpctchange100: NUMBER(20,4)
        周收益率标准差(100周)   
    s_wq_avgpctchange100: NUMBER(20,4)
        周收益率平均值(100周)   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    crncy_code = Column(VARCHAR2(10))
    s_wq_pctchange = Column(NUMBER(20,4))
    s_wq_turn = Column(NUMBER(20,4))
    s_wq_avgturn = Column(NUMBER(20,4))
    s_wq_amount = Column(NUMBER(20,4))
    s_risk_betar100 = Column(NUMBER(20,4))
    s_wq_varpctchange100 = Column(NUMBER(20,4))
    s_wq_devpctchange100 = Column(NUMBER(20,4))
    s_wq_avgpctchange100 = Column(NUMBER(20,4))
    
