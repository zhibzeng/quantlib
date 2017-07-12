from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class UnlistedIBrokerIndicator(BaseModel):
    """
    非上市券商专用指标

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
    statement_type: VARCHAR2(40)
        报表类型   报表类型:408001000:合并报表408002000:合并报告(单季度)408003000:合并报告(单季度调整)408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408007000:母公司报表(单季度)408008000:母公司报告(单季度调整)408009000:母公司报表(调整)408010000:母公司报表(更正前)
    iflisted_data: NUMBER(5,0)
        是否上市后数据   
    net_capital: NUMBER(20,4)
        净资本   
    trusted_capital: NUMBER(20,4)
        受托资金   
    net_gearing_ratio: NUMBER(20,4)
        净资本负债率(%)   
    prop_equity_ratio: NUMBER(20,4)
        自营权益类证券比例   
    longterm_invest_ratio: NUMBER(20,4)
        长期投资比例   
    fixed_capital_ratio: NUMBER(20,4)
        固定资本比例   
    fee_business_ratio: NUMBER(20,4)
        营业费用率   
    total_capital_return: NUMBER(20,4)
        总资产收益率   
    net_capital_yield: NUMBER(20,4)
        净资本收益率   
    current_ratio: NUMBER(20,4)
        流动比率   
    asset_liability_ratio: NUMBER(20,4)
        资产负债率   
    asset_turnover_ratio: NUMBER(20,4)
        资产周转率   
    net_capital_return: NUMBER(20,4)
        净资产收益率   
    contingent_liability_ratio: NUMBER(20,4)
        或有负债(担保)比率   
    prop_securities: NUMBER(20,4)
        自营证券   
    treasury_bond: NUMBER(20,4)
        国债   
    investment_funds: NUMBER(20,4)
        投资基金   
    stocks: NUMBER(20,4)
        股票   
    convertible_bond: NUMBER(20,4)
        可转债   
    per_capita_profits: NUMBER(20,4)
        人均利润   
    net_cap_total_riskprov: NUMBER(20,4)
        净资本/各项风险准备之和   
    net_cap_net_assets: NUMBER(20,4)
        净资本/净资产   
    prop_equ_der_netcap: NUMBER(20,4)
        自营权益类证券及证券衍生品/净资本   
    prop_fixedincome_netcap: NUMBER(20,4)
        自营固定收益类证券/   

    """
    __tablename__ = "UnlistedIBrokerIndicator"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(40))
    iflisted_data = Column(NUMBER(5,0))
    net_capital = Column(NUMBER(20,4))
    trusted_capital = Column(NUMBER(20,4))
    net_gearing_ratio = Column(NUMBER(20,4))
    prop_equity_ratio = Column(NUMBER(20,4))
    longterm_invest_ratio = Column(NUMBER(20,4))
    fixed_capital_ratio = Column(NUMBER(20,4))
    fee_business_ratio = Column(NUMBER(20,4))
    total_capital_return = Column(NUMBER(20,4))
    net_capital_yield = Column(NUMBER(20,4))
    current_ratio = Column(NUMBER(20,4))
    asset_liability_ratio = Column(NUMBER(20,4))
    asset_turnover_ratio = Column(NUMBER(20,4))
    net_capital_return = Column(NUMBER(20,4))
    contingent_liability_ratio = Column(NUMBER(20,4))
    prop_securities = Column(NUMBER(20,4))
    treasury_bond = Column(NUMBER(20,4))
    investment_funds = Column(NUMBER(20,4))
    stocks = Column(NUMBER(20,4))
    convertible_bond = Column(NUMBER(20,4))
    per_capita_profits = Column(NUMBER(20,4))
    net_cap_total_riskprov = Column(NUMBER(20,4))
    net_cap_net_assets = Column(NUMBER(20,4))
    prop_equ_der_netcap = Column(NUMBER(20,4))
    prop_fixedincome_netcap = Column(NUMBER(20,4))
    
