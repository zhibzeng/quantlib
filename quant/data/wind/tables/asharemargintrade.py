from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareMarginTrade(BaseModel):
    """
    中国A股融资融券交易明细

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        日期   
    s_margin_tradingbalance: NUMBER(20,4)
        融资余额(元)   
    s_margin_purchwithborrowmoney: NUMBER(20,4)
        融资买入额(元,股)   
    s_margin_repaymenttobroker: NUMBER(20,4)
        融资偿还额(元,股)   
    s_margin_seclendingbalance: NUMBER(20,4)
        融券余额(元)   
    s_margin_seclendingbalancevol: NUMBER(20,4)
        融券余量   股(标的证券为股票)

    """
    __tablename__ = "AShareMarginTrade"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    s_margin_tradingbalance = Column(NUMBER(20,4))
    s_margin_purchwithborrowmoney = Column(NUMBER(20,4))
    s_margin_repaymenttobroker = Column(NUMBER(20,4))
    s_margin_seclendingbalance = Column(NUMBER(20,4))
    s_margin_seclendingbalancevol = Column(NUMBER(20,4))
    
