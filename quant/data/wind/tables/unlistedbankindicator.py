from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class UnlistedBankIndicator(BaseModel):
    """
    非上市银行专用指标

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

    """
    object_id = Column(VARCHAR2(100))
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
    
