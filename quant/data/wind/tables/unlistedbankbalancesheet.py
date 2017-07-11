from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class UnlistedBankBalanceSheet(BaseModel):
    """
    非上市银行资产负债表

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
        报表类型   报表类型:408001000:合并报表408004000:合并报表(调整)408005000:合并报表(更正前)408050000:合并调整(更正前)408006000:母公司报表408009000:母公司报表(调整)408010000:母公司报表(更正前)408060000:母公司调整(更正前)
    crncy_code: VARCHAR2(10)
        货币代码   CNY
    actual_ann_dt: VARCHAR2(8)
        实际公告日期   
    cash_deposits_central_bank: NUMBER(20,4)
        现金及存放中央银行款项   
    asset_dep_oth_banks_fin_inst: NUMBER(20,4)
        存放同业和其它金融机构款项   
    precious_metals: NUMBER(20,4)
        贵金属   
    loans_to_oth_banks: NUMBER(20,4)
        拆出资金   
    tradable_fin_assets: NUMBER(20,4)
        交易性金融资产   
    derivative_fin_assets: NUMBER(20,4)
        衍生金融资产   
    red_monetary_cap_for_sale: NUMBER(20,4)
        买入返售金融资产   
    int_rcv: NUMBER(20,4)
        应收利息   
    loans_and_adv_granted: NUMBER(20,4)
        发放贷款及垫款   
    agency_bus_assets: NUMBER(20,4)
        代理业务资产   
    fin_assets_avail_for_sale: NUMBER(20,4)
        可供出售金融资产   
    held_to_mty_invest: NUMBER(20,4)
        持有至到期投资   

    """
    object_id = Column(VARCHAR2(100))
    s_info_compcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    actual_ann_dt = Column(VARCHAR2(8))
    cash_deposits_central_bank = Column(NUMBER(20,4))
    asset_dep_oth_banks_fin_inst = Column(NUMBER(20,4))
    precious_metals = Column(NUMBER(20,4))
    loans_to_oth_banks = Column(NUMBER(20,4))
    tradable_fin_assets = Column(NUMBER(20,4))
    derivative_fin_assets = Column(NUMBER(20,4))
    red_monetary_cap_for_sale = Column(NUMBER(20,4))
    int_rcv = Column(NUMBER(20,4))
    loans_and_adv_granted = Column(NUMBER(20,4))
    agency_bus_assets = Column(NUMBER(20,4))
    fin_assets_avail_for_sale = Column(NUMBER(20,4))
    held_to_mty_invest = Column(NUMBER(20,4))
    
