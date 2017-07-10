from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondBalanceSheet(BaseModel):
    """
    中国债券发行主体资产负债表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_compcode: VARCHAR2(40)
        公司ID   
    ann_dt: VARCHAR2(8)
        公告日期   
    report_period: VARCHAR2(8)
        报告期   
    statement_type: VARCHAR2(10)
        报表类型   报表类型:408001000:合并报表408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408009000:母公司报表(调整)408010000:母公司报表(更正前)
    crncy_code: VARCHAR2(10)
        货币代码   CNY
    monetary_cap: NUMBER(20,4)
        货币资金   
    tradable_fin_assets: NUMBER(20,4)
        交易性金融资产   
    notes_rcv: NUMBER(20,4)
        应收票据   
    acct_rcv: NUMBER(20,4)
        应收账款   
    oth_rcv: NUMBER(20,4)
        其他应收款   

    """
    object_id = Column(VARCHAR2(100))
    s_info_compcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    monetary_cap = Column(NUMBER(20,4))
    tradable_fin_assets = Column(NUMBER(20,4))
    notes_rcv = Column(NUMBER(20,4))
    acct_rcv = Column(NUMBER(20,4))
    oth_rcv = Column(NUMBER(20,4))
    
