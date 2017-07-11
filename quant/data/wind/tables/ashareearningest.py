from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareEarningEst(BaseModel):
    """
    中国A股盈利预测明细

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    wind_code: VARCHAR2(40)
        Wind代码   
    research_inst_name: VARCHAR2(20)
        研究机构名称   
    analyst_name: VARCHAR2(20)
        分析师名称   
    est_dt: VARCHAR2(8)
        预测日期   
    reporting_period: VARCHAR2(8)
        预测报告期   
    est_eps_diluted: NUMBER(20,4)
        预测每股收益(摊薄)(元)   
    est_net_profit: NUMBER(20,4)
        预测净利润(万元)   
    est_main_bus_inc: NUMBER(20,4)
        预测主营业务收入(万元)   
    est_ebit: NUMBER(20,4)
        预测息税前利润(万元)   
    est_ebitda: NUMBER(20,4)
        预测息税折旧摊销前利润(万元)   
    est_base_cap: NUMBER(20,4)
        预测基准股本(万股)   
    ann_dt: VARCHAR2(8)
        公告日期(内部)   记录了盈利预测信息到达万得平台的时间，该字段精确到”日”，未保存具体的时点。
    s_est_cps: NUMBER(20,4)
        预测每股现金流   
    s_est_dps: NUMBER(20,4)
        预测每股股利   
    s_est_bps: NUMBER(20,4)
        预测每股净资产   
    s_est_ebt: NUMBER(20,4)
        预测利润总额(万元)   
    s_est_roa: NUMBER(20,4)
        预测总资产收益率   
    s_est_roe: NUMBER(20,4)
        预测净资产收益率   
    s_est_oprofit: NUMBER(20,4)
        预测营业利润(万元)   
    s_est_epsdiluted: NUMBER(20,4)
        预测每股收益(稀释)(元)   
    s_est_epsbasic: NUMBER(20,4)
        预测每股收益(基本)(元)   
    s_est_oc: NUMBER(20,4)
        预测营业成本及附加(万元)   
    s_est_npcal: NUMBER(20,4)
        预测净利润(换算)(万元)   
    s_est_epscal: NUMBER(20,4)
        预测每股收益(换算)   
    s_est_nprate: NUMBER(20,4)
        预测净利润调整比率   
    s_est_epsrate: NUMBER(20,4)
        预测EPS调整比率   
    s_est_pe: NUMBER(20,4)
        预测市盈率   
    s_est_pb: NUMBER(20,4)
        预测市净率   
    s_est_evebitda: NUMBER(20,4)
        预测EV/EBITDA   
    s_est_dividendyield: NUMBER(20,4)
        预测股息率   
    s_est_enddate: VARCHAR2(8)
        预测有效截止   
    s_est_ope: NUMBER(20,4)
        预测主营业务利润率   

    """
    __tablename__ = "AShareEarningEst"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    wind_code = Column(VARCHAR2(40))
    research_inst_name = Column(VARCHAR2(20))
    analyst_name = Column(VARCHAR2(20))
    est_dt = Column(VARCHAR2(8))
    reporting_period = Column(VARCHAR2(8))
    est_eps_diluted = Column(NUMBER(20,4))
    est_net_profit = Column(NUMBER(20,4))
    est_main_bus_inc = Column(NUMBER(20,4))
    est_ebit = Column(NUMBER(20,4))
    est_ebitda = Column(NUMBER(20,4))
    est_base_cap = Column(NUMBER(20,4))
    ann_dt = Column(VARCHAR2(8))
    s_est_cps = Column(NUMBER(20,4))
    s_est_dps = Column(NUMBER(20,4))
    s_est_bps = Column(NUMBER(20,4))
    s_est_ebt = Column(NUMBER(20,4))
    s_est_roa = Column(NUMBER(20,4))
    s_est_roe = Column(NUMBER(20,4))
    s_est_oprofit = Column(NUMBER(20,4))
    s_est_epsdiluted = Column(NUMBER(20,4))
    s_est_epsbasic = Column(NUMBER(20,4))
    s_est_oc = Column(NUMBER(20,4))
    s_est_npcal = Column(NUMBER(20,4))
    s_est_epscal = Column(NUMBER(20,4))
    s_est_nprate = Column(NUMBER(20,4))
    s_est_epsrate = Column(NUMBER(20,4))
    s_est_pe = Column(NUMBER(20,4))
    s_est_pb = Column(NUMBER(20,4))
    s_est_evebitda = Column(NUMBER(20,4))
    s_est_dividendyield = Column(NUMBER(20,4))
    s_est_enddate = Column(VARCHAR2(8))
    s_est_ope = Column(NUMBER(20,4))
    
