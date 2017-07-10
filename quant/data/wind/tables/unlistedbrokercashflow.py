from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class UnlistedBrokerCashFlow(BaseModel):
    """
    非上市券商现金流量表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_compcode: VARCHAR2(40)
        公司代码   
    wind_code: VARCHAR2(40)
        Wind代码   
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
    net_incr_disp_tfa: NUMBER(20,4)
        处置交易性金融资产净增加额   
    net_incr_disp_faas: NUMBER(20,4)
        处置可供出售金融资产净增加额   
    net_incr_int_handling_chrg: NUMBER(20,4)
        收取利息和手续费净增加额   
    net_incr_loans_other_bank: NUMBER(20,4)
        拆入资金净增加额   
    net_incr_repurch_bus_fund: NUMBER(20,4)
        回购业务资金净增加额   
    other_cash_recp_ral_oper_act: NUMBER(20,4)
        收到其他与经营活动有关的现金   
    spe_bal_cash_inflows_oper: NUMBER(20,4)
        经营活动现金流入差额(特殊报表科目)   
    tot_bal_cash_inflows_oper: NUMBER(20,4)
        经营活动现金流入差额(合计平衡项目)   

    """
    object_id = Column(VARCHAR2(100))
    s_info_compcode = Column(VARCHAR2(40))
    wind_code = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    free_cash_flow = Column(NUMBER(20,4))
    actual_ann_dt = Column(VARCHAR2(8))
    net_incr_disp_tfa = Column(NUMBER(20,4))
    net_incr_disp_faas = Column(NUMBER(20,4))
    net_incr_int_handling_chrg = Column(NUMBER(20,4))
    net_incr_loans_other_bank = Column(NUMBER(20,4))
    net_incr_repurch_bus_fund = Column(NUMBER(20,4))
    other_cash_recp_ral_oper_act = Column(NUMBER(20,4))
    spe_bal_cash_inflows_oper = Column(NUMBER(20,4))
    tot_bal_cash_inflows_oper = Column(NUMBER(20,4))
    
