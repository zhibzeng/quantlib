from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class UnlistedBankCashFlow(BaseModel):
    """
    非上市银行现金流量表

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
        报表类型   报表类型:408001000:合并报表408002000:合并报告(单季度)408003000:合并报告(单季度调整)408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408007000:母公司报表(单季度)408008000:母公司报告(单季度调整)408009000:母公司报表(调整)408010000:母公司报表(更正前)
    crncy_code: VARCHAR2(10)
        货币代码   CNY
    free_cash_flow: NUMBER(20,4)
        企业自由现金流量(FCFF)   
    actual_ann_dt: VARCHAR2(8)
        实际公告日期   
    net_incr_dep_cob: NUMBER(20,4)
        客户存款和同业存放款项净增加额   
    net_incr_loans_central_bank: NUMBER(20,4)
        向中央银行借款净增加额   
    net_incr_fund_borr_ofi: NUMBER(20,4)
        向其他金融机构拆入资金净增加额   
    net_incr_int_handling_chrg: NUMBER(20,4)
        收取利息和手续费净增加额   
    other_cash_recp_ral_oper_act: NUMBER(20,4)
        收到其他与经营活动有关的现金   
    spe_bal_cash_inflows_oper: NUMBER(20,4)
        经营活动现金流入差额(特殊报表科目)   
    tot_bal_cash_inflows_oper: NUMBER(20,4)
        经营活动现金流入差额(合计平衡项目)   
    stot_cash_inflows_oper_act: NUMBER(20,4)
        经营活动现金流入小计   
    net_incr_clients_loan_adv: NUMBER(20,4)
        客户贷款及垫款净增加额   
    net_incr_dep_cbob: NUMBER(20,4)
        存放央行和同业款项净增加额   
    cash_pay_beh_empl: NUMBER(20,4)
        支付给职工以及为职工支付的现金   
    pay_all_typ_tax: NUMBER(20,4)
        支付的各项税费   
    other_cash_pay_ral_oper_act: NUMBER(20,4)
        支付其他与经营活动有关的现金   
    handling_chrg_paid: NUMBER(20,4)
        支付手续费的现金   
    spe_bal_cash_outflows_oper: NUMBER(20,4)
        经营活动现金流出差额(特殊报表科目)   
    tot_bal_cash_outflows_oper: NUMBER(20,4)
        经营活动现金流出差额(合计平衡项目)   
    stot_cash_outflows_oper_act: NUMBER(20,4)
        经营活动现金流出小计   
    tot_bal_netcash_outflows_oper: NUMBER(20,4)
        经营活动产生的现金量净额差额(合计平衡项目)   
    net_cash_flows_oper_act: NUMBER(20,4)
        经营活动产生的现金流量净额   
    cash_recp_disp_withdrwl_invest: NUMBER(20,4)
        收回投资收到的现金   
    cash_recp_return_invest: NUMBER(20,4)
        取得投资收益收到的现金   
    net_cash_recp_disp_fiolta: NUMBER(20,4)
        处置固定资产、无形资产和其他长期资产收回的现金净额   
    other_cash_recp_ral_inv_act: NUMBER(20,4)
        收到其他与投资活动有关的现金   
    spe_bal_cash_inflows_inv: NUMBER(20,4)
        投资活动现金流入差额(特殊报表科目)   
    tot_bal_cash_inflows_inv: NUMBER(20,4)
        投资活动现金流入差额(合计平衡项目)   
    stot_cash_inflows_inv_act: NUMBER(20,4)
        投资活动现金流入小计   
    cash_paid_invest: NUMBER(20,4)
        投资支付的现金   
    cash_pay_acq_const_fiolta: NUMBER(20,4)
        购建固定资产、无形资产和其他长期资产支付的现金   
    other_cash_pay_ral_inv_act: NUMBER(20,4)
        支付其他与投资活动有关的现金   
    spe_bal_cash_outflows_inv: NUMBER(20,4)
        投资活动现金流出差额(特殊报表科目)   
    tot_bal_cash_outflows_inv: NUMBER(20,4)
        投资活动现金流出差额(合计平衡项目)   
    stot_cash_outflows_inv_act: NUMBER(20,4)
        投资活动现金流出小计   
    tot_bal_netcash_outflows_inv: NUMBER(20,4)
        投资活动产生的现金量净额差额(合计平衡项目)   
    net_cash_flows_inv_act: NUMBER(20,4)
        投资活动产生的现金流量净额   
    cash_recp_cap_contrib: NUMBER(20,4)
        吸收投资收到的现金   
    cash_recp_borrow: NUMBER(20,4)
        取得借款收到的现金   
    proc_issue_bonds: NUMBER(20,4)
        发行债券收到的现金   
    other_cash_recp_ral_fnc_act: NUMBER(20,4)
        收到其他与筹资活动有关的现金   
    stot_cash_inflows_fnc_act: NUMBER(20,4)
        筹资活动现金流入小计   
    cash_prepay_amt_borr: NUMBER(20,4)
        偿还债务支付的现金   
    cash_pay_dist_dpcp_int_exp: NUMBER(20,4)
        分配股利、利润或偿付利息支付的现金   
    other_cash_pay_ral_fnc_act: NUMBER(20,4)
        支付其他与筹资活动有关的现金   
    spe_bal_cash_inflows_fnc: NUMBER(20,4)
        筹资活动现金流入差额(特殊报表科目)   
    tot_bal_cash_inflows_fnc: NUMBER(20,4)
        筹资活动现金流入差额(合计平衡项目)   
    stot_cash_outflows_fnc_act: NUMBER(20,4)
        筹资活动现金流出小计   
    tot_bal_netcash_outflows_fnc: NUMBER(20,4)
        筹资活动产生的现金量净额差额(合计平衡项目)   
    net_cash_flows_fnc_act: NUMBER(20,4)
        筹资活动产生的现金流量净额   
    eff_fx_flu_cash: NUMBER(20,4)
        汇率变动对现金的影响   
    spe_bal_netcash_equ_dir: NUMBER(20,4)
        直接法-现金及现金等价物净增加额差额(特殊报表科目)   
    tot_bal_netcash_equ_dir: NUMBER(20,4)
        直接法-现金及现金等价物净增加额差额(合计平衡项目)   
    net_incr_cash_cash_equ: NUMBER(20,4)
        现金及现金等价物净增加额   
    cash_cash_equ_beg_period: NUMBER(20,4)
        期初现金及现金等价物余额   
    cash_cash_equ_end_period: NUMBER(20,4)
        期末现金及现金等价物余额   
    net_profit: NUMBER(20,4)
        净利润   
    plus_prov_depr_assets: NUMBER(20,4)
        加:资产减值准备   
    depr_fa_coga_dpba: NUMBER(20,4)
        固定资产折旧、油气资产折耗、生产性生物资产折旧   
    amort_intang_assets: NUMBER(20,4)
        无形资产摊销   
    amort_lt_deferred_exp: NUMBER(20,4)
        长期待摊费用摊销   
    decr_deferred_exp: NUMBER(20,4)
        待摊费用减少   
    incr_acc_exp: NUMBER(20,4)
        预提费用增加   
    loss_disp_fiolta: NUMBER(20,4)
        处置固定、无形资产和其他长期资产的损失   
    loss_scr_fa: NUMBER(20,4)
        固定资产报废损失   
    loss_fv_chg: NUMBER(20,4)
        公允价值变动损失   
    fin_exp: NUMBER(20,4)
        财务费用   
    invest_loss: NUMBER(20,4)
        投资损失   
    decr_deferred_inc_tax_assets: NUMBER(20,4)
        递延所得税资产减少   
    incr_deferred_inc_tax_liab: NUMBER(20,4)
        递延所得税负债增加   
    decr_inventories: NUMBER(20,4)
        存货的减少   
    decr_oper_payable: NUMBER(20,4)
        经营性应收项目的减少   
    incr_oper_payable: NUMBER(20,4)
        经营性应付项目的增加   
    others: NUMBER(20,4)
        其他   
    spe_bal_netcash_equ_undir: NUMBER(20,4)
        间接法-经营活动现金流量净额差额(特殊报表科目)   
    tot_bal_netcash_equ_undir: NUMBER(20,4)
        间接法-经营活动现金流量净额差额(合计平衡项目)   
    im_net_cash_flows_oper_act: NUMBER(20,4)
        间接法-经营活动产生的现金流量净额   
    conv_debt_into_cap: NUMBER(20,4)
        债务转为资本   
    conv_corp_bonds_due_within_1y: NUMBER(20,4)
        一年内到期的可转换公司债券   
    fa_fnc_leases: NUMBER(20,4)
        融资租入固定资产   
    end_bal_cash: NUMBER(20,4)
        现金的期末余额   
    less_beg_bal_cash: NUMBER(20,4)
        减:现金的期初余额   
    plus_end_bal_cash_equ: NUMBER(20,4)
        加:现金等价物的期末余额   
    less_beg_bal_cash_equ: NUMBER(20,4)
        减:现金等价物的期初余额   
    spe_bal_netcash_inc_undir: NUMBER(20,4)
        间接法-现金净增加额差额(特殊报表科目)   
    tot_bal_netcash_inc_undir: NUMBER(20,4)
        间接法-现金净增加额差额(合计平衡项目)   
    im_net_incr_cash_cash_equ: NUMBER(20,4)
        间接法-现金及现金等价物净增加额   

    """
    __tablename__ = "UnlistedBankCashFlow"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_compcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    free_cash_flow = Column(NUMBER(20,4))
    actual_ann_dt = Column(VARCHAR2(8))
    net_incr_dep_cob = Column(NUMBER(20,4))
    net_incr_loans_central_bank = Column(NUMBER(20,4))
    net_incr_fund_borr_ofi = Column(NUMBER(20,4))
    net_incr_int_handling_chrg = Column(NUMBER(20,4))
    other_cash_recp_ral_oper_act = Column(NUMBER(20,4))
    spe_bal_cash_inflows_oper = Column(NUMBER(20,4))
    tot_bal_cash_inflows_oper = Column(NUMBER(20,4))
    stot_cash_inflows_oper_act = Column(NUMBER(20,4))
    net_incr_clients_loan_adv = Column(NUMBER(20,4))
    net_incr_dep_cbob = Column(NUMBER(20,4))
    cash_pay_beh_empl = Column(NUMBER(20,4))
    pay_all_typ_tax = Column(NUMBER(20,4))
    other_cash_pay_ral_oper_act = Column(NUMBER(20,4))
    handling_chrg_paid = Column(NUMBER(20,4))
    spe_bal_cash_outflows_oper = Column(NUMBER(20,4))
    tot_bal_cash_outflows_oper = Column(NUMBER(20,4))
    stot_cash_outflows_oper_act = Column(NUMBER(20,4))
    tot_bal_netcash_outflows_oper = Column(NUMBER(20,4))
    net_cash_flows_oper_act = Column(NUMBER(20,4))
    cash_recp_disp_withdrwl_invest = Column(NUMBER(20,4))
    cash_recp_return_invest = Column(NUMBER(20,4))
    net_cash_recp_disp_fiolta = Column(NUMBER(20,4))
    other_cash_recp_ral_inv_act = Column(NUMBER(20,4))
    spe_bal_cash_inflows_inv = Column(NUMBER(20,4))
    tot_bal_cash_inflows_inv = Column(NUMBER(20,4))
    stot_cash_inflows_inv_act = Column(NUMBER(20,4))
    cash_paid_invest = Column(NUMBER(20,4))
    cash_pay_acq_const_fiolta = Column(NUMBER(20,4))
    other_cash_pay_ral_inv_act = Column(NUMBER(20,4))
    spe_bal_cash_outflows_inv = Column(NUMBER(20,4))
    tot_bal_cash_outflows_inv = Column(NUMBER(20,4))
    stot_cash_outflows_inv_act = Column(NUMBER(20,4))
    tot_bal_netcash_outflows_inv = Column(NUMBER(20,4))
    net_cash_flows_inv_act = Column(NUMBER(20,4))
    cash_recp_cap_contrib = Column(NUMBER(20,4))
    cash_recp_borrow = Column(NUMBER(20,4))
    proc_issue_bonds = Column(NUMBER(20,4))
    other_cash_recp_ral_fnc_act = Column(NUMBER(20,4))
    stot_cash_inflows_fnc_act = Column(NUMBER(20,4))
    cash_prepay_amt_borr = Column(NUMBER(20,4))
    cash_pay_dist_dpcp_int_exp = Column(NUMBER(20,4))
    other_cash_pay_ral_fnc_act = Column(NUMBER(20,4))
    spe_bal_cash_inflows_fnc = Column(NUMBER(20,4))
    tot_bal_cash_inflows_fnc = Column(NUMBER(20,4))
    stot_cash_outflows_fnc_act = Column(NUMBER(20,4))
    tot_bal_netcash_outflows_fnc = Column(NUMBER(20,4))
    net_cash_flows_fnc_act = Column(NUMBER(20,4))
    eff_fx_flu_cash = Column(NUMBER(20,4))
    spe_bal_netcash_equ_dir = Column(NUMBER(20,4))
    tot_bal_netcash_equ_dir = Column(NUMBER(20,4))
    net_incr_cash_cash_equ = Column(NUMBER(20,4))
    cash_cash_equ_beg_period = Column(NUMBER(20,4))
    cash_cash_equ_end_period = Column(NUMBER(20,4))
    net_profit = Column(NUMBER(20,4))
    plus_prov_depr_assets = Column(NUMBER(20,4))
    depr_fa_coga_dpba = Column(NUMBER(20,4))
    amort_intang_assets = Column(NUMBER(20,4))
    amort_lt_deferred_exp = Column(NUMBER(20,4))
    decr_deferred_exp = Column(NUMBER(20,4))
    incr_acc_exp = Column(NUMBER(20,4))
    loss_disp_fiolta = Column(NUMBER(20,4))
    loss_scr_fa = Column(NUMBER(20,4))
    loss_fv_chg = Column(NUMBER(20,4))
    fin_exp = Column(NUMBER(20,4))
    invest_loss = Column(NUMBER(20,4))
    decr_deferred_inc_tax_assets = Column(NUMBER(20,4))
    incr_deferred_inc_tax_liab = Column(NUMBER(20,4))
    decr_inventories = Column(NUMBER(20,4))
    decr_oper_payable = Column(NUMBER(20,4))
    incr_oper_payable = Column(NUMBER(20,4))
    others = Column(NUMBER(20,4))
    spe_bal_netcash_equ_undir = Column(NUMBER(20,4))
    tot_bal_netcash_equ_undir = Column(NUMBER(20,4))
    im_net_cash_flows_oper_act = Column(NUMBER(20,4))
    conv_debt_into_cap = Column(NUMBER(20,4))
    conv_corp_bonds_due_within_1y = Column(NUMBER(20,4))
    fa_fnc_leases = Column(NUMBER(20,4))
    end_bal_cash = Column(NUMBER(20,4))
    less_beg_bal_cash = Column(NUMBER(20,4))
    plus_end_bal_cash_equ = Column(NUMBER(20,4))
    less_beg_bal_cash_equ = Column(NUMBER(20,4))
    spe_bal_netcash_inc_undir = Column(NUMBER(20,4))
    tot_bal_netcash_inc_undir = Column(NUMBER(20,4))
    im_net_incr_cash_cash_equ = Column(NUMBER(20,4))
    
