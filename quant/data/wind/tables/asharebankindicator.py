from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareBankIndicator(BaseModel):
    """
    4.49 中国A股银行专用指标

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    report_period: VARCHAR2(8)
        报告期   
    statement_type: VARCHAR2(10)
        报表类型   报表类型:408001000:合并报表408002000:合并报告(单季度)408003000:合并报告(单季度调整)408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408007000:母公司报表(单季度)408008000:母公司报告(单季度调整)408009000:母公司报表(调整)408010000:母公司报表(更正前)
    crncy_code: VARCHAR2(10)
        货币代码   CNY
    capi_ade_ratio: NUMBER(20,4)
        资本充足率   
    core_capi_ade_ratio: NUMBER(20,4)
        核心资本充足率   
    npl_ratio: NUMBER(20,4)
        不良贷款比例   
    loan_depo_ratio: NUMBER(20,4)
        存贷款比例   
    loan_depo_ratio_rmb: NUMBER(20,4)
        存贷款比例(人民币)   
    loan_depo_ratio_normb: NUMBER(20,4)
        存贷款比例(外币)   
    st_asset_liq_ratio_rmb: NUMBER(20,4)
        短期资产流动性比例(人民币)   
    st_asset_liq_ratio_normb: NUMBER(20,4)
        短期资产流动性比例(外币)   
    loan_from_banks_ratio: NUMBER(20,4)
        拆入资金比例   
    lend_to_banks_ratio: NUMBER(20,4)
        拆出资金比例   
    largest_customer_loan: NUMBER(20,4)
        单一客户贷款比例   
    top_ten_customer_loan: NUMBER(20,4)
        最大十家客户贷款比例   
    total_loan: NUMBER(20,4)
        贷款总额   
    total_deposit: NUMBER(20,4)
        存款总额   
    loan_loss_provision: NUMBER(20,4)
        贷款呆账准备金   
    bad_load_five_class: NUMBER(20,4)
        不良贷款余额(5级分类)   
    npl_provision_coverage: NUMBER(20,4)
        不良贷款拨备覆盖率   
    cost_income_ratio: NUMBER(20,4)
        成本收入比   
    non_interest_margin: NUMBER(20,4)
        非利息收入占比   
    net_capital: NUMBER(20,4)
        资本净额   
    core_capi_net_amount: NUMBER(20,4)
        核心资本净额   
    risk_weight_asset: NUMBER(20,4)
        加权风险资本净额   
    interest_bearing_asset: NUMBER(20,4)
        生息资产   
    interest_bearing_asset_comp: NUMBER(20,4)
        生息资产(计算值)   
    interest_bearing_lia: NUMBER(20,4)
        计息负债   
    interest_bearing_lia_comp: NUMBER(20,4)
        计息负债(计算值)   
    non_interest_income: NUMBER(20,4)
        非利息收入   
    noneaning_asset: NUMBER(20,4)
        非生息资产   
    noneaning_lia: NUMBER(20,4)
        非计息负债   
    net_interest_margin: NUMBER(20,4)
        净息差   
    net_interest_margin_is_ann: NUMBER(20,4)
        净息差是否公布值   
    net_interest_spread: NUMBER(20,4)
        净利差   
    net_interest_spread_is_ann: NUMBER(20,4)
        净利差是否公布值   
    overdue_loan: NUMBER(20,4)
        逾期贷款   
    total_interest_income: NUMBER(20,4)
        总利息收入   
    total_interest_exp: NUMBER(20,4)
        总利息支出   
    cash_on_hand: NUMBER(20,4)
        库存现金   
    longterm_loans_ratio_cny: NUMBER(20,4)
        中长期贷款比例(人民币)   
    longterm_loans_ratio_fc: NUMBER(20,4)
        中长期贷款比例(外币)   
    ibusiness_loan_ratio: NUMBER(20,4)
        国际商业借款比例   
    interect_collection_ratio: NUMBER(20,4)
        利息回收率   
    cash_reserve_ratio_cny: NUMBER(20,4)
        备付金比例(人民币)   
    cash_reserve_ratio_fc: NUMBER(20,4)
        备付金比例(外币)   
    overseas_funds_app_ratio: NUMBER(20,4)
        境外资金运用比例   
    market_risk_capital: NUMBER(20,4)
        市场风险资本   
    interest_bearing_asset_ifpub: NUMBER(1,0)
        生息资产是否是发布值   
    interest_bearing_lia_ifpub: NUMBER(1,0)
        计息负债是否是发布值   
    net_interest_margin_ifpub: NUMBER(1,0)
        净利差是否是发布值   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareBankIndicator"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    capi_ade_ratio = Column(NUMBER(20,4))
    core_capi_ade_ratio = Column(NUMBER(20,4))
    npl_ratio = Column(NUMBER(20,4))
    loan_depo_ratio = Column(NUMBER(20,4))
    loan_depo_ratio_rmb = Column(NUMBER(20,4))
    loan_depo_ratio_normb = Column(NUMBER(20,4))
    st_asset_liq_ratio_rmb = Column(NUMBER(20,4))
    st_asset_liq_ratio_normb = Column(NUMBER(20,4))
    loan_from_banks_ratio = Column(NUMBER(20,4))
    lend_to_banks_ratio = Column(NUMBER(20,4))
    largest_customer_loan = Column(NUMBER(20,4))
    top_ten_customer_loan = Column(NUMBER(20,4))
    total_loan = Column(NUMBER(20,4))
    total_deposit = Column(NUMBER(20,4))
    loan_loss_provision = Column(NUMBER(20,4))
    bad_load_five_class = Column(NUMBER(20,4))
    npl_provision_coverage = Column(NUMBER(20,4))
    cost_income_ratio = Column(NUMBER(20,4))
    non_interest_margin = Column(NUMBER(20,4))
    net_capital = Column(NUMBER(20,4))
    core_capi_net_amount = Column(NUMBER(20,4))
    risk_weight_asset = Column(NUMBER(20,4))
    interest_bearing_asset = Column(NUMBER(20,4))
    interest_bearing_asset_comp = Column(NUMBER(20,4))
    interest_bearing_lia = Column(NUMBER(20,4))
    interest_bearing_lia_comp = Column(NUMBER(20,4))
    non_interest_income = Column(NUMBER(20,4))
    noneaning_asset = Column(NUMBER(20,4))
    noneaning_lia = Column(NUMBER(20,4))
    net_interest_margin = Column(NUMBER(20,4))
    net_interest_margin_is_ann = Column(NUMBER(20,4))
    net_interest_spread = Column(NUMBER(20,4))
    net_interest_spread_is_ann = Column(NUMBER(20,4))
    overdue_loan = Column(NUMBER(20,4))
    total_interest_income = Column(NUMBER(20,4))
    total_interest_exp = Column(NUMBER(20,4))
    cash_on_hand = Column(NUMBER(20,4))
    longterm_loans_ratio_cny = Column(NUMBER(20,4))
    longterm_loans_ratio_fc = Column(NUMBER(20,4))
    ibusiness_loan_ratio = Column(NUMBER(20,4))
    interect_collection_ratio = Column(NUMBER(20,4))
    cash_reserve_ratio_cny = Column(NUMBER(20,4))
    cash_reserve_ratio_fc = Column(NUMBER(20,4))
    overseas_funds_app_ratio = Column(NUMBER(20,4))
    market_risk_capital = Column(NUMBER(20,4))
    interest_bearing_asset_ifpub = Column(NUMBER(1,0))
    interest_bearing_lia_ifpub = Column(NUMBER(1,0))
    net_interest_margin_ifpub = Column(NUMBER(1,0))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
