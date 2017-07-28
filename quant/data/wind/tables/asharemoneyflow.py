from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareMoneyflow(BaseModel):
    """
    4.40 中国A股资金流向数据

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
        中户量差(含主动被动)   中单买量-中单卖量(手)
    volume_diff_med_trader_act: NUMBER(20,4)
        中户量差(仅主动)   中单主动买量-中单主动卖量(手)
    volume_diff_large_trader: NUMBER(20,4)
        大户量差(含主动被动)   大单买量-大单卖量(手)
    volume_diff_large_trader_act: NUMBER(20,4)
        大户量差(仅主动)   大单主动买量-大单主动买量(手)
    volume_diff_institute: NUMBER(20,4)
        机构量差(含主动被动)   特大单买量-特大单卖量(手)
    volume_diff_institute_act: NUMBER(20,4)
        机构量差(仅主动)   特大单主动买量-特大单主动买量(手)
    value_diff_small_trader: NUMBER(20,4)
        散户金额差(含主动被动)   小单买额-小单卖额
    value_diff_small_trader_act: NUMBER(20,4)
        散户金额差(仅主动)   小单主动买额-小单主动卖额
    value_diff_med_trader: NUMBER(20,4)
        中户金额差(含主动被动)   中单买额-中单卖额
    value_diff_med_trader_act: NUMBER(20,4)
        中户金额差(仅主动)   中单主动买额-中单主动卖额
    value_diff_large_trader: NUMBER(20,4)
        大户金额差(含主动被动)   大单买额-大单卖额
    value_diff_large_trader_act: NUMBER(20,4)
        大户金额差(仅主动)   大单主动买额-大单主动买额
    value_diff_institute: NUMBER(20,4)
        机构金额差(含主动被动)   特大单买额-特大单卖额
    value_diff_institute_act: NUMBER(20,4)
        机构金额差(仅主动)   特大单主动买额-特大单主动卖额
    s_mfd_inflowvolume: NUMBER(20,4)
        净流入量   当日净流入量(手)
    net_inflow_rate_volume: NUMBER(20,4)
        流入率(量)   当日净流入量/成交股数(手/手)
    s_mfd_inflow_openvolume: NUMBER(20,4)
        开盘资金流入量   10点前的资金净流入量(手)
    open_net_inflow_rate_volume: NUMBER(20,4)
        开盘资金流入率(量)   10点前的资金净流入量/成交股数(手/手)
    s_mfd_inflow_closevolume: NUMBER(20,4)
        尾盘资金流入量   14：30后的资金净流入量(手)
    close_net_inflow_rate_volume: NUMBER(20,4)
        尾盘资金流入率(量)   14：30后的资金净流入量/成交股数(手/手)
    s_mfd_inflow: NUMBER(20,4)
        净流入金额   当日净流入资金额
    net_inflow_rate_value: NUMBER(20,4)
        流入率(金额)   当日净流入/成交额(万元/万元)
    s_mfd_inflow_open: NUMBER(20,4)
        开盘资金流入金额   10点前的资金净流入金额
    open_net_inflow_rate_value: NUMBER(20,4)
        开盘资金流入率(金额)   10点前的资金净流入金额/成交额(万元/万元)
    s_mfd_inflow_close: NUMBER(20,4)
        尾盘资金流入金额   14：30后的资金净流入金额
    close_net_inflow_rate_value: NUMBER(20,4)
        尾盘资金流入率(金额)   14：30后的资金净流入金额/成交额(万元/万元)
    tot_volume_bid: NUMBER(20,4)
        委买总量   当日委买总量
    tot_volume_ask: NUMBER(20,4)
        委卖总量   当日委卖总量
    moneyflow_pct_volume: NUMBER(20,4)
        资金流向占比(量)   当日资金净流入量/流通盘股数(手/万股)
    open_moneyflow_pct_volume: NUMBER(20,4)
        开盘资金流向占比(量)   10点前的资金净流向占比(手/万股)
    close_moneyflow_pct_volume: NUMBER(20,4)
        尾盘资金流向占比(量)   14：30后的资金流向占比(手/万股)
    moneyflow_pct_value: NUMBER(20,4)
        资金流向占比(金额)   当日资金净流入金额/流通市值(万元/(元*万股))
    open_moneyflow_pct_value: NUMBER(20,4)
        开盘资金流向占比(金额)   10点前的资金净流向占比(金额比)(万元/(元*万股))
    close_moneyflow_pct_value: NUMBER(20,4)
        尾盘资金流向占比(金额)   14：30后的资金流向占比(金额比)(万元/(元*万股))
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

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
    volume_diff_med_trader_act = Column(NUMBER(20,4))
    volume_diff_large_trader = Column(NUMBER(20,4))
    volume_diff_large_trader_act = Column(NUMBER(20,4))
    volume_diff_institute = Column(NUMBER(20,4))
    volume_diff_institute_act = Column(NUMBER(20,4))
    value_diff_small_trader = Column(NUMBER(20,4))
    value_diff_small_trader_act = Column(NUMBER(20,4))
    value_diff_med_trader = Column(NUMBER(20,4))
    value_diff_med_trader_act = Column(NUMBER(20,4))
    value_diff_large_trader = Column(NUMBER(20,4))
    value_diff_large_trader_act = Column(NUMBER(20,4))
    value_diff_institute = Column(NUMBER(20,4))
    value_diff_institute_act = Column(NUMBER(20,4))
    s_mfd_inflowvolume = Column(NUMBER(20,4))
    net_inflow_rate_volume = Column(NUMBER(20,4))
    s_mfd_inflow_openvolume = Column(NUMBER(20,4))
    open_net_inflow_rate_volume = Column(NUMBER(20,4))
    s_mfd_inflow_closevolume = Column(NUMBER(20,4))
    close_net_inflow_rate_volume = Column(NUMBER(20,4))
    s_mfd_inflow = Column(NUMBER(20,4))
    net_inflow_rate_value = Column(NUMBER(20,4))
    s_mfd_inflow_open = Column(NUMBER(20,4))
    open_net_inflow_rate_value = Column(NUMBER(20,4))
    s_mfd_inflow_close = Column(NUMBER(20,4))
    close_net_inflow_rate_value = Column(NUMBER(20,4))
    tot_volume_bid = Column(NUMBER(20,4))
    tot_volume_ask = Column(NUMBER(20,4))
    moneyflow_pct_volume = Column(NUMBER(20,4))
    open_moneyflow_pct_volume = Column(NUMBER(20,4))
    close_moneyflow_pct_volume = Column(NUMBER(20,4))
    moneyflow_pct_value = Column(NUMBER(20,4))
    open_moneyflow_pct_value = Column(NUMBER(20,4))
    close_moneyflow_pct_value = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
