from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CCommodityFuturesEODPrices(BaseModel):
    """
    中国商品期货日行情

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    s_dq_presettle: NUMBER(20,4)
        前结算价(元)   
    s_dq_open: NUMBER(20,4)
        开盘价(元)   
    s_dq_high: NUMBER(20,4)
        最高价(元)   
    s_dq_low: NUMBER(20,4)
        最低价(元)   
    s_dq_close: NUMBER(20,4)
        收盘价(元)   
    s_dq_settle: NUMBER(20,4)
        结算价(元)   
    s_dq_volume: NUMBER(20,4)
        成交量(手)   
    s_dq_amount: NUMBER(20,4)
        成交金额(万元)   
    s_dq_oi: NUMBER(20,4)
        持仓量(手)   
    s_dq_change: NUMBER(20,4)
        涨跌(元)   收盘价-前结算价
    s_dq_oichange: NUMBER(20,4)
        持仓量变化   
    fs_info_type: VARCHAR2(10)
        合约类型   1:主力合约2:真实合约3:连续合约

    """
    __tablename__ = "CCommodityFuturesEODPrices"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    s_dq_presettle = Column(NUMBER(20,4))
    s_dq_open = Column(NUMBER(20,4))
    s_dq_high = Column(NUMBER(20,4))
    s_dq_low = Column(NUMBER(20,4))
    s_dq_close = Column(NUMBER(20,4))
    s_dq_settle = Column(NUMBER(20,4))
    s_dq_volume = Column(NUMBER(20,4))
    s_dq_amount = Column(NUMBER(20,4))
    s_dq_oi = Column(NUMBER(20,4))
    s_dq_change = Column(NUMBER(20,4))
    s_dq_oichange = Column(NUMBER(20,4))
    fs_info_type = Column(VARCHAR2(10))
    
