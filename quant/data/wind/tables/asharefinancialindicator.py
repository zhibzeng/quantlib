from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareFinancialIndicator(BaseModel):
    """
    4.48 中国A股财务指标

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
        营业总成本/营业总收入   
    s_fa_optogr: NUMBER(20,4)
        营业利润/营业总收入   
    s_fa_ebittogr: NUMBER(20,4)
        息税前利润/营业总收入   
    s_fa_roe: NUMBER(20,4)
        净资产收益率   
    s_fa_roe_deducted: NUMBER(20,4)
        净资产收益率(扣除非经常损益)   
    s_fa_roa2: NUMBER(20,4)
        总资产报酬率   
    s_fa_roa: NUMBER(20,4)
        总资产净利润   
    s_fa_roic: NUMBER(20,4)
        投入资本回报率   
    s_fa_roe_yearly: NUMBER(20,4)
        年化净资产收益率   
    s_fa_roa2_yearly: NUMBER(20,4)
        年化总资产报酬率   
    s_fa_roe_avg: NUMBER(20,4)
        平均净资产收益率(增发条件)   
    s_fa_operateincometoebt: NUMBER(20,4)
        经营活动净收益/利润总额   
    s_fa_investincometoebt: NUMBER(20,4)
        价值变动净收益/利润总额   
    s_fa_nonoperateprofittoebt: NUMBER(20,4)
        营业外收支净额/利润总额   
    s_fa_taxtoebt: NUMBER(20,4)
        所得税/利润总额   
    s_fa_deductedprofittoprofit: NUMBER(20,4)
        扣除非经常损益后的净利润/净利润   
    s_fa_salescashintoor: NUMBER(20,4)
        销售商品提供劳务收到的现金/营业收入   
    s_fa_ocftoor: NUMBER(20,4)
        经营活动产生的现金流量净额/营业收入   
    s_fa_ocftooperateincome: NUMBER(20,4)
        经营活动产生的现金流量净额/经营活动净收益   
    s_fa_capitalizedtoda: NUMBER(20,4)
        资本支出/折旧和摊销   
    s_fa_debttoassets: NUMBER(20,4)
        资产负债率   
    s_fa_assetstoequity: NUMBER(20,4)
        权益乘数   
    s_fa_dupont_assetstoequity: NUMBER(20,4)
        权益乘数(用于杜邦分析)   
    s_fa_catoassets: NUMBER(20,4)
        流动资产/总资产   
    s_fa_ncatoassets: NUMBER(20,4)
        非流动资产/总资产   
    s_fa_tangibleassetstoassets: NUMBER(20,4)
        有形资产/总资产   
    s_fa_intdebttototalcap: NUMBER(20,4)
        带息债务/全部投入资本   
    s_fa_equitytototalcapital: NUMBER(20,4)
        归属于母公司的股东权益/全部投入资本   
    s_fa_currentdebttodebt: NUMBER(20,4)
        流动负债/负债合计   
    s_fa_longdebtodebt: NUMBER(20,4)
        非流动负债/负债合计   
    s_fa_current: NUMBER(20,4)
        流动比率   
    s_fa_quick: NUMBER(20,4)
        速动比率   
    s_fa_cashratio: NUMBER(20,4)
        保守速动比率   
    s_fa_ocftoshortdebt: NUMBER(20,4)
        经营活动产生的现金流量净额/流动负债   
    s_fa_debttoequity: NUMBER(20,4)
        产权比率   
    s_fa_equitytodebt: NUMBER(20,4)
        归属于母公司的股东权益/负债合计   
    s_fa_equitytointerestdebt: NUMBER(20,4)
        归属于母公司的股东权益/带息债务   
    s_fa_tangibleassettodebt: NUMBER(20,4)
        有形资产/负债合计   
    s_fa_tangassettointdebt: NUMBER(20,4)
        有形资产/带息债务   
    s_fa_tangibleassettonetdebt: NUMBER(20,4)
        有形资产/净债务   
    s_fa_ocftodebt: NUMBER(20,4)
        经营活动产生的现金流量净额/负债合计   
    s_fa_ocftointerestdebt: NUMBER(20,4)
        经营活动产生的现金流量净额/带息债务   
    s_fa_ocftonetdebt: NUMBER(20,4)
        经营活动产生的现金流量净额/净债务   
    s_fa_ebittointerest: NUMBER(20,4)
        已获利息倍数(EBIT/利息费用)   
    s_fa_longdebttoworkingcapital: NUMBER(20,4)
        长期债务与营运资金比率   
    s_fa_ebitdatodebt: NUMBER(20,4)
        息税折旧摊销前利润/负债合计   
    s_fa_turndays: NUMBER(20,4)
        营业周期   
    s_fa_invturndays: NUMBER(20,4)
        存货周转天数   
    s_fa_arturndays: NUMBER(20,4)
        应收账款周转天数   
    s_fa_invturn: NUMBER(20,4)
        存货周转率   
    s_fa_arturn: NUMBER(20,4)
        应收账款周转率   
    s_fa_caturn: NUMBER(20,4)
        流动资产周转率   
    s_fa_faturn: NUMBER(20,4)
        固定资产周转率   
    s_fa_assetsturn: NUMBER(20,4)
        总资产周转率   
    s_fa_roa_yearly: NUMBER(20,4)
        年化总资产净利率   
    s_fa_dupont_roa: NUMBER(20,4)
        总资产净利率(杜邦分析)   
    s_stm_bs: NUMBER(20,4)
        固定资产合计   
    s_fa_prefinexpense_opprofit: NUMBER(20,4)
        扣除财务费用前营业利润   
    s_fa_nonopprofit: NUMBER(20,4)
        非营业利润   
    s_fa_optoebt: NUMBER(20,4)
        营业利润／利润总额   
    s_fa_noptoebt: NUMBER(20,4)
        非营业利润／利润总额   
    s_fa_ocftoprofit: NUMBER(20,4)
        经营活动产生的现金流量净额／营业利润   
    s_fa_cashtoliqdebt: NUMBER(20,4)
        货币资金／流动负债   
    s_fa_cashtoliqdebtwithinterest: NUMBER(20,4)
        货币资金／带息流动负债   
    s_fa_optoliqdebt: NUMBER(20,4)
        营业利润／流动负债   
    s_fa_optodebt: NUMBER(20,4)
        营业利润／负债合计   
    s_fa_roic_yearly: NUMBER(20,4)
        年化投入资本回报率   
    s_fa_tot_faturn: NUMBER(20,4)
        固定资产合计周转率   
    s_fa_profittoop: NUMBER(20,4)
        利润总额／营业收入   
    s_qfa_operateincome: NUMBER(20,4)
        单季度.经营活动净收益   
    s_qfa_investincome: NUMBER(20,4)
        单季度.价值变动净收益   
    s_qfa_deductedprofit: NUMBER(20,4)
        单季度.扣除非经常损益后的净利润   
    s_qfa_eps: NUMBER(20,4)
        单季度.每股收益   
    s_qfa_netprofitmargin: NUMBER(20,4)
        单季度.销售净利率   
    s_qfa_grossprofitmargin: NUMBER(20,4)
        单季度.销售毛利率   
    s_qfa_expensetosales: NUMBER(20,4)
        单季度.销售期间费用率   
    s_qfa_profittogr: NUMBER(20,4)
        单季度.净利润／营业总收入   
    s_qfa_saleexpensetogr: NUMBER(20,4)
        单季度.销售费用／营业总收入   
    s_qfa_adminexpensetogr: NUMBER(20,4)
        单季度.管理费用／营业总收入   
    s_qfa_finaexpensetogr: NUMBER(20,4)
        单季度.财务费用／营业总收入   
    s_qfa_impairtogr_ttm: NUMBER(20,4)
        单季度.资产减值损失／营业总收入   
    s_qfa_gctogr: NUMBER(20,4)
        单季度.营业总成本／营业总收入   
    s_qfa_optogr: NUMBER(20,4)
        单季度.营业利润／营业总收入   
    s_qfa_roe: NUMBER(20,4)
        单季度.净资产收益率   
    s_qfa_roe_deducted: NUMBER(20,4)
        单季度.净资产收益率(扣除非经常损益)   
    s_qfa_roa: NUMBER(20,4)
        单季度.总资产净利润   
    s_qfa_operateincometoebt: NUMBER(20,4)
        单季度.经营活动净收益／利润总额   
    s_qfa_investincometoebt: NUMBER(20,4)
        单季度.价值变动净收益／利润总额   
    s_qfa_deductedprofittoprofit: NUMBER(20,4)
        单季度.扣除非经常损益后的净利润／净利润   
    s_qfa_salescashintoor: NUMBER(20,4)
        单季度.销售商品提供劳务收到的现金／营业收入   
    s_qfa_ocftosales: NUMBER(20,4)
        单季度.经营活动产生的现金流量净额／营业收入   
    s_qfa_ocftoor: NUMBER(20,4)
        单季度.经营活动产生的现金流量净额／经营活动净收益   
    s_fa_yoyeps_basic: NUMBER(20,4)
        同比增长率-基本每股收益(%)   
    s_fa_yoyeps_diluted: NUMBER(20,4)
        同比增长率-稀释每股收益(%)   
    s_fa_yoyocfps: NUMBER(20,4)
        同比增长率-每股经营活动产生的现金流量净额(%)   
    s_fa_yoyop: NUMBER(20,4)
        同比增长率-营业利润(%)   
    s_fa_yoyebt: NUMBER(20,4)
        同比增长率-利润总额(%)   
    s_fa_yoynetprofit: NUMBER(20,4)
        同比增长率-归属母公司股东的净利润(%)   
    s_fa_yoynetprofit_deducted: NUMBER(20,4)
        同比增长率-归属母公司股东的净利润-扣除非经常损益(%)   
    s_fa_yoyocf: NUMBER(20,4)
        同比增长率-经营活动产生的现金流量净额(%)   
    s_fa_yoyroe: NUMBER(20,4)
        同比增长率-净资产收益率(摊薄)(%)   
    s_fa_yoybps: NUMBER(20,4)
        相对年初增长率-每股净资产(%)   
    s_fa_yoyassets: NUMBER(20,4)
        相对年初增长率-资产总计(%)   
    s_fa_yoyequity: NUMBER(20,4)
        相对年初增长率-归属母公司的股东权益(%)   
    s_fa_yoy_tr: NUMBER(20,4)
        营业总收入同比增长率(%)   
    s_fa_yoy_or: NUMBER(20,4)
        营业收入同比增长率(%)   
    s_qfa_yoygr: NUMBER(20,4)
        单季度.营业总收入同比增长率(%)   
    s_qfa_cgrgr: NUMBER(20,4)
        单季度.营业总收入环比增长率(%)   
    s_qfa_yoysales: NUMBER(20,4)
        单季度.营业收入同比增长率(%)   
    s_qfa_cgrsales: NUMBER(20,4)
        单季度.营业收入环比增长率(%)   
    s_qfa_yoyop: NUMBER(20,4)
        单季度.营业利润同比增长率(%)   
    s_qfa_cgrop: NUMBER(20,4)
        单季度.营业利润环比增长率(%)   
    s_qfa_yoyprofit: NUMBER(20,4)
        单季度.净利润同比增长率(%)   
    s_qfa_cgrprofit: NUMBER(20,4)
        单季度.净利润环比增长率(%)   
    s_qfa_yoynetprofit: NUMBER(20,4)
        单季度.归属母公司股东的净利润同比增长率(%)   
    s_qfa_cgrnetprofit: NUMBER(20,4)
        单季度.归属母公司股东的净利润环比增长率(%)   
    s_fa_yoy_equity: NUMBER(20,4)
        净资产(同比增长率)   
    rd_expense: NUMBER(20, 4)
        研发费用   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

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
    s_fa_optogr = Column(NUMBER(20,4))
    s_fa_ebittogr = Column(NUMBER(20,4))
    s_fa_roe = Column(NUMBER(20,4))
    s_fa_roe_deducted = Column(NUMBER(20,4))
    s_fa_roa2 = Column(NUMBER(20,4))
    s_fa_roa = Column(NUMBER(20,4))
    s_fa_roic = Column(NUMBER(20,4))
    s_fa_roe_yearly = Column(NUMBER(20,4))
    s_fa_roa2_yearly = Column(NUMBER(20,4))
    s_fa_roe_avg = Column(NUMBER(20,4))
    s_fa_operateincometoebt = Column(NUMBER(20,4))
    s_fa_investincometoebt = Column(NUMBER(20,4))
    s_fa_nonoperateprofittoebt = Column(NUMBER(20,4))
    s_fa_taxtoebt = Column(NUMBER(20,4))
    s_fa_deductedprofittoprofit = Column(NUMBER(20,4))
    s_fa_salescashintoor = Column(NUMBER(20,4))
    s_fa_ocftoor = Column(NUMBER(20,4))
    s_fa_ocftooperateincome = Column(NUMBER(20,4))
    s_fa_capitalizedtoda = Column(NUMBER(20,4))
    s_fa_debttoassets = Column(NUMBER(20,4))
    s_fa_assetstoequity = Column(NUMBER(20,4))
    s_fa_dupont_assetstoequity = Column(NUMBER(20,4))
    s_fa_catoassets = Column(NUMBER(20,4))
    s_fa_ncatoassets = Column(NUMBER(20,4))
    s_fa_tangibleassetstoassets = Column(NUMBER(20,4))
    s_fa_intdebttototalcap = Column(NUMBER(20,4))
    s_fa_equitytototalcapital = Column(NUMBER(20,4))
    s_fa_currentdebttodebt = Column(NUMBER(20,4))
    s_fa_longdebtodebt = Column(NUMBER(20,4))
    s_fa_current = Column(NUMBER(20,4))
    s_fa_quick = Column(NUMBER(20,4))
    s_fa_cashratio = Column(NUMBER(20,4))
    s_fa_ocftoshortdebt = Column(NUMBER(20,4))
    s_fa_debttoequity = Column(NUMBER(20,4))
    s_fa_equitytodebt = Column(NUMBER(20,4))
    s_fa_equitytointerestdebt = Column(NUMBER(20,4))
    s_fa_tangibleassettodebt = Column(NUMBER(20,4))
    s_fa_tangassettointdebt = Column(NUMBER(20,4))
    s_fa_tangibleassettonetdebt = Column(NUMBER(20,4))
    s_fa_ocftodebt = Column(NUMBER(20,4))
    s_fa_ocftointerestdebt = Column(NUMBER(20,4))
    s_fa_ocftonetdebt = Column(NUMBER(20,4))
    s_fa_ebittointerest = Column(NUMBER(20,4))
    s_fa_longdebttoworkingcapital = Column(NUMBER(20,4))
    s_fa_ebitdatodebt = Column(NUMBER(20,4))
    s_fa_turndays = Column(NUMBER(20,4))
    s_fa_invturndays = Column(NUMBER(20,4))
    s_fa_arturndays = Column(NUMBER(20,4))
    s_fa_invturn = Column(NUMBER(20,4))
    s_fa_arturn = Column(NUMBER(20,4))
    s_fa_caturn = Column(NUMBER(20,4))
    s_fa_faturn = Column(NUMBER(20,4))
    s_fa_assetsturn = Column(NUMBER(20,4))
    s_fa_roa_yearly = Column(NUMBER(20,4))
    s_fa_dupont_roa = Column(NUMBER(20,4))
    s_stm_bs = Column(NUMBER(20,4))
    s_fa_prefinexpense_opprofit = Column(NUMBER(20,4))
    s_fa_nonopprofit = Column(NUMBER(20,4))
    s_fa_optoebt = Column(NUMBER(20,4))
    s_fa_noptoebt = Column(NUMBER(20,4))
    s_fa_ocftoprofit = Column(NUMBER(20,4))
    s_fa_cashtoliqdebt = Column(NUMBER(20,4))
    s_fa_cashtoliqdebtwithinterest = Column(NUMBER(20,4))
    s_fa_optoliqdebt = Column(NUMBER(20,4))
    s_fa_optodebt = Column(NUMBER(20,4))
    s_fa_roic_yearly = Column(NUMBER(20,4))
    s_fa_tot_faturn = Column(NUMBER(20,4))
    s_fa_profittoop = Column(NUMBER(20,4))
    s_qfa_operateincome = Column(NUMBER(20,4))
    s_qfa_investincome = Column(NUMBER(20,4))
    s_qfa_deductedprofit = Column(NUMBER(20,4))
    s_qfa_eps = Column(NUMBER(20,4))
    s_qfa_netprofitmargin = Column(NUMBER(20,4))
    s_qfa_grossprofitmargin = Column(NUMBER(20,4))
    s_qfa_expensetosales = Column(NUMBER(20,4))
    s_qfa_profittogr = Column(NUMBER(20,4))
    s_qfa_saleexpensetogr = Column(NUMBER(20,4))
    s_qfa_adminexpensetogr = Column(NUMBER(20,4))
    s_qfa_finaexpensetogr = Column(NUMBER(20,4))
    s_qfa_impairtogr_ttm = Column(NUMBER(20,4))
    s_qfa_gctogr = Column(NUMBER(20,4))
    s_qfa_optogr = Column(NUMBER(20,4))
    s_qfa_roe = Column(NUMBER(20,4))
    s_qfa_roe_deducted = Column(NUMBER(20,4))
    s_qfa_roa = Column(NUMBER(20,4))
    s_qfa_operateincometoebt = Column(NUMBER(20,4))
    s_qfa_investincometoebt = Column(NUMBER(20,4))
    s_qfa_deductedprofittoprofit = Column(NUMBER(20,4))
    s_qfa_salescashintoor = Column(NUMBER(20,4))
    s_qfa_ocftosales = Column(NUMBER(20,4))
    s_qfa_ocftoor = Column(NUMBER(20,4))
    s_fa_yoyeps_basic = Column(NUMBER(20,4))
    s_fa_yoyeps_diluted = Column(NUMBER(20,4))
    s_fa_yoyocfps = Column(NUMBER(20,4))
    s_fa_yoyop = Column(NUMBER(20,4))
    s_fa_yoyebt = Column(NUMBER(20,4))
    s_fa_yoynetprofit = Column(NUMBER(20,4))
    s_fa_yoynetprofit_deducted = Column(NUMBER(20,4))
    s_fa_yoyocf = Column(NUMBER(20,4))
    s_fa_yoyroe = Column(NUMBER(20,4))
    s_fa_yoybps = Column(NUMBER(20,4))
    s_fa_yoyassets = Column(NUMBER(20,4))
    s_fa_yoyequity = Column(NUMBER(20,4))
    s_fa_yoy_tr = Column(NUMBER(20,4))
    s_fa_yoy_or = Column(NUMBER(20,4))
    s_qfa_yoygr = Column(NUMBER(20,4))
    s_qfa_cgrgr = Column(NUMBER(20,4))
    s_qfa_yoysales = Column(NUMBER(20,4))
    s_qfa_cgrsales = Column(NUMBER(20,4))
    s_qfa_yoyop = Column(NUMBER(20,4))
    s_qfa_cgrop = Column(NUMBER(20,4))
    s_qfa_yoyprofit = Column(NUMBER(20,4))
    s_qfa_cgrprofit = Column(NUMBER(20,4))
    s_qfa_yoynetprofit = Column(NUMBER(20,4))
    s_qfa_cgrnetprofit = Column(NUMBER(20,4))
    s_fa_yoy_equity = Column(NUMBER(20,4))
    rd_expense = Column(NUMBER(20, 4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
