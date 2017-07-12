from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondBalanceSheet(BaseModel):
    """
    中国债券发行主体资产负债表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_compcode: VARCHAR2(40)
        公司ID   
    ann_dt: VARCHAR2(8)
        公告日期   
    report_period: VARCHAR2(8)
        报告期   
    statement_type: VARCHAR2(10)
        报表类型   报表类型:408001000:合并报表408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408009000:母公司报表(调整)408010000:母公司报表(更正前)
    crncy_code: VARCHAR2(10)
        货币代码   CNY
    monetary_cap: NUMBER(20,4)
        货币资金   
    tradable_fin_assets: NUMBER(20,4)
        交易性金融资产   
    notes_rcv: NUMBER(20,4)
        应收票据   
    acct_rcv: NUMBER(20,4)
        应收账款   
    oth_rcv: NUMBER(20,4)
        其他应收款   
    prepay: NUMBER(20,4)
        预付款项   
    dvd_rcv: NUMBER(20,4)
        应收股利   
    int_rcv: NUMBER(20,4)
        应收利息   
    inventories: NUMBER(20,4)
        存货   
    consumptive_bio_assets: NUMBER(20,4)
        消耗性生物资产   
    deferred_exp: NUMBER(20,4)
        待摊费用   
    non_cur_assets_due_within_1y: NUMBER(20,4)
        一年内到期的非流动资产   
    settle_rsrv: NUMBER(20,4)
        结算备付金   
    loans_to_oth_banks: NUMBER(20,4)
        拆出资金   
    prem_rcv: NUMBER(20,4)
        应收保费   
    rcv_from_reinsurer: NUMBER(20,4)
        应收分保账款   
    rcv_from_ceded_insur_cont_rsrv: NUMBER(20,4)
        应收分保合同准备金   
    red_monetary_cap_for_sale: NUMBER(20,4)
        买入返售金融资产   
    oth_cur_assets: NUMBER(20,4)
        其他流动资产   
    tot_cur_assets: NUMBER(20,4)
        流动资产合计   
    fin_assets_avail_for_sale: NUMBER(20,4)
        可供出售金融资产   
    held_to_mty_invest: NUMBER(20,4)
        持有至到期投资   
    long_term_eqy_invest: NUMBER(20,4)
        长期股权投资   
    invest_real_estate: NUMBER(20,4)
        投资性房地产   
    time_deposits: NUMBER(20,4)
        定期存款   
    oth_assets: NUMBER(20,4)
        其他资产   
    long_term_rec: NUMBER(20,4)
        长期应收款   
    fix_assets: NUMBER(20,4)
        固定资产   
    const_in_prog: NUMBER(20,4)
        在建工程   
    proj_matl: NUMBER(20,4)
        工程物资   
    fix_assets_disp: NUMBER(20,4)
        固定资产清理   
    productive_bio_assets: NUMBER(20,4)
        生产性生物资产   
    oil_and_natural_gas_assets: NUMBER(20,4)
        油气资产   
    intang_assets: NUMBER(20,4)
        无形资产   
    r_and_d_costs: NUMBER(20,4)
        开发支出   
    goodwill: NUMBER(20,4)
        商誉   
    long_term_deferred_exp: NUMBER(20,4)
        长期待摊费用   
    deferred_tax_assets: NUMBER(20,4)
        递延所得税资产   
    loans_and_adv_granted: NUMBER(20,4)
        发放贷款及垫款   
    oth_non_cur_assets: NUMBER(20,4)
        其他非流动资产   
    tot_non_cur_assets: NUMBER(20,4)
        非流动资产合计   
    cash_deposits_central_bank: NUMBER(20,4)
        现金及存放中央银行款项   
    asset_dep_oth_banks_fin_inst: NUMBER(20,4)
        存放同业和其它金融机构款项   
    precious_metals: NUMBER(20,4)
        贵金属   
    derivative_fin_assets: NUMBER(20,4)
        衍生金融资产   
    agency_bus_assets: NUMBER(20,4)
        代理业务资产   
    subr_rec: NUMBER(20,4)
        应收代位追偿款   
    rcv_ceded_unearned_prem_rsrv: NUMBER(20,4)
        应收分保未到期责任准备金   
    rcv_ceded_claim_rsrv: NUMBER(20,4)
        应收分保未决赔款准备金   
    rcv_ceded_life_insur_rsrv: NUMBER(20,4)
        应收分保寿险责任准备金   
    rcv_ceded_lt_health_insur_rsrv: NUMBER(20,4)
        应收分保长期健康险   

    """
    __tablename__ = "CBondBalanceSheet"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_compcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    monetary_cap = Column(NUMBER(20,4))
    tradable_fin_assets = Column(NUMBER(20,4))
    notes_rcv = Column(NUMBER(20,4))
    acct_rcv = Column(NUMBER(20,4))
    oth_rcv = Column(NUMBER(20,4))
    prepay = Column(NUMBER(20,4))
    dvd_rcv = Column(NUMBER(20,4))
    int_rcv = Column(NUMBER(20,4))
    inventories = Column(NUMBER(20,4))
    consumptive_bio_assets = Column(NUMBER(20,4))
    deferred_exp = Column(NUMBER(20,4))
    non_cur_assets_due_within_1y = Column(NUMBER(20,4))
    settle_rsrv = Column(NUMBER(20,4))
    loans_to_oth_banks = Column(NUMBER(20,4))
    prem_rcv = Column(NUMBER(20,4))
    rcv_from_reinsurer = Column(NUMBER(20,4))
    rcv_from_ceded_insur_cont_rsrv = Column(NUMBER(20,4))
    red_monetary_cap_for_sale = Column(NUMBER(20,4))
    oth_cur_assets = Column(NUMBER(20,4))
    tot_cur_assets = Column(NUMBER(20,4))
    fin_assets_avail_for_sale = Column(NUMBER(20,4))
    held_to_mty_invest = Column(NUMBER(20,4))
    long_term_eqy_invest = Column(NUMBER(20,4))
    invest_real_estate = Column(NUMBER(20,4))
    time_deposits = Column(NUMBER(20,4))
    oth_assets = Column(NUMBER(20,4))
    long_term_rec = Column(NUMBER(20,4))
    fix_assets = Column(NUMBER(20,4))
    const_in_prog = Column(NUMBER(20,4))
    proj_matl = Column(NUMBER(20,4))
    fix_assets_disp = Column(NUMBER(20,4))
    productive_bio_assets = Column(NUMBER(20,4))
    oil_and_natural_gas_assets = Column(NUMBER(20,4))
    intang_assets = Column(NUMBER(20,4))
    r_and_d_costs = Column(NUMBER(20,4))
    goodwill = Column(NUMBER(20,4))
    long_term_deferred_exp = Column(NUMBER(20,4))
    deferred_tax_assets = Column(NUMBER(20,4))
    loans_and_adv_granted = Column(NUMBER(20,4))
    oth_non_cur_assets = Column(NUMBER(20,4))
    tot_non_cur_assets = Column(NUMBER(20,4))
    cash_deposits_central_bank = Column(NUMBER(20,4))
    asset_dep_oth_banks_fin_inst = Column(NUMBER(20,4))
    precious_metals = Column(NUMBER(20,4))
    derivative_fin_assets = Column(NUMBER(20,4))
    agency_bus_assets = Column(NUMBER(20,4))
    subr_rec = Column(NUMBER(20,4))
    rcv_ceded_unearned_prem_rsrv = Column(NUMBER(20,4))
    rcv_ceded_claim_rsrv = Column(NUMBER(20,4))
    rcv_ceded_life_insur_rsrv = Column(NUMBER(20,4))
    rcv_ceded_lt_health_insur_rsrv = Column(NUMBER(20,4))
    
