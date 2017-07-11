from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareProfitExpress(BaseModel):
    """
    中国A股业绩快报

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    report_period: VARCHAR2(8)
        报告期   
    oper_rev: NUMBER(20,4)
        营业收入(元)   
    oper_profit: NUMBER(20,4)
        营业利润(元)   
    tot_profit: NUMBER(20,4)
        利润总额(元)   
    net_profit_excl_min_int_inc: NUMBER(20,4)
        净利润(元)   
    tot_assets: NUMBER(20,4)
        总资产(元)   
    tot_shrhldr_eqy_excl_min_int: NUMBER(20,4)
        股东权益合计(不含少数股东权益)(元)   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    oper_rev = Column(NUMBER(20,4))
    oper_profit = Column(NUMBER(20,4))
    tot_profit = Column(NUMBER(20,4))
    net_profit_excl_min_int_inc = Column(NUMBER(20,4))
    tot_assets = Column(NUMBER(20,4))
    tot_shrhldr_eqy_excl_min_int = Column(NUMBER(20,4))
    
