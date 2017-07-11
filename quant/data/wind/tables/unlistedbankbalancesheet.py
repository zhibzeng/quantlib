from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class UnlistedBankBalanceSheet(BaseModel):
    """
    非上市银行资产负债表

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
    cash_deposits_central_bank: NUMBER(20,4)
        现金及存放中央银行款项   
    asset_dep_oth_banks_fin_inst: NUMBER(20,4)
        存放同业和其它金融机构款项   
    precious_metals: NUMBER(20,4)
        贵金属   
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
    loans_and_adv_granted: NUMBER(20,4)
        发放贷款及垫款   
    agency_bus_assets: NUMBER(20,4)
        代理业务资产   
    fin_assets_avail_for_sale: NUMBER(20,4)
        可供出售金融资产   
    held_to_mty_invest: NUMBER(20,4)
        持有至到期投资   
    long_term_eqy_invest: NUMBER(20,4)
        长期股权投资   
    rcv_invest: NUMBER(20,4)
        应收款项类投资   
    fix_assets: NUMBER(20,4)
        固定资产   
    intang_assets: NUMBER(20,4)
        无形资产   
    goodwill: NUMBER(20,4)
        商誉   
    deferred_tax_assets: NUMBER(20,4)
        递延所得税资产   
    invest_real_estate: NUMBER(20,4)
        投资性房地产   
    oth_assets: NUMBER(20,4)
        其他资产   
    spe_bal_assets: NUMBER(20,4)
        资产差额(特殊报表科目)   
    tot_bal_assets: NUMBER(20,4)
        资产差额(合计平衡项目)   
    tot_assets: NUMBER(20,4)
        资产总计   
    liab_dep_oth_banks_fin_inst: NUMBER(20,4)
        同业和其它金融机构存放款项   
    borrow_central_bank: NUMBER(20,4)
        向中央银行借款   
    loans_oth_banks: NUMBER(20,4)
        拆入资金   
    tradable_fin_liab: NUMBER(20,4)
        交易性金融负债   
    derivative_fin_liab: NUMBER(20,4)
        衍生金融负债   
    fund_sales_fin_assets_rp: NUMBER(20,4)
        卖出回购金融资产款   
    cust_bank_dep: NUMBER(20,4)
        吸收存款   
    empl_ben_payable: NUMBER(20,4)
        应付职工薪酬   
    taxes_surcharges_payable: NUMBER(20,4)
        应交税费   
    int_payable: NUMBER(20,4)
        应付利息   
    agency_bus_liab: NUMBER(20,4)
        代理业务负债   
    bonds_payable: NUMBER(20,4)
        应付债券   
    deferred_tax_liab: NUMBER(20,4)
        递延所得税负债   
    provisions: NUMBER(20,4)
        预计负债   
    oth_liab: NUMBER(20,4)
        其他负债   
    spe_bal_liab: NUMBER(20,4)
        负债差额(特殊报表科目)   
    tot_bal_liab: NUMBER(20,4)
        负债差额(合计平衡项目)   
    tot_liab: NUMBER(20,4)
        负债合计   
    cap_stk: NUMBER(20,4)
        股本(实收资本)   
    cap_rsrv: NUMBER(20,4)
        资本公积金   
    less_tsy_stk: NUMBER(20,4)
        减:库存股   
    surplus_rsrv: NUMBER(20,4)
        盈余公积金   
    undistributed_profit: NUMBER(20,4)
        未分配利润   
    prov_nom_risks: NUMBER(20,4)
        一般风险准备   
    cnvd_diff_foreign_curr_stat: NUMBER(20,4)
        外币报表折算差额   
    unconfirmed_invest_loss: NUMBER(20,4)
        未确认的投资损失   
    spe_bal_shrhldr_eqy: NUMBER(20,4)
        股东权益差额(特殊报表科目)   
    tot_bal_shrhldr_eqy: NUMBER(20,4)
        股东权益差额(合计平衡项目)   
    minority_int: NUMBER(20,4)
        少数股东权益   
    tot_shrhldr_eqy_excl_min_int: NUMBER(20,4)
        股东权益合计(不含少数股东权益)   
    tot_shrhldr_eqy_incl_min_int: NUMBER(20,4)
        股东权益合计(含少数股东权益)   
    spe_bal_liab_eqy: NUMBER(20,4)
        负债及股东权益差额(特殊报表项目)   
    tot_bal_liab_eqy: NUMBER(20,4)
        负债及股东权益差额(合计平衡项目)   
    tot_liab_shrhldr_eqy: NUMBER(20,4)
        负债及股东权益总计   

    """
    __tablename__ = "UnlistedBankBalanceSheet"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_compcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    actual_ann_dt = Column(VARCHAR2(8))
    cash_deposits_central_bank = Column(NUMBER(20,4))
    asset_dep_oth_banks_fin_inst = Column(NUMBER(20,4))
    precious_metals = Column(NUMBER(20,4))
    loans_to_oth_banks = Column(NUMBER(20,4))
    tradable_fin_assets = Column(NUMBER(20,4))
    derivative_fin_assets = Column(NUMBER(20,4))
    red_monetary_cap_for_sale = Column(NUMBER(20,4))
    int_rcv = Column(NUMBER(20,4))
    loans_and_adv_granted = Column(NUMBER(20,4))
    agency_bus_assets = Column(NUMBER(20,4))
    fin_assets_avail_for_sale = Column(NUMBER(20,4))
    held_to_mty_invest = Column(NUMBER(20,4))
    long_term_eqy_invest = Column(NUMBER(20,4))
    rcv_invest = Column(NUMBER(20,4))
    fix_assets = Column(NUMBER(20,4))
    intang_assets = Column(NUMBER(20,4))
    goodwill = Column(NUMBER(20,4))
    deferred_tax_assets = Column(NUMBER(20,4))
    invest_real_estate = Column(NUMBER(20,4))
    oth_assets = Column(NUMBER(20,4))
    spe_bal_assets = Column(NUMBER(20,4))
    tot_bal_assets = Column(NUMBER(20,4))
    tot_assets = Column(NUMBER(20,4))
    liab_dep_oth_banks_fin_inst = Column(NUMBER(20,4))
    borrow_central_bank = Column(NUMBER(20,4))
    loans_oth_banks = Column(NUMBER(20,4))
    tradable_fin_liab = Column(NUMBER(20,4))
    derivative_fin_liab = Column(NUMBER(20,4))
    fund_sales_fin_assets_rp = Column(NUMBER(20,4))
    cust_bank_dep = Column(NUMBER(20,4))
    empl_ben_payable = Column(NUMBER(20,4))
    taxes_surcharges_payable = Column(NUMBER(20,4))
    int_payable = Column(NUMBER(20,4))
    agency_bus_liab = Column(NUMBER(20,4))
    bonds_payable = Column(NUMBER(20,4))
    deferred_tax_liab = Column(NUMBER(20,4))
    provisions = Column(NUMBER(20,4))
    oth_liab = Column(NUMBER(20,4))
    spe_bal_liab = Column(NUMBER(20,4))
    tot_bal_liab = Column(NUMBER(20,4))
    tot_liab = Column(NUMBER(20,4))
    cap_stk = Column(NUMBER(20,4))
    cap_rsrv = Column(NUMBER(20,4))
    less_tsy_stk = Column(NUMBER(20,4))
    surplus_rsrv = Column(NUMBER(20,4))
    undistributed_profit = Column(NUMBER(20,4))
    prov_nom_risks = Column(NUMBER(20,4))
    cnvd_diff_foreign_curr_stat = Column(NUMBER(20,4))
    unconfirmed_invest_loss = Column(NUMBER(20,4))
    spe_bal_shrhldr_eqy = Column(NUMBER(20,4))
    tot_bal_shrhldr_eqy = Column(NUMBER(20,4))
    minority_int = Column(NUMBER(20,4))
    tot_shrhldr_eqy_excl_min_int = Column(NUMBER(20,4))
    tot_shrhldr_eqy_incl_min_int = Column(NUMBER(20,4))
    spe_bal_liab_eqy = Column(NUMBER(20,4))
    tot_bal_liab_eqy = Column(NUMBER(20,4))
    tot_liab_shrhldr_eqy = Column(NUMBER(20,4))
    
