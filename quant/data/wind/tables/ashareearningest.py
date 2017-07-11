from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


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

    """
    object_id = Column(VARCHAR2(100))
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
    
