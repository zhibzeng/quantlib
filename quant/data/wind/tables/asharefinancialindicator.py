from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareFinancialIndicator(BaseModel):
    """
    中国A股财务指标

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    wind_code: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    report_period: VARCHAR2(8)
        报告期   
    crncy_code: VARCHAR2(10)
        货币代码   默认为人民币
    s_fa_extraordinary: NUMBER(20,4)
        非经常性损益   
    s_fa_deductedprofit: NUMBER(20,4)
        扣除非经常性损益后的净利润   
    s_fa_grossmargin: NUMBER(20,4)
        毛利   
    s_fa_operateincome: NUMBER(20,4)
        经营活动净收益   
    s_fa_investincome: NUMBER(20,4)
        价值变动净收益   
    s_stmnote_finexp: NUMBER(20,4)
        利息费用   
    s_stm_is: NUMBER(20,4)
        折旧与摊销   
    s_fa_ebit: NUMBER(20,4)
        息税前利润   
    s_fa_ebitda: NUMBER(20,4)
        息税折旧摊销前利润   
    s_fa_fcff: NUMBER(20,4)
        企业自由现金流量(FCFF)   
    s_fa_fcfe: NUMBER(20,4)
        股权自由现金流量(FCFE)   
    s_fa_exinterestdebt_current: NUMBER(20,4)
        无息流动负债   
    s_fa_exinterestdebt_noncurrent: NUMBER(20,4)
        无息非流动负债   
    s_fa_interestdebt: NUMBER(20,4)
        带息债务   
    s_fa_netdebt: NUMBER(20,4)
        净债务   
    s_fa_tangibleasset: NUMBER(20,4)
        有形资产   
    s_fa_workingcapital: NUMBER(20,4)
        营运资金   
    s_fa_networkingcapital: NUMBER(20,4)
        营运流动资本   
    s_fa_investcapital: NUMBER(20,4)
        全部投入资本   
    s_fa_retainedearnings: NUMBER(20,4)
        留存收益   
    s_fa_eps_basic: NUMBER(20,4)
        基本每股收益   
    s_fa_eps_diluted: NUMBER(20,4)
        稀释每股收益   
    s_fa_eps_diluted2: NUMBER(20,4)
        期末摊薄每股收益   
    s_fa_bps: NUMBER(20,4)
        每股净资产   
    s_fa_ocfps: NUMBER(20,4)
        每股经营活动产生的现金流量净额   
    s_fa_grps: NUMBER(20,4)
        每股营业总收入   
    s_fa_orps: NUMBER(20,4)
        每股营业收入   
    s_fa_surpluscapitalps: NUMBER(20,4)
        每股资本公积   
    s_fa_surplusreserveps: NUMBER(20,4)
        每股盈余公积   
    s_fa_undistributedps: NUMBER(20,4)
        每股未分配利润   
    s_fa_retainedps: NUMBER(20,4)
        每股留存收益   
    s_fa_cfps: NUMBER(20,4)
        每股现金流量净额   
    s_fa_ebitps: NUMBER(20,4)
        每股息税前利润   
    s_fa_fcffps: NUMBER(20,4)
        每股企业自由现金流量   
    s_fa_fcfeps: NUMBER(20,4)
        每股股东自由现金流量   
    s_fa_netprofitmargin: NUMBER(20,4)
        销售净利率   
    s_fa_grossprofitmargin: NUMBER(20,4)
        销售毛利率   
    s_fa_cogstosales: NUMBER(20,4)
        销售成本率   
    s_fa_expensetosales: NUMBER(20,4)
        销售期间费用率   
    s_fa_profittogr: NUMBER(20,4)
        净利润/营业总收入   
    s_fa_saleexpensetogr: NUMBER(20,4)
        销售费用/营业总收入   
    s_fa_adminexpensetogr: NUMBER(20,4)
        管理费用/营业总收入   
    s_fa_finaexpensetogr: NUMBER(20,4)
        财务费用/营业总收入   
    s_fa_impairtogr_ttm: NUMBER(20,4)
        资产减值损失/营业总收入   
    s_fa_gctogr: NUMBER(20,4)
        营业总成本/营业总收   

    """
    __tablename__ = "AShareFinancialIndicator"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    wind_code = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    crncy_code = Column(VARCHAR2(10))
    s_fa_extraordinary = Column(NUMBER(20,4))
    s_fa_deductedprofit = Column(NUMBER(20,4))
    s_fa_grossmargin = Column(NUMBER(20,4))
    s_fa_operateincome = Column(NUMBER(20,4))
    s_fa_investincome = Column(NUMBER(20,4))
    s_stmnote_finexp = Column(NUMBER(20,4))
    s_stm_is = Column(NUMBER(20,4))
    s_fa_ebit = Column(NUMBER(20,4))
    s_fa_ebitda = Column(NUMBER(20,4))
    s_fa_fcff = Column(NUMBER(20,4))
    s_fa_fcfe = Column(NUMBER(20,4))
    s_fa_exinterestdebt_current = Column(NUMBER(20,4))
    s_fa_exinterestdebt_noncurrent = Column(NUMBER(20,4))
    s_fa_interestdebt = Column(NUMBER(20,4))
    s_fa_netdebt = Column(NUMBER(20,4))
    s_fa_tangibleasset = Column(NUMBER(20,4))
    s_fa_workingcapital = Column(NUMBER(20,4))
    s_fa_networkingcapital = Column(NUMBER(20,4))
    s_fa_investcapital = Column(NUMBER(20,4))
    s_fa_retainedearnings = Column(NUMBER(20,4))
    s_fa_eps_basic = Column(NUMBER(20,4))
    s_fa_eps_diluted = Column(NUMBER(20,4))
    s_fa_eps_diluted2 = Column(NUMBER(20,4))
    s_fa_bps = Column(NUMBER(20,4))
    s_fa_ocfps = Column(NUMBER(20,4))
    s_fa_grps = Column(NUMBER(20,4))
    s_fa_orps = Column(NUMBER(20,4))
    s_fa_surpluscapitalps = Column(NUMBER(20,4))
    s_fa_surplusreserveps = Column(NUMBER(20,4))
    s_fa_undistributedps = Column(NUMBER(20,4))
    s_fa_retainedps = Column(NUMBER(20,4))
    s_fa_cfps = Column(NUMBER(20,4))
    s_fa_ebitps = Column(NUMBER(20,4))
    s_fa_fcffps = Column(NUMBER(20,4))
    s_fa_fcfeps = Column(NUMBER(20,4))
    s_fa_netprofitmargin = Column(NUMBER(20,4))
    s_fa_grossprofitmargin = Column(NUMBER(20,4))
    s_fa_cogstosales = Column(NUMBER(20,4))
    s_fa_expensetosales = Column(NUMBER(20,4))
    s_fa_profittogr = Column(NUMBER(20,4))
    s_fa_saleexpensetogr = Column(NUMBER(20,4))
    s_fa_adminexpensetogr = Column(NUMBER(20,4))
    s_fa_finaexpensetogr = Column(NUMBER(20,4))
    s_fa_impairtogr_ttm = Column(NUMBER(20,4))
    s_fa_gctogr = Column(NUMBER(20,4))
    
