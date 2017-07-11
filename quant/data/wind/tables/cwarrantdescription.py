from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CwarrantDescription(BaseModel):
    """
    中国权证基本资料

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    windcode: VARCHAR2(40)
        Wind代码   
    underlyingwindcode: VARCHAR2(10)
        标的证券wind代码   
    callput: VARCHAR2(40)
        行权方式   欧式；美式；百慕大
    equitycovered: VARCHAR2(40)
        权证类型   认购权证;认沽权证
    issuer: VARCHAR2(200)
        发行人   
    issuer_type: VARCHAR2(200)
        发行方式   
    issuer_iponum: NUMBER(20,4)
        发行数量(万份)   
    issuernum: NUMBER(20,4)
        上市数量(万份)   
    inistrikeprice: NUMBER(20,4)
        初始行权价   
    inistrikeratio: NUMBER(20,4)
        初始行权比例   
    duration_days: NUMBER(20,4)
        存续期限(天)   
    duration_startdate: VARCHAR2(8)
        存续起始日期   
    duration_enddate: VARCHAR2(8)
        存续截止日期   
    issuedate: VARCHAR2(8)
        发行日期   
    issueprice: NUMBER(20,4)
        发行价格   
    crncy_code: VARCHAR2(10)
        货币代码   
    listeddate: VARCHAR2(8)
        上市日期   
    annissuedate: VARCHAR2(8)
        发行公告日   
    annlisteddate: VARCHAR2(8)
        上市公告日   
    settlementmethod: VARCHAR2(40)
        结算方式   证券给付；现金

    """
    object_id = Column(VARCHAR2(100))
    windcode = Column(VARCHAR2(40))
    underlyingwindcode = Column(VARCHAR2(10))
    callput = Column(VARCHAR2(40))
    equitycovered = Column(VARCHAR2(40))
    issuer = Column(VARCHAR2(200))
    issuer_type = Column(VARCHAR2(200))
    issuer_iponum = Column(NUMBER(20,4))
    issuernum = Column(NUMBER(20,4))
    inistrikeprice = Column(NUMBER(20,4))
    inistrikeratio = Column(NUMBER(20,4))
    duration_days = Column(NUMBER(20,4))
    duration_startdate = Column(VARCHAR2(8))
    duration_enddate = Column(VARCHAR2(8))
    issuedate = Column(VARCHAR2(8))
    issueprice = Column(NUMBER(20,4))
    crncy_code = Column(VARCHAR2(10))
    listeddate = Column(VARCHAR2(8))
    annissuedate = Column(VARCHAR2(8))
    annlisteddate = Column(VARCHAR2(8))
    settlementmethod = Column(VARCHAR2(40))
    
