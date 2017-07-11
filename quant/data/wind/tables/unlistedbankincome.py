from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class UnlistedBankIncome(BaseModel):
    """
    非上市银行利润表

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
    net_int_inc: NUMBER(20,4)
        利息净收入   
    int_inc: NUMBER(20,4)
        利息收入   
    less_int_exp: NUMBER(20,4)
        减:利息支出   
    net_handling_chrg_comm_inc: NUMBER(20,4)
        手续费及佣金净收入   
    handling_chrg_comm_inc: NUMBER(20,4)
        手续费及佣金收入   
    less_handling_chrg_comm_exp: NUMBER(20,4)
        减:手续费及佣金支出   
    plus_net_invest_inc: NUMBER(20,4)
        加:投资净收益   
    incl_inc_invest_assoc_jv_entp: NUMBER(20,4)
        其中:对联营企业和合营企业的投资收益   
    plus_net_gain_chg_fv: NUMBER(20,4)
        加:公允价值变动净收益   
    net_inc_other_ops: NUMBER(20,4)
        其他经营净收益   
    plus_net_gain_fx_trans: NUMBER(20,4)
        加:汇兑净收益   
    plus_net_inc_other_bus: NUMBER(20,4)
        加:其他业务净收益   
    other_bus_inc: NUMBER(20,4)
        其他业务收入   
    other_bus_cost: NUMBER(20,4)
        其他业务成本   
    oper_exp: NUMBER(20,4)
        营业支出   
    less_taxes_surcharges_ops: NUMBER(20,4)
        减:营业税金及附加   
    less_gerl_admin_exp: NUMBER(20,4)
        减:管理费用   
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
    other_compreh_inc: NUMBER(20,4)
        其他综合收益   
    tot_compreh_inc: NUMBER(20,4)
        综合收益总额   
    tot_compreh_inc_min_shrhldr: NUMBER(20,4)
        综合收益总额(少数股东)   
    tot_compreh_inc_parent_comp: NUMBER(20,4)
        综合收益总额(母公司)   

    """
    __tablename__ = "UnlistedBankIncome"
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
    net_int_inc = Column(NUMBER(20,4))
    int_inc = Column(NUMBER(20,4))
    less_int_exp = Column(NUMBER(20,4))
    net_handling_chrg_comm_inc = Column(NUMBER(20,4))
    handling_chrg_comm_inc = Column(NUMBER(20,4))
    less_handling_chrg_comm_exp = Column(NUMBER(20,4))
    plus_net_invest_inc = Column(NUMBER(20,4))
    incl_inc_invest_assoc_jv_entp = Column(NUMBER(20,4))
    plus_net_gain_chg_fv = Column(NUMBER(20,4))
    net_inc_other_ops = Column(NUMBER(20,4))
    plus_net_gain_fx_trans = Column(NUMBER(20,4))
    plus_net_inc_other_bus = Column(NUMBER(20,4))
    other_bus_inc = Column(NUMBER(20,4))
    other_bus_cost = Column(NUMBER(20,4))
    oper_exp = Column(NUMBER(20,4))
    less_taxes_surcharges_ops = Column(NUMBER(20,4))
    less_gerl_admin_exp = Column(NUMBER(20,4))
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
    other_compreh_inc = Column(NUMBER(20,4))
    tot_compreh_inc = Column(NUMBER(20,4))
    tot_compreh_inc_min_shrhldr = Column(NUMBER(20,4))
    tot_compreh_inc_parent_comp = Column(NUMBER(20,4))
    
