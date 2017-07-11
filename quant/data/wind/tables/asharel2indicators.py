from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


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
    s_li_largebuymoney: NUMBER(20,4)
        大买总额   大单买入的总成交额
    s_li_largebuyamount: NUMBER(20,4)
        大买总量   大单买入的总成交量
    s_li_largesellrate: NUMBER(20,4)
        大卖比率   大单卖出成交金额占总成交金额的比例
    s_li_largesellmoney: NUMBER(20,4)
        大卖总额   大单卖出的总成交额
    s_li_largesellamount: NUMBER(20,4)
        大卖总量   大单卖出的总成交量
    s_li_entrustrate: NUMBER(20,4)
        总委比   (总委买量-总委卖量)/总委买量+总委卖量)*100%
    s_li_entrudifferamount: NUMBER(20,4)
        总委差量   总委买量-总委卖量
    s_li_entrudifferamoney: NUMBER(20,4)
        总委差额   总委买金额-总委卖金额
    s_li_entrustbuymoney: NUMBER(20,4)
        总委买额   从买一到跌停位置的总委买金额=总委买量*委买均价

    """
    __tablename__ = "AShareL2Indicators"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(NUMBER(8))
    s_li_initiativebuyrate = Column(NUMBER(20,4))
    s_li_initiativebuymoney = Column(NUMBER(20,4))
    s_li_initiativebuyamount = Column(NUMBER(20,4))
    s_li_initiativesellrate = Column(NUMBER(20,4))
    s_li_initiativesellmoney = Column(NUMBER(20,4))
    s_li_initiativesellamount = Column(NUMBER(20,4))
    s_li_largebuyrate = Column(NUMBER(20,4))
    s_li_largebuymoney = Column(NUMBER(20,4))
    s_li_largebuyamount = Column(NUMBER(20,4))
    s_li_largesellrate = Column(NUMBER(20,4))
    s_li_largesellmoney = Column(NUMBER(20,4))
    s_li_largesellamount = Column(NUMBER(20,4))
    s_li_entrustrate = Column(NUMBER(20,4))
    s_li_entrudifferamount = Column(NUMBER(20,4))
    s_li_entrudifferamoney = Column(NUMBER(20,4))
    s_li_entrustbuymoney = Column(NUMBER(20,4))
    
