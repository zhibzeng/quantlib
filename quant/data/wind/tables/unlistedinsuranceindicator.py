from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class UnlistedinsuranceIndicator(BaseModel):
    """
    非上市保险专用指标

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
    statement_type: NUMBER(9,0)
        报表类型   报表类型:408001000:合并报表408002000:合并报告(单季度)408003000:合并报告(单季度调整)408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408007000:母公司报表(单季度)408008000:母公司报告(单季度调整)408009000:母公司报表(调整)408010000:母公司报表(更正前)
    cap_adequacy_ratio_life: NUMBER(20,4)
        寿险：偿付能力充足率   
    cap_adequacy_ratio_property: NUMBER(20,4)
        产险：偿付能力充足率   
    surrender_rate: NUMBER(20,4)
        退保率   
    policy_persistency_rate_13m: NUMBER(20,4)
        保单继续率-13个月   
    policy_persistency_rate_25m: NUMBER(20,4)
        保单继续率-25个月   
    policy_persistency_rate_14m: NUMBER(20,4)
        保单继续率-14个月   
    policy_persistency_rate_26m: NUMBER(20,4)
        保单继续率-26个月   
    net_investment_yield: NUMBER(20,4)
        净投资收益率   
    total_investment_yield: NUMBER(20,4)
        总投资收益率   
    risk_discount_rate: NUMBER(20,4)
        评估利率假设：风险贴现率   
    combined_cost_property: NUMBER(20,4)
        产险：综合成本率   
    loss_ratio_property: NUMBER(20,4)
        产险：赔付率   
    fee_ratio_property: NUMBER(20,4)
        产险：费用率   
    intrinsic_value_life: NUMBER(20,4)
        寿险：内含价值   
    value_new_business_life: NUMBER(20,4)
        寿险：新业务价值   
    value_effective_business_life: NUMBER(20,4)
        寿险：有效业务价值   
    actual_capital_life: NUMBER(20,4)
        寿险：实际资本   
    minimun_capital_life: NUMBER(20,4)
        寿险：最低资本   
    actual_capital_property: NUMBER(20,4)
        产险：实际资本   
    minimun_capital_property: NUMBER(20,4)
        产险：最低资本   
    actual_capital_group: NUMBER(20,4)
        集团：实际资本   
    minimun_capital_group: NUMBER(20,4)
        集团：最低资本   
    capital_adequacy_ratio_group: NUMBER(20,4)
        集团：偿付能力充足率   
    crncy_code: VARCHAR2(10)
        货币代码   
    report_type: NUMBER(9,0)
        报告类型代码   

    """
    __tablename__ = "UnlistedinsuranceIndicator"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(NUMBER(9,0))
    cap_adequacy_ratio_life = Column(NUMBER(20,4))
    cap_adequacy_ratio_property = Column(NUMBER(20,4))
    surrender_rate = Column(NUMBER(20,4))
    policy_persistency_rate_13m = Column(NUMBER(20,4))
    policy_persistency_rate_25m = Column(NUMBER(20,4))
    policy_persistency_rate_14m = Column(NUMBER(20,4))
    policy_persistency_rate_26m = Column(NUMBER(20,4))
    net_investment_yield = Column(NUMBER(20,4))
    total_investment_yield = Column(NUMBER(20,4))
    risk_discount_rate = Column(NUMBER(20,4))
    combined_cost_property = Column(NUMBER(20,4))
    loss_ratio_property = Column(NUMBER(20,4))
    fee_ratio_property = Column(NUMBER(20,4))
    intrinsic_value_life = Column(NUMBER(20,4))
    value_new_business_life = Column(NUMBER(20,4))
    value_effective_business_life = Column(NUMBER(20,4))
    actual_capital_life = Column(NUMBER(20,4))
    minimun_capital_life = Column(NUMBER(20,4))
    actual_capital_property = Column(NUMBER(20,4))
    minimun_capital_property = Column(NUMBER(20,4))
    actual_capital_group = Column(NUMBER(20,4))
    minimun_capital_group = Column(NUMBER(20,4))
    capital_adequacy_ratio_group = Column(NUMBER(20,4))
    crncy_code = Column(VARCHAR2(10))
    report_type = Column(NUMBER(9,0))
    
