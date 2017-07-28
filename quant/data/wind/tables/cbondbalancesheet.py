from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondBalanceSheet(BaseModel):
    """
    4.158 中国债券发行主体资产负债表

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
        应收分保长期健康险责任准备金   
    mrgn_paid: NUMBER(20,4)
        存出保证金   
    insured_pledge_loan: NUMBER(20,4)
        保户质押贷款   
    cap_mrgn_paid: NUMBER(20,4)
        存出资本保证金   
    independent_acct_assets: NUMBER(20,4)
        独立账户资产   
    clients_cap_deposit: NUMBER(20,4)
        客户资金存款   
    clients_rsrv_settle: NUMBER(20,4)
        客户备付金   
    incl_seat_fees_exchange: NUMBER(20,4)
        其中:交易席位费   
    rcv_invest: NUMBER(20,4)
        应收款项类投资   
    tot_assets: NUMBER(20,4)
        资产总计   
    st_borrow: NUMBER(20,4)
        短期借款   
    borrow_central_bank: NUMBER(20,4)
        向中央银行借款   
    deposit_received_ib_deposits: NUMBER(20,4)
        吸收存款及同业存放   
    loans_oth_banks: NUMBER(20,4)
        拆入资金   
    tradable_fin_liab: NUMBER(20,4)
        交易性金融负债   
    notes_payable: NUMBER(20,4)
        应付票据   
    acct_payable: NUMBER(20,4)
        应付账款   
    adv_from_cust: NUMBER(20,4)
        预收款项   
    fund_sales_fin_assets_rp: NUMBER(20,4)
        卖出回购金融资产款   
    handling_charges_comm_payable: NUMBER(20,4)
        应付手续费及佣金   
    empl_ben_payable: NUMBER(20,4)
        应付职工薪酬   
    taxes_surcharges_payable: NUMBER(20,4)
        应交税费   
    int_payable: NUMBER(20,4)
        应付利息   
    dvd_payable: NUMBER(20,4)
        应付股利   
    oth_payable: NUMBER(20,4)
        其他应付款   
    acc_exp: NUMBER(20,4)
        预提费用   
    deferred_inc: NUMBER(20,4)
        递延收益   
    st_bonds_payable: NUMBER(20,4)
        应付短期债券   
    payable_to_reinsurer: NUMBER(20,4)
        应付分保账款   
    rsrv_insur_cont: NUMBER(20,4)
        保险合同准备金   
    acting_trading_sec: NUMBER(20,4)
        代理买卖证券款   
    acting_uw_sec: NUMBER(20,4)
        代理承销证券款   
    non_cur_liab_due_within_1y: NUMBER(20,4)
        一年内到期的非流动负债   
    oth_cur_liab: NUMBER(20,4)
        其他流动负债   
    tot_cur_liab: NUMBER(20,4)
        流动负债合计   
    lt_borrow: NUMBER(20,4)
        长期借款   
    bonds_payable: NUMBER(20,4)
        应付债券   
    lt_payable: NUMBER(20,4)
        长期应付款   
    specific_item_payable: NUMBER(20,4)
        专项应付款   
    provisions: NUMBER(20,4)
        预计负债   
    deferred_tax_liab: NUMBER(20,4)
        递延所得税负债   
    deferred_inc_non_cur_liab: NUMBER(20,4)
        递延收益-非流动负债   
    oth_non_cur_liab: NUMBER(20,4)
        其他非流动负债   
    tot_non_cur_liab: NUMBER(20,4)
        非流动负债合计   
    liab_dep_oth_banks_fin_inst: NUMBER(20,4)
        同业和其它金融机构存放款项   
    derivative_fin_liab: NUMBER(20,4)
        衍生金融负债   
    cust_bank_dep: NUMBER(20,4)
        吸收存款   
    agency_bus_liab: NUMBER(20,4)
        代理业务负债   
    oth_liab: NUMBER(20,4)
        其他负债   
    prem_received_adv: NUMBER(20,4)
        预收保费   
    deposit_received: NUMBER(20,4)
        存入保证金   
    insured_deposit_invest: NUMBER(20,4)
        保户储金及投资款   
    unearned_prem_rsrv: NUMBER(20,4)
        未到期责任准备金   
    out_loss_rsrv: NUMBER(20,4)
        未决赔款准备金   
    life_insur_rsrv: NUMBER(20,4)
        寿险责任准备金   
    lt_health_insur_v: NUMBER(20,4)
        长期健康险责任准备金   
    independent_acct_liab: NUMBER(20,4)
        独立账户负债   
    incl_pledge_loan: NUMBER(20,4)
        其中:质押借款   
    claims_payable: NUMBER(20,4)
        应付赔付款   
    dvd_payable_insured: NUMBER(20,4)
        应付保单红利   
    tot_liab: NUMBER(20,4)
        负债合计   
    cap_stk: NUMBER(20,4)
        股本   
    cap_rsrv: NUMBER(20,4)
        资本公积金   
    special_rsrv: NUMBER(20,4)
        专项储备   
    surplus_rsrv: NUMBER(20,4)
        盈余公积金   
    undistributed_profit: NUMBER(20,4)
        未分配利润   
    less_tsy_stk: NUMBER(20,4)
        减:库存股   
    prov_nom_risks: NUMBER(20,4)
        一般风险准备   
    cnvd_diff_foreign_curr_stat: NUMBER(20,4)
        外币报表折算差额   
    unconfirmed_invest_loss: NUMBER(20,4)
        未确认的投资损失   
    minority_int: NUMBER(20,4)
        少数股东权益   
    tot_shrhldr_eqy_excl_min_int: NUMBER(20,4)
        股东权益合计(不含少数股东权益)   
    tot_shrhldr_eqy_incl_min_int: NUMBER(20,4)
        股东权益合计(含少数股东权益)   
    tot_liab_shrhldr_eqy: NUMBER(20,4)
        负债及股东权益总计   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

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
    mrgn_paid = Column(NUMBER(20,4))
    insured_pledge_loan = Column(NUMBER(20,4))
    cap_mrgn_paid = Column(NUMBER(20,4))
    independent_acct_assets = Column(NUMBER(20,4))
    clients_cap_deposit = Column(NUMBER(20,4))
    clients_rsrv_settle = Column(NUMBER(20,4))
    incl_seat_fees_exchange = Column(NUMBER(20,4))
    rcv_invest = Column(NUMBER(20,4))
    tot_assets = Column(NUMBER(20,4))
    st_borrow = Column(NUMBER(20,4))
    borrow_central_bank = Column(NUMBER(20,4))
    deposit_received_ib_deposits = Column(NUMBER(20,4))
    loans_oth_banks = Column(NUMBER(20,4))
    tradable_fin_liab = Column(NUMBER(20,4))
    notes_payable = Column(NUMBER(20,4))
    acct_payable = Column(NUMBER(20,4))
    adv_from_cust = Column(NUMBER(20,4))
    fund_sales_fin_assets_rp = Column(NUMBER(20,4))
    handling_charges_comm_payable = Column(NUMBER(20,4))
    empl_ben_payable = Column(NUMBER(20,4))
    taxes_surcharges_payable = Column(NUMBER(20,4))
    int_payable = Column(NUMBER(20,4))
    dvd_payable = Column(NUMBER(20,4))
    oth_payable = Column(NUMBER(20,4))
    acc_exp = Column(NUMBER(20,4))
    deferred_inc = Column(NUMBER(20,4))
    st_bonds_payable = Column(NUMBER(20,4))
    payable_to_reinsurer = Column(NUMBER(20,4))
    rsrv_insur_cont = Column(NUMBER(20,4))
    acting_trading_sec = Column(NUMBER(20,4))
    acting_uw_sec = Column(NUMBER(20,4))
    non_cur_liab_due_within_1y = Column(NUMBER(20,4))
    oth_cur_liab = Column(NUMBER(20,4))
    tot_cur_liab = Column(NUMBER(20,4))
    lt_borrow = Column(NUMBER(20,4))
    bonds_payable = Column(NUMBER(20,4))
    lt_payable = Column(NUMBER(20,4))
    specific_item_payable = Column(NUMBER(20,4))
    provisions = Column(NUMBER(20,4))
    deferred_tax_liab = Column(NUMBER(20,4))
    deferred_inc_non_cur_liab = Column(NUMBER(20,4))
    oth_non_cur_liab = Column(NUMBER(20,4))
    tot_non_cur_liab = Column(NUMBER(20,4))
    liab_dep_oth_banks_fin_inst = Column(NUMBER(20,4))
    derivative_fin_liab = Column(NUMBER(20,4))
    cust_bank_dep = Column(NUMBER(20,4))
    agency_bus_liab = Column(NUMBER(20,4))
    oth_liab = Column(NUMBER(20,4))
    prem_received_adv = Column(NUMBER(20,4))
    deposit_received = Column(NUMBER(20,4))
    insured_deposit_invest = Column(NUMBER(20,4))
    unearned_prem_rsrv = Column(NUMBER(20,4))
    out_loss_rsrv = Column(NUMBER(20,4))
    life_insur_rsrv = Column(NUMBER(20,4))
    lt_health_insur_v = Column(NUMBER(20,4))
    independent_acct_liab = Column(NUMBER(20,4))
    incl_pledge_loan = Column(NUMBER(20,4))
    claims_payable = Column(NUMBER(20,4))
    dvd_payable_insured = Column(NUMBER(20,4))
    tot_liab = Column(NUMBER(20,4))
    cap_stk = Column(NUMBER(20,4))
    cap_rsrv = Column(NUMBER(20,4))
    special_rsrv = Column(NUMBER(20,4))
    surplus_rsrv = Column(NUMBER(20,4))
    undistributed_profit = Column(NUMBER(20,4))
    less_tsy_stk = Column(NUMBER(20,4))
    prov_nom_risks = Column(NUMBER(20,4))
    cnvd_diff_foreign_curr_stat = Column(NUMBER(20,4))
    unconfirmed_invest_loss = Column(NUMBER(20,4))
    minority_int = Column(NUMBER(20,4))
    tot_shrhldr_eqy_excl_min_int = Column(NUMBER(20,4))
    tot_shrhldr_eqy_incl_min_int = Column(NUMBER(20,4))
    tot_liab_shrhldr_eqy = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
