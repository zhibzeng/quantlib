from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


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

    """
    object_id = Column(VARCHAR2(100))
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
    
