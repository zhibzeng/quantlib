from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareInsiderTrade(BaseModel):
    """
    中国A股内部人交易

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   数据来源：交易所网站
    related_manager_name: VARCHAR2(100)
        相关管理层姓名   与交易者相关的管理层姓名
    reported_trader_name: VARCHAR2(100)
        变动人姓名   进行交易的交易者姓名, 不一定是管理人本人
    change_volume: NUMBER(20,4)
        变动数   
    trade_avg_price: NUMBER(20,4)
        成交均价   
    position_after_trade: NUMBER(20,4)
        变动后持股   
    trade_dt: VARCHAR2(8)
        变动日期   
    ann_dt: VARCHAR2(8)
        填报日期   
    trade_reason_code: NUMBER(9,0)
        变动原因类型代码   对应:类型编码表中的原始类型代码
    related_manager_post: VARCHAR2(80)
        相关管理层职务   
    trader_manager_relation: VARCHAR2(20)
        变动人与管理层的关系   
    actual_ann_dt: VARCHAR2(8)
        实际公告日期   

    """
    __tablename__ = "AShareInsiderTrade"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    related_manager_name = Column(VARCHAR2(100))
    reported_trader_name = Column(VARCHAR2(100))
    change_volume = Column(NUMBER(20,4))
    trade_avg_price = Column(NUMBER(20,4))
    position_after_trade = Column(NUMBER(20,4))
    trade_dt = Column(VARCHAR2(8))
    ann_dt = Column(VARCHAR2(8))
    trade_reason_code = Column(NUMBER(9,0))
    related_manager_post = Column(VARCHAR2(80))
    trader_manager_relation = Column(VARCHAR2(20))
    actual_ann_dt = Column(VARCHAR2(8))
    
