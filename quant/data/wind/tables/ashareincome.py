from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareIncome(BaseModel):
    """
    4.46 中国A股利润表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    wind_code: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    report_period: VARCHAR2(8)
        报告期   
    statement_type: VARCHAR2(10)
        报表类型   报表类型:408001000:合并报表408002000:合并报表(单季度)408003000:合并报表(单季度调整)408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408007000:母公司报表(单季度)408008000:母公司报表(单季度调整)408009000:母公司报表(调整)408010000:母公司报表(更正前)
    crncy_code: VARCHAR2(10)
        货币代码   CNY
    tot_oper_rev: NUMBER(20,4)
        营业总收入   
    oper_rev: NUMBER(20,4)
        营业收入   
    int_inc: NUMBER(20,4)
        利息收入   
    net_int_inc: NUMBER(20,4)
        利息净收入   
    insur_prem_unearned: NUMBER(20,4)
        已赚保费   
    handling_chrg_comm_inc: NUMBER(20,4)
        手续费及佣金收入   
    net_handling_chrg_comm_inc: NUMBER(20,4)
        手续费及佣金净收入   
    net_inc_other_ops: NUMBER(20,4)
        其他经营净收益   
    plus_net_inc_other_bus: NUMBER(20,4)
        加:其他业务净收益   
    prem_inc: NUMBER(20,4)
        保费业务收入   
    less_ceded_out_prem: NUMBER(20,4)
        减:分出保费   
    chg_unearned_prem_res: NUMBER(20,4)
        提取未到期责任准备金   
    incl_reinsurance_prem_inc: NUMBER(20,4)
        其中:分保费收入   
    net_inc_sec_trading_brok_bus: NUMBER(20,4)
        代理买卖证券业务净收入   
    net_inc_sec_uw_bus: NUMBER(20,4)
        证券承销业务净收入   
    net_inc_ec_asset_mgmt_bus: NUMBER(20,4)
        受托客户资产管理业务净收入   
    other_bus_inc: NUMBER(20,4)
        其他业务收入   
    plus_net_gain_chg_fv: NUMBER(20,4)
        加:公允价值变动净收益   
    plus_net_invest_inc: NUMBER(20,4)
        加:投资净收益   
    incl_inc_invest_assoc_jv_entp: NUMBER(20,4)
        其中:对联营企业和合营企业的投资收益   
    plus_net_gain_fx_trans: NUMBER(20,4)
        加:汇兑净收益   
    tot_oper_cost: NUMBER(20,4)
        营业总成本   
    less_oper_cost: NUMBER(20,4)
        减:营业成本   
    less_int_exp: NUMBER(20,4)
        减:利息支出   
    less_handling_chrg_comm_exp: NUMBER(20,4)
        减:手续费及佣金支出   
    less_taxes_surcharges_ops: NUMBER(20,4)
        减:营业税金及附加   
    less_selling_dist_exp: NUMBER(20,4)
        减:销售费用   
    less_gerl_admin_exp: NUMBER(20,4)
        减:管理费用   
    less_fin_exp: NUMBER(20,4)
        减:财务费用   
    less_impair_loss_assets: NUMBER(20,4)
        减:资产减值损失   
    prepay_surr: NUMBER(20,4)
        退保金   
    tot_claim_exp: NUMBER(20,4)
        赔付总支出   
    chg_insur_cont_rsrv: NUMBER(20,4)
        提取保险责任准备金   
    dvd_exp_insured: NUMBER(20,4)
        保户红利支出   
    reinsurance_exp: NUMBER(20,4)
        分保费用   
    oper_exp: NUMBER(20,4)
        营业支出   
    less_claim_recb_reinsurer: NUMBER(20,4)
        减:摊回赔付支出   
    less_ins_rsrv_recb_reinsurer: NUMBER(20,4)
        减:摊回保险责任准备金   
    less_exp_recb_reinsurer: NUMBER(20,4)
        减:摊回分保费用   
    other_bus_cost: NUMBER(20,4)
        其他业务成本   
    oper_profit: NUMBER(20,4)
        营业利润   
    plus_non_oper_rev: NUMBER(20,4)
        加:营业外收入   
    less_non_oper_exp: NUMBER(20,4)
        减:营业外支出   
    il_net_loss_disp_noncur_asset: NUMBER(20,4)
        其中:减:非流动资产处置净损失   
    tot_profit: NUMBER(20,4)
        利润总额   
    inc_tax: NUMBER(20,4)
        所得税   
    unconfirmed_invest_loss: NUMBER(20,4)
        未确认投资损失   
    net_profit_incl_min_int_inc: NUMBER(20,4)
        净利润(含少数股东损益)   
    net_profit_excl_min_int_inc: NUMBER(20,4)
        净利润(不含少数股东损益)   
    minority_int_inc: NUMBER(20,4)
        少数股东损益   
    other_compreh_inc: NUMBER(20,4)
        其他综合收益   
    tot_compreh_inc: NUMBER(20,4)
        综合收益总额   
    tot_compreh_inc_parent_comp: NUMBER(20,4)
        综合收益总额(母公司)   
    tot_compreh_inc_min_shrhldr: NUMBER(20,4)
        综合收益总额(少数股东)   
    ebit: NUMBER(20,4)
        息税前利润   
    ebitda: NUMBER(20,4)
        息税折旧摊销前利润   
    net_profit_after_ded_nr_lp: NUMBER(20,4)
        扣除非经常性损益后净利润   
    net_profit_under_intl_acc_sta: NUMBER(20,4)
        国际会计准则净利润   
    comp_type_code: VARCHAR2(2)
        公司类型代码   1非金融类2银行3保险4证券
    s_fa_eps_basic: NUMBER(20,4)
        基本每股收益   
    s_fa_eps_diluted: NUMBER(20,4)
        稀释每股收益   
    actual_ann_dt: VARCHAR2(8)
        实际公告日期   
    insurance_expense: NUMBER(20,4)
        保险业务支出   
    spe_bal_oper_profit: NUMBER(20,4)
        营业利润差额(特殊报表科目)   
    tot_bal_oper_profit: NUMBER(20,4)
        营业利润差额(合计平衡项目)   
    spe_bal_tot_profit: NUMBER(20,4)
        利润总额差额(特殊报表科目)   
    tot_bal_tot_profit: NUMBER(20,4)
        利润总额差额(合计平衡项目)   
    spe_bal_net_profit: NUMBER(20,4)
        净利润差额(特殊报表科目)   
    tot_bal_net_profit: NUMBER(20,4)
        净利润差额(合计平衡项目)   
    undistributed_profit: NUMBER(20,4)
        年初未分配利润   
    adjlossgain_prevyear: NUMBER(20,4)
        调整以前年度损益   
    transfer_from_surplusreserve: NUMBER(20,4)
        盈余公积转入   
    transfer_from_housingimprest: NUMBER(20,4)
        住房周转金转入   
    transfer_from_others: NUMBER(20,4)
        其他转入   
    distributable_profit: NUMBER(20,4)
        可分配利润   
    withdr_legalsurplus: NUMBER(20,4)
        提取法定盈余公积   
    withdr_legalpubwelfunds: NUMBER(20,4)
        提取法定公益金   
    workers_welfare: NUMBER(20,4)
        职工奖金福利   
    withdr_buzexpwelfare: NUMBER(20,4)
        提取企业发展基金   
    withdr_reservefund: NUMBER(20,4)
        提取储备基金   
    distributable_profit_shrhder: NUMBER(20,4)
        可供股东分配的利润   
    prfshare_dvd_payable: NUMBER(20,4)
        应付优先股股利   
    withdr_othersurpreserve: NUMBER(20,4)
        提取任意盈余公积金   
    comshare_dvd_payable: NUMBER(20,4)
        应付普通股股利   
    capitalized_comstock_div: NUMBER(20,4)
        转作股本的普通股股利   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareIncome"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    wind_code = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    tot_oper_rev = Column(NUMBER(20,4))
    oper_rev = Column(NUMBER(20,4))
    int_inc = Column(NUMBER(20,4))
    net_int_inc = Column(NUMBER(20,4))
    insur_prem_unearned = Column(NUMBER(20,4))
    handling_chrg_comm_inc = Column(NUMBER(20,4))
    net_handling_chrg_comm_inc = Column(NUMBER(20,4))
    net_inc_other_ops = Column(NUMBER(20,4))
    plus_net_inc_other_bus = Column(NUMBER(20,4))
    prem_inc = Column(NUMBER(20,4))
    less_ceded_out_prem = Column(NUMBER(20,4))
    chg_unearned_prem_res = Column(NUMBER(20,4))
    incl_reinsurance_prem_inc = Column(NUMBER(20,4))
    net_inc_sec_trading_brok_bus = Column(NUMBER(20,4))
    net_inc_sec_uw_bus = Column(NUMBER(20,4))
    net_inc_ec_asset_mgmt_bus = Column(NUMBER(20,4))
    other_bus_inc = Column(NUMBER(20,4))
    plus_net_gain_chg_fv = Column(NUMBER(20,4))
    plus_net_invest_inc = Column(NUMBER(20,4))
    incl_inc_invest_assoc_jv_entp = Column(NUMBER(20,4))
    plus_net_gain_fx_trans = Column(NUMBER(20,4))
    tot_oper_cost = Column(NUMBER(20,4))
    less_oper_cost = Column(NUMBER(20,4))
    less_int_exp = Column(NUMBER(20,4))
    less_handling_chrg_comm_exp = Column(NUMBER(20,4))
    less_taxes_surcharges_ops = Column(NUMBER(20,4))
    less_selling_dist_exp = Column(NUMBER(20,4))
    less_gerl_admin_exp = Column(NUMBER(20,4))
    less_fin_exp = Column(NUMBER(20,4))
    less_impair_loss_assets = Column(NUMBER(20,4))
    prepay_surr = Column(NUMBER(20,4))
    tot_claim_exp = Column(NUMBER(20,4))
    chg_insur_cont_rsrv = Column(NUMBER(20,4))
    dvd_exp_insured = Column(NUMBER(20,4))
    reinsurance_exp = Column(NUMBER(20,4))
    oper_exp = Column(NUMBER(20,4))
    less_claim_recb_reinsurer = Column(NUMBER(20,4))
    less_ins_rsrv_recb_reinsurer = Column(NUMBER(20,4))
    less_exp_recb_reinsurer = Column(NUMBER(20,4))
    other_bus_cost = Column(NUMBER(20,4))
    oper_profit = Column(NUMBER(20,4))
    plus_non_oper_rev = Column(NUMBER(20,4))
    less_non_oper_exp = Column(NUMBER(20,4))
    il_net_loss_disp_noncur_asset = Column(NUMBER(20,4))
    tot_profit = Column(NUMBER(20,4))
    inc_tax = Column(NUMBER(20,4))
    unconfirmed_invest_loss = Column(NUMBER(20,4))
    net_profit_incl_min_int_inc = Column(NUMBER(20,4))
    net_profit_excl_min_int_inc = Column(NUMBER(20,4))
    minority_int_inc = Column(NUMBER(20,4))
    other_compreh_inc = Column(NUMBER(20,4))
    tot_compreh_inc = Column(NUMBER(20,4))
    tot_compreh_inc_parent_comp = Column(NUMBER(20,4))
    tot_compreh_inc_min_shrhldr = Column(NUMBER(20,4))
    ebit = Column(NUMBER(20,4))
    ebitda = Column(NUMBER(20,4))
    net_profit_after_ded_nr_lp = Column(NUMBER(20,4))
    net_profit_under_intl_acc_sta = Column(NUMBER(20,4))
    comp_type_code = Column(VARCHAR2(2))
    s_fa_eps_basic = Column(NUMBER(20,4))
    s_fa_eps_diluted = Column(NUMBER(20,4))
    actual_ann_dt = Column(VARCHAR2(8))
    insurance_expense = Column(NUMBER(20,4))
    spe_bal_oper_profit = Column(NUMBER(20,4))
    tot_bal_oper_profit = Column(NUMBER(20,4))
    spe_bal_tot_profit = Column(NUMBER(20,4))
    tot_bal_tot_profit = Column(NUMBER(20,4))
    spe_bal_net_profit = Column(NUMBER(20,4))
    tot_bal_net_profit = Column(NUMBER(20,4))
    undistributed_profit = Column(NUMBER(20,4))
    adjlossgain_prevyear = Column(NUMBER(20,4))
    transfer_from_surplusreserve = Column(NUMBER(20,4))
    transfer_from_housingimprest = Column(NUMBER(20,4))
    transfer_from_others = Column(NUMBER(20,4))
    distributable_profit = Column(NUMBER(20,4))
    withdr_legalsurplus = Column(NUMBER(20,4))
    withdr_legalpubwelfunds = Column(NUMBER(20,4))
    workers_welfare = Column(NUMBER(20,4))
    withdr_buzexpwelfare = Column(NUMBER(20,4))
    withdr_reservefund = Column(NUMBER(20,4))
    distributable_profit_shrhder = Column(NUMBER(20,4))
    prfshare_dvd_payable = Column(NUMBER(20,4))
    withdr_othersurpreserve = Column(NUMBER(20,4))
    comshare_dvd_payable = Column(NUMBER(20,4))
    capitalized_comstock_div = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
