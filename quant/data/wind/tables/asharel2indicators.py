from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareL2Indicators(BaseModel):
    """
    中国A股Level2指标

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: NUMBER(8)
        交易日期   
    s_li_initiativebuyrate: NUMBER(20,4)
        主买比率   主动性买入成交金额占总成交金额的比例
    s_li_initiativebuymoney: NUMBER(20,4)
        主买总额   主动买入的总成交金额注：金额=成交价格*成交量(深市)
    s_li_initiativebuyamount: NUMBER(20,4)
        主买总量   主动买入的总成交量
    s_li_initiativesellrate: NUMBER(20,4)
        主卖比率   主动性卖出成交金额占总成交金额的比例
    s_li_initiativesellmoney: NUMBER(20,4)
        主卖总额   主动卖出的总成交额
    s_li_initiativesellamount: NUMBER(20,4)
        主卖总量   主动卖出的总成交量
    s_li_largebuyrate: NUMBER(20,4)
        大买比率   大单买入成交金额占总成交金额的比例注：所谓大单=机构单+大户单(沪市)

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(NUMBER(8))
    s_li_initiativebuyrate = Column(NUMBER(20,4))
    s_li_initiativebuymoney = Column(NUMBER(20,4))
    s_li_initiativebuyamount = Column(NUMBER(20,4))
    s_li_initiativesellrate = Column(NUMBER(20,4))
    s_li_initiativesellmoney = Column(NUMBER(20,4))
    s_li_initiativesellamount = Column(NUMBER(20,4))
    s_li_largebuyrate = Column(NUMBER(20,4))
    
