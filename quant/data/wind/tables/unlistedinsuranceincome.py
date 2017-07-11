from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class UnlistedInsuranceIncome(BaseModel):
    """
    非上市保险利润表

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
        报表类型   报表类型:408001000:合并报表408002000:合并报表(单季度)408003000:合并报表(单季度调整)408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408007000:母公司报表(单季度)408008000:母公司报表(单季度调整)408009000:母公司报表(调整)408010000:母公司报表(更正前)
    crncy_code: VARCHAR2(10)
        货币代码   CNY
    ebit: NUMBER(20,4)
        息税前利润   
    ebitda: NUMBER(20,4)
        息税折旧摊销前利润   
    net_profit_after_ded_nr_lp: NUMBER(20,4)
        扣除非经常性损益后净利润   
    net_profit_under_intl_acc_sta: NUMBER(20,4)
        国际会计准则净利润   
    s_fa_eps_basic: NUMBER(20,4)
        基本每股收益   
    s_fa_eps_diluted: NUMBER(20,4)
        稀释每股收益   
    actual_ann_dt: VARCHAR2(8)
        实际公告日期   
    oper_rev: NUMBER(20,4)
        营业收入   
    insur_prem_unearned: NUMBER(20,4)
        已赚保费   
    prem_inc: NUMBER(20,4)
        保费业务收入   
    incl_reinsurance_prem_inc: NUMBER(20,4)
        其中:分保费收入   
    less_ceded_out_prem: NUMBER(20,4)
        减:分出保费   
    chg_unearned_prem_res: NUMBER(20,4)
        提取未到期责任准备金   
    plus_net_invest_inc: NUMBER(20,4)
        加:投资净收益   
    incl_inc_invest_assoc_jv_entp: NUMBER(20,4)
        其中:对联营企业和合营企业的投资收益   
    plus_net_gain_chg_fv: NUMBER(20,4)
        加:公允价值变动净收益   
    plus_net_gain_fx_trans: NUMBER(20,4)
        加:汇兑净收益   
    oper_exp: NUMBER(20,4)
        营业支出   
    prepay_surr: NUMBER(20,4)
        退保金   
    tot_claim_exp: NUMBER(20,4)
        赔付总支出   
    less_claim_recb_reinsurer: NUMBER(20,4)
        减:摊回赔付支出   
    less_ins_rsrv_recb_reinsurer: NUMBER(20,4)
        减:摊回保险责任准备金   
    dvd_exp_insured: NUMBER(20,4)
        保户红利支出   
    reinsurance_exp: NUMBER(20,4)
        分保费用   
    less_taxes_surcharges_ops: NUMBER(20,4)
        减:营业税金及附加   
    less_handling_chrg_comm_exp: NUMBER(20,4)
        减:手续费及佣金支出   
    less_gerl_admin_exp: NUMBER(20,4)
        减:管理费用   
    less_exp_recb_reinsurer: NUMBER(20,4)
        减:摊回分保费用   
    other_bus_cost: NUMBER(20,4)
        其他业务成本   
    less_impair_loss_assets: NUMBER(20,4)
        减:资产减值损失   
    spe_bal_oper_profit: NUMBER(20,4)
        营业利润差额(特殊报表科目)   
    tot_bal_oper_profit: NUMBER(20,4)
        营业利润差额(合计平衡项目)   
    oper_profit: NUMBER(20,4)
        营业利润   
    plus_non_oper_rev: NUMBER(20,4)
        加:营业外收入   
    less_non_oper_exp: NUMBER(20,4)
        减:营业外支出   
    il_net_loss_disp_noncur_asset: NUMBER(20,4)
        其中:减:非流动资产处置净损失   
    spe_bal_tot_profit: NUMBER(20,4)
        利润总额差额(特殊报表科目)   
    tot_bal_tot_profit: NUMBER(20,4)
        利润总额差额(合计平衡项目)   
    tot_profit: NUMBER(20,4)
        利润总额   
    inc_tax: NUMBER(20,4)
        所得税   
    unconfirmed_invest_loss: NUMBER(20,4)
        未确认投资损失   
    spe_bal_net_profit: NUMBER(20,4)
        净利润总额差额(特殊报表科目)   
    tot_bal_net_profit: NUMBER(20,4)
        净利润总额差额(合计平衡项目)   
    net_profit_incl_min_int_inc: NUMBER(20,4)
        净利润(含少数股东损益)   
    net_profit_excl_min_int_inc: NUMBER(20,4)
        净利润(不含少数股东损益)   
    minority_int_inc: NUMBER(20,4)
        少数股东损益   

    """
    __tablename__ = "UnlistedInsuranceIncome"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_compcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    ebit = Column(NUMBER(20,4))
    ebitda = Column(NUMBER(20,4))
    net_profit_after_ded_nr_lp = Column(NUMBER(20,4))
    net_profit_under_intl_acc_sta = Column(NUMBER(20,4))
    s_fa_eps_basic = Column(NUMBER(20,4))
    s_fa_eps_diluted = Column(NUMBER(20,4))
    actual_ann_dt = Column(VARCHAR2(8))
    oper_rev = Column(NUMBER(20,4))
    insur_prem_unearned = Column(NUMBER(20,4))
    prem_inc = Column(NUMBER(20,4))
    incl_reinsurance_prem_inc = Column(NUMBER(20,4))
    less_ceded_out_prem = Column(NUMBER(20,4))
    chg_unearned_prem_res = Column(NUMBER(20,4))
    plus_net_invest_inc = Column(NUMBER(20,4))
    incl_inc_invest_assoc_jv_entp = Column(NUMBER(20,4))
    plus_net_gain_chg_fv = Column(NUMBER(20,4))
    plus_net_gain_fx_trans = Column(NUMBER(20,4))
    oper_exp = Column(NUMBER(20,4))
    prepay_surr = Column(NUMBER(20,4))
    tot_claim_exp = Column(NUMBER(20,4))
    less_claim_recb_reinsurer = Column(NUMBER(20,4))
    less_ins_rsrv_recb_reinsurer = Column(NUMBER(20,4))
    dvd_exp_insured = Column(NUMBER(20,4))
    reinsurance_exp = Column(NUMBER(20,4))
    less_taxes_surcharges_ops = Column(NUMBER(20,4))
    less_handling_chrg_comm_exp = Column(NUMBER(20,4))
    less_gerl_admin_exp = Column(NUMBER(20,4))
    less_exp_recb_reinsurer = Column(NUMBER(20,4))
    other_bus_cost = Column(NUMBER(20,4))
    less_impair_loss_assets = Column(NUMBER(20,4))
    spe_bal_oper_profit = Column(NUMBER(20,4))
    tot_bal_oper_profit = Column(NUMBER(20,4))
    oper_profit = Column(NUMBER(20,4))
    plus_non_oper_rev = Column(NUMBER(20,4))
    less_non_oper_exp = Column(NUMBER(20,4))
    il_net_loss_disp_noncur_asset = Column(NUMBER(20,4))
    spe_bal_tot_profit = Column(NUMBER(20,4))
    tot_bal_tot_profit = Column(NUMBER(20,4))
    tot_profit = Column(NUMBER(20,4))
    inc_tax = Column(NUMBER(20,4))
    unconfirmed_invest_loss = Column(NUMBER(20,4))
    spe_bal_net_profit = Column(NUMBER(20,4))
    tot_bal_net_profit = Column(NUMBER(20,4))
    net_profit_incl_min_int_inc = Column(NUMBER(20,4))
    net_profit_excl_min_int_inc = Column(NUMBER(20,4))
    minority_int_inc = Column(NUMBER(20,4))
    
