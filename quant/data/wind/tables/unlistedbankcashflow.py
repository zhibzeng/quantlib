from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


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

    """
    object_id = Column(VARCHAR2(100))
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
    
