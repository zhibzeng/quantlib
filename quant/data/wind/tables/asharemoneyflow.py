from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareMoneyflow(BaseModel):
    """
    中国A股资金流向数据

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        日期   
    buy_value_exlarge_order: NUMBER(20,4)
        机构买入金额   当日机构买入金额
    sell_value_exlarge_order: NUMBER(20,4)
        机构卖出金额   当日机构卖出金额
    buy_value_large_order: NUMBER(20,4)
        大户买入金额   当日大户买入金额
    sell_value_large_order: NUMBER(20,4)
        大户卖出金额   当日大户卖出金额
    buy_value_med_order: NUMBER(20,4)
        中户买入金额   当日中户买入金额
    sell_value_med_order: NUMBER(20,4)
        中户卖出金额   当日中户卖出金额
    buy_value_small_order: NUMBER(20,4)
        散户买入金额   当日散户买入金额
    sell_value_small_order: NUMBER(20,4)
        散户卖出金额   当日散户卖出金额
    buy_volume_exlarge_order: NUMBER(20,4)
        机构买入总量   当日机构买入总手数
    sell_volume_exlarge_order: NUMBER(20,4)
        机构卖出总量   当日机构卖出总手数
    buy_volume_large_order: NUMBER(20,4)
        大户买入总量   当日大户买入总手数
    sell_volume_large_order: NUMBER(20,4)
        大户卖出总量   当日大户卖出总手数
    buy_volume_med_order: NUMBER(20,4)
        中户买入总量   当日中户买入总手数
    sell_volume_med_order: NUMBER(20,4)
        中户卖出总量   当日中户卖出总手数
    buy_volume_small_order: NUMBER(20,4)
        散户买入总量   当日散户买入总手数
    sell_volume_small_order: NUMBER(20,4)
        散户卖出总量   当日散户卖出总手数
    trades_count: NUMBER(20,4)
        成交笔数   当日个股成交总笔数
    buy_trades_exlarge_order: NUMBER(20,4)
        机构买入单数   当日买入特大单的单数
    sell_trades_exlarge_order: NUMBER(20,4)
        机构卖出单数   当日卖出特大单的单数
    buy_trades_large_order: NUMBER(20,4)
        大户买入单数   当日买入大单的单数
    sell_trades_large_order: NUMBER(20,4)
        大户卖出单数   当日卖出大单的单数
    buy_trades_med_order: NUMBER(20,4)
        中户买入单数   当日买入中单的单数
    sell_trades_med_order: NUMBER(20,4)
        中户卖出单数   当日卖出中单的单数
    buy_trades_small_order: NUMBER(20,4)
        散户买入单数   当日买入小单的单数
    sell_trades_small_order: NUMBER(20,4)
        散户卖出单数   当日卖出小单的单数
    volume_diff_small_trader: NUMBER(20,4)
        散户量差(含主动被动)   小单买量-小单卖量(手)
    volume_diff_small_trader_act: NUMBER(20,4)
        散户量差(仅主动)   小单主动买量-小单主动卖量(手)
    volume_diff_med_trader: NUMBER(20,4)
        中户量差(含主动被   中单买量-中单卖量(手)

    """
    __tablename__ = "AShareMoneyflow"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    buy_value_exlarge_order = Column(NUMBER(20,4))
    sell_value_exlarge_order = Column(NUMBER(20,4))
    buy_value_large_order = Column(NUMBER(20,4))
    sell_value_large_order = Column(NUMBER(20,4))
    buy_value_med_order = Column(NUMBER(20,4))
    sell_value_med_order = Column(NUMBER(20,4))
    buy_value_small_order = Column(NUMBER(20,4))
    sell_value_small_order = Column(NUMBER(20,4))
    buy_volume_exlarge_order = Column(NUMBER(20,4))
    sell_volume_exlarge_order = Column(NUMBER(20,4))
    buy_volume_large_order = Column(NUMBER(20,4))
    sell_volume_large_order = Column(NUMBER(20,4))
    buy_volume_med_order = Column(NUMBER(20,4))
    sell_volume_med_order = Column(NUMBER(20,4))
    buy_volume_small_order = Column(NUMBER(20,4))
    sell_volume_small_order = Column(NUMBER(20,4))
    trades_count = Column(NUMBER(20,4))
    buy_trades_exlarge_order = Column(NUMBER(20,4))
    sell_trades_exlarge_order = Column(NUMBER(20,4))
    buy_trades_large_order = Column(NUMBER(20,4))
    sell_trades_large_order = Column(NUMBER(20,4))
    buy_trades_med_order = Column(NUMBER(20,4))
    sell_trades_med_order = Column(NUMBER(20,4))
    buy_trades_small_order = Column(NUMBER(20,4))
    sell_trades_small_order = Column(NUMBER(20,4))
    volume_diff_small_trader = Column(NUMBER(20,4))
    volume_diff_small_trader_act = Column(NUMBER(20,4))
    volume_diff_med_trader = Column(NUMBER(20,4))
    
