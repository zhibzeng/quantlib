from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareStrangeTrade(BaseModel):
    """
    中国A股证券交易异动营业部买卖信息

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_strange_bgdate: VARCHAR2(8)
        交易起始日   
    s_strange_enddate: VARCHAR2(8)
        交易截止日   
    s_strange_range: NUMBER(20,4)
        涨跌幅   
    s_strange_volume: NUMBER(20,4)
        总成交量(万股)   
    s_strange_amount: NUMBER(20,4)
        总成交金额   
    s_strange_tradername: VARCHAR2(200)
        营业部名称   
    s_strange_traderamount: NUMBER(20,4)
        营业部买卖金额   
    s_strange_buyamount: NUMBER(20,4)
        买入金额(元)   
    s_strange_sellamount: NUMBER(20,4)
        卖出金额(元)   

    """
    __tablename__ = "AShareStrangeTrade"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_strange_bgdate = Column(VARCHAR2(8))
    s_strange_enddate = Column(VARCHAR2(8))
    s_strange_range = Column(NUMBER(20,4))
    s_strange_volume = Column(NUMBER(20,4))
    s_strange_amount = Column(NUMBER(20,4))
    s_strange_tradername = Column(VARCHAR2(200))
    s_strange_traderamount = Column(NUMBER(20,4))
    s_strange_buyamount = Column(NUMBER(20,4))
    s_strange_sellamount = Column(NUMBER(20,4))
    
