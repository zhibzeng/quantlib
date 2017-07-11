from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareCashFlow(BaseModel):
    """
    中国A股现金流量表

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
    statement_type: VARCHAR2(10)
        报表类型   报表类型:408001000:合并报表408002000:合并报告(单季度)408003000:合并报告(单季度调整)408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408007000:母公司报表(单季度)408008000:母公司报告(单季度调整)408009000:母公司报表(调整)408010000:母公司报表(更正前)
    crncy_code: VARCHAR2(10)
        货币代码   CNY
    cash_recp_sg_and_rs: NUMBER(20,4)
        销售商品、提供劳务收到的现金   
    recp_tax_rends: NUMBER(20,4)
        收到的税费返还   
    net_incr_dep_cob: NUMBER(20,4)
        客户存款和同业存放款项净增加额   
    net_incr_loans_central_bank: NUMBER(20,4)
        向中央银行借款净增加额   
    net_incr_fund_borr_ofi: NUMBER(20,4)
        向其他金融机构拆入资金净增加额   
    cash_recp_prem_orig_inco: NUMBER(20,4)
        收到原保险合同保费取得的现金   
    net_incr_insured_dep: NUMBER(20,4)
        保户储金净增加额   
    net_cash_received_reinsu_bus: NUMBER(20,4)
        收到再保业务现金净额   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    wind_code = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    cash_recp_sg_and_rs = Column(NUMBER(20,4))
    recp_tax_rends = Column(NUMBER(20,4))
    net_incr_dep_cob = Column(NUMBER(20,4))
    net_incr_loans_central_bank = Column(NUMBER(20,4))
    net_incr_fund_borr_ofi = Column(NUMBER(20,4))
    cash_recp_prem_orig_inco = Column(NUMBER(20,4))
    net_incr_insured_dep = Column(NUMBER(20,4))
    net_cash_received_reinsu_bus = Column(NUMBER(20,4))
    
