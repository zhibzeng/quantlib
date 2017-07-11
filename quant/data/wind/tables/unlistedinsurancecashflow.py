from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class UnlistedInsuranceCashFlow(BaseModel):
    """
    非上市保险现金流量表

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
    cash_recp_prem_orig_inco: NUMBER(20,4)
        收到原保险合同保费取得的现金   
    net_cash_received_reinsu_bus: NUMBER(20,4)
        收到再保业务现金净额   
    other_cash_recp_ral_oper_act: NUMBER(20,4)
        收到其他与经营活动有关的现金   
    net_incr_insured_dep: NUMBER(20,4)
        保户储金净增加额   
    spe_bal_cash_inflows_oper: NUMBER(20,4)
        经营活动现金流入差额(特殊报表科目)   
    tot_bal_cash_inflows_oper: NUMBER(20,4)
        经营活动现金流入差额(合计平衡项目)   
    stot_cash_inflows_oper_act: NUMBER(20,4)
        经营活动现金流入小计   
    cash_pay_claims_orig_inco: NUMBER(20,4)
        支付原保险合同赔付款项的现金   
    cash_pay_beh_empl: NUMBER(20,4)
        支付给职工以及为职工支付的现金   
    handling_chrg_paid: NUMBER(20,4)
        支付手续费的现金   
    pay_all_typ_tax: NUMBER(20,4)
        支付的各项税费   
    other_cash_pay_ral_oper_act: NUMBER(20,4)
        支付其他与经营活动有关的现金   
    comm_insur_plcy_paid: NUMBER(20,4)
        支付保单红利的现金   
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
    net_incr_pledge_loan: NUMBER(20,4)
        质押贷款净增加额   
    cash_pay_acq_const_fiolta: NUMBER(20,4)
        购建固定资产、无形资产和其他长期资产支   

    """
    __tablename__ = "UnlistedInsuranceCashFlow"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_compcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    free_cash_flow = Column(NUMBER(20,4))
    actual_ann_dt = Column(VARCHAR2(8))
    cash_recp_prem_orig_inco = Column(NUMBER(20,4))
    net_cash_received_reinsu_bus = Column(NUMBER(20,4))
    other_cash_recp_ral_oper_act = Column(NUMBER(20,4))
    net_incr_insured_dep = Column(NUMBER(20,4))
    spe_bal_cash_inflows_oper = Column(NUMBER(20,4))
    tot_bal_cash_inflows_oper = Column(NUMBER(20,4))
    stot_cash_inflows_oper_act = Column(NUMBER(20,4))
    cash_pay_claims_orig_inco = Column(NUMBER(20,4))
    cash_pay_beh_empl = Column(NUMBER(20,4))
    handling_chrg_paid = Column(NUMBER(20,4))
    pay_all_typ_tax = Column(NUMBER(20,4))
    other_cash_pay_ral_oper_act = Column(NUMBER(20,4))
    comm_insur_plcy_paid = Column(NUMBER(20,4))
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
    net_incr_pledge_loan = Column(NUMBER(20,4))
    cash_pay_acq_const_fiolta = Column(NUMBER(20,4))
    
