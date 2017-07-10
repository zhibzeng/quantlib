from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareMonthlyYield(BaseModel):
    """
    中国A股月收益率

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
    s_mq_pctchange: NUMBER(20,4)
        月收益率   
    s_mq_turn: NUMBER(20,4)
        月换手率(合计)   
    s_mq_avgturn: NUMBER(20,4)
        月换手率(算术平均)   
    s_mq_amount: NUMBER(20,4)
        月成交金额(万元)   
    s_risk_betar24: NUMBER(20,4)
        BETA(24月)   
    s_risk_betar60: NUMBER(20,4)
        BETA(60月)   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    crncy_code = Column(VARCHAR2(10))
    s_mq_pctchange = Column(NUMBER(20,4))
    s_mq_turn = Column(NUMBER(20,4))
    s_mq_avgturn = Column(NUMBER(20,4))
    s_mq_amount = Column(NUMBER(20,4))
    s_risk_betar24 = Column(NUMBER(20,4))
    s_risk_betar60 = Column(NUMBER(20,4))
    
