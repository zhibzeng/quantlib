from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class UnlistedBrokerBalanceSheet(BaseModel):
    """
    非上市券商资产负债表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_compcode: VARCHAR2(40)
        公司代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    report_period: VARCHAR2(8)
        报告期   
    statement_type: VARCHAR2(10)
        报表类型   报表类型:408001000:合并报表408004000:合并报表(调整)408005000:合并报表(更正前)408050000:合并调整(更正前)408006000:母公司报表408009000:母公司报表(调整)408010000:母公司报表(更正前)408060000:母公司调整(更正前)
    crncy_code: VARCHAR2(10)
        货币代码   CNY
    actual_ann_dt: VARCHAR2(8)
        实际公告日期   
    monetary_cap: NUMBER(20,4)
        货币资金   
    clients_cap_deposit: NUMBER(20,4)
        客户资金存款   
    settle_rsrv: NUMBER(20,4)
        结算备付金   
    clients_rsrv_settle: NUMBER(20,4)
        客户备付金   
    loans_to_oth_banks: NUMBER(20,4)
        拆出资金   
    tradable_fin_assets: NUMBER(20,4)
        交易性金融资产   
    derivative_fin_assets: NUMBER(20,4)
        衍生金融资产   
    red_monetary_cap_for_sale: NUMBER(20,4)
        买入返售金融资产   
    int_rcv: NUMBER(20,4)
        应收利息   
    mrgn_paid: NUMBER(20,4)
        存出保证金   
    agency_bus_assets: NUMBER(20,4)
        代理业务资产   
    fin_assets_avail_for_sale: NUMBER(20,4)
        可供出售金融资产   
    held_to_mty_invest: NUMBER(20,4)
        持有至到期投资   
    long_term_eqy_invest: NUMBER(20,4)
        长期股权投资   
    fix_assets: NUMBER(20,4)
        固定资产   
    intang_assets: NUMBER(20,4)
        无形资产   

    """
    object_id = Column(VARCHAR2(100))
    s_info_compcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    actual_ann_dt = Column(VARCHAR2(8))
    monetary_cap = Column(NUMBER(20,4))
    clients_cap_deposit = Column(NUMBER(20,4))
    settle_rsrv = Column(NUMBER(20,4))
    clients_rsrv_settle = Column(NUMBER(20,4))
    loans_to_oth_banks = Column(NUMBER(20,4))
    tradable_fin_assets = Column(NUMBER(20,4))
    derivative_fin_assets = Column(NUMBER(20,4))
    red_monetary_cap_for_sale = Column(NUMBER(20,4))
    int_rcv = Column(NUMBER(20,4))
    mrgn_paid = Column(NUMBER(20,4))
    agency_bus_assets = Column(NUMBER(20,4))
    fin_assets_avail_for_sale = Column(NUMBER(20,4))
    held_to_mty_invest = Column(NUMBER(20,4))
    long_term_eqy_invest = Column(NUMBER(20,4))
    fix_assets = Column(NUMBER(20,4))
    intang_assets = Column(NUMBER(20,4))
    
