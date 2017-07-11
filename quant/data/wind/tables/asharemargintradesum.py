from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareMarginTradeSum(BaseModel):
    """
    中国A股融资融券交易汇总

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    trade_dt: VARCHAR2(8)
        日期   
    s_marsum_exchmarket: VARCHAR2(40)
        交易所英文简称   
    s_marsum_tradingbalance: NUMBER(20,4)
        融资余额(元)   上海：本日融资余额;深圳：融资余额;前日融资余额＋本日融资买入额－本日融资偿还额
    s_marsum_purchwithborrowmoney: NUMBER(20,4)
        融资买入额(元)   上海：本日融资买入额;深圳：融资买入额
    s_marsum_repaymenttobroker: NUMBER(20,4)
        融资偿还额(元)   上海：本日融资偿还额;深圳：未公布;本日直接还款额＋本日卖券还款额＋本日融资强制平仓额＋本日融资正权益调整－本日融资负权益调整
    s_marsum_seclendingbalance: NUMBER(20,4)
        融券余额(元)   上海：本日融券余量金额;深圳：融券余额
    s_marsum_salesofborrowedsec: NUMBER(20,4)
        融券卖出量(股,份,手)   上海：未公布;深圳：融券卖出量
    s_marsum_margintradebalance: NUMBER(20,4)
        融资融券余额(股,份,手)   上海：本日融资融券交易总量;深圳：融资融券余额;融资余额＋融券余额

    """
    object_id = Column(VARCHAR2(100))
    trade_dt = Column(VARCHAR2(8))
    s_marsum_exchmarket = Column(VARCHAR2(40))
    s_marsum_tradingbalance = Column(NUMBER(20,4))
    s_marsum_purchwithborrowmoney = Column(NUMBER(20,4))
    s_marsum_repaymenttobroker = Column(NUMBER(20,4))
    s_marsum_seclendingbalance = Column(NUMBER(20,4))
    s_marsum_salesofborrowedsec = Column(NUMBER(20,4))
    s_marsum_margintradebalance = Column(NUMBER(20,4))
    
