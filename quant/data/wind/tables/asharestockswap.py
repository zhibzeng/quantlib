from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareStockSwap(BaseModel):
    """
    中国A股股票置换

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    transferer_windcode: VARCHAR2(40)
        换股方万得代码   
    transferer_name: VARCHAR2(40)
        换股方简称   
    progress: VARCHAR2(10)
        方案进度   
    targetcomp_windcode: VARCHAR2(40)
        标的方万得代码   
    targetcomp_name: VARCHAR2(40)
        标的方简称   
    transferer_conversionprice: NUMBER(20,4)
        换股方换股价   
    targetcomp_conversionprice: NUMBER(20,4)
        标的方换股价   
    conversionratio: NUMBER(20,8)
        换股比例   
    is_cashoption: NUMBER(5,0)
        是否有现金选择权   
    cashoption: NUMBER(20,4)
        现金选择权   
    cashoption_reportstartdate: VARCHAR2(8)
        现金选择权申报起始日   
    cashoption_reportenddate: VARCHAR2(8)
        现金选择权申报截止日   
    cashoption_applicationcode: VARCHAR2(10)
        现金选择权申请代码   
    cashoption_sharepurchaser: VARCHAR2(80)
        现金选择权股份购买方   
    cashoption_applicantname: VARCHAR2(40)
        现金选择权适用方简称   
    is_overalllisting: NUMBER(5,0)
        是否属于整体上市   
    prelandate: VARCHAR2(8)
        预案公告日   
    mtstartdate: VARCHAR2(8)
        股东大会召开日   
    smtgrecdate: VARCHAR2(8)
        股东大会股权登记日   
    smtganncedate: VARCHAR2(8)
        股东大会公告日   
    iecannouncementdate: VARCHAR2(8)
        证监会发审委公告日   
    anncedate: VARCHAR2(8)
        实施公告日   
    anncelstdate: VARCHAR2(8)
        上市公告日   
    ann_dt: VARCHAR2(8)
        最新公告日   
    traderesumptiondate: VARCHAR2(8)
        预案公布后复牌日   
    lasttradedate: VARCHAR2(8)
        实施前最后交易日   
    equityregistrationdate: VARCHAR2(8)
        换股股权登记日   
    listdate: VARCHAR2(8)
        上市日   
    consolidationbasedate: VARCHAR2(8)
        合并基准日   
    financialadvisor: VARCHAR2(80)
        财务顾问   
    plandescription: VARCHAR2(300)
        方案说明   
    casharrivaldate: VARCHAR2(8)
        现金选择权现金到账日   
    effectivereportedshares: NUMBER(20,4)
        现金选择权有效申报股数   

    """
    __tablename__ = "AShareStockSwap"
    object_id = Column(VARCHAR2(100), primary_key=True)
    transferer_windcode = Column(VARCHAR2(40))
    transferer_name = Column(VARCHAR2(40))
    progress = Column(VARCHAR2(10))
    targetcomp_windcode = Column(VARCHAR2(40))
    targetcomp_name = Column(VARCHAR2(40))
    transferer_conversionprice = Column(NUMBER(20,4))
    targetcomp_conversionprice = Column(NUMBER(20,4))
    conversionratio = Column(NUMBER(20,8))
    is_cashoption = Column(NUMBER(5,0))
    cashoption = Column(NUMBER(20,4))
    cashoption_reportstartdate = Column(VARCHAR2(8))
    cashoption_reportenddate = Column(VARCHAR2(8))
    cashoption_applicationcode = Column(VARCHAR2(10))
    cashoption_sharepurchaser = Column(VARCHAR2(80))
    cashoption_applicantname = Column(VARCHAR2(40))
    is_overalllisting = Column(NUMBER(5,0))
    prelandate = Column(VARCHAR2(8))
    mtstartdate = Column(VARCHAR2(8))
    smtgrecdate = Column(VARCHAR2(8))
    smtganncedate = Column(VARCHAR2(8))
    iecannouncementdate = Column(VARCHAR2(8))
    anncedate = Column(VARCHAR2(8))
    anncelstdate = Column(VARCHAR2(8))
    ann_dt = Column(VARCHAR2(8))
    traderesumptiondate = Column(VARCHAR2(8))
    lasttradedate = Column(VARCHAR2(8))
    equityregistrationdate = Column(VARCHAR2(8))
    listdate = Column(VARCHAR2(8))
    consolidationbasedate = Column(VARCHAR2(8))
    financialadvisor = Column(VARCHAR2(80))
    plandescription = Column(VARCHAR2(300))
    casharrivaldate = Column(VARCHAR2(8))
    effectivereportedshares = Column(NUMBER(20,4))
    
