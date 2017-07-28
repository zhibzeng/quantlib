from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CwarrantDescription(BaseModel):
    """
    4.190 中国权证基本资料

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
    exercisingend: VARCHAR2(8)
        最后行权日   
    exercode: VARCHAR2(10)
        行权代码   
    exername: VARCHAR2(40)
        行权简称   
    isratioadjust: NUMBER(5,0)
        行权价及行权比例是否调整   0：否；1：是
    adjustratio: VARCHAR2(800)
        行权价及比例调整公式   
    progress: VARCHAR2(8)
        方案进度   1：董事会预案2：股东大会通过3：实施12：停止实施
    prelan_date: VARCHAR2(8)
        预案公告日   
    smtg_date: VARCHAR2(8)
        股东大会公告日   
    typebyissuer: VARCHAR2(40)
        权证类型(按发行人分类)   股本权证；备兑权证
    old_shrhldr_ratio: NUMBER(20,4)
        原股东配售比例   
    placingrecorddate: VARCHAR2(8)
        权证配售股权登记日   
    offeringobject: VARCHAR2(40)
        发行对象   全体流通股东；全体股东；全体投资者
    guartype: VARCHAR2(40)
        担保方式   
    exercisestartdate: VARCHAR2(8)
        行权起始日期   
    ref_price: NUMBER(20,4)
        上市首日参考价   
    iscallclause: NUMBER(5,0)
        是否有约购条款   0：否；1：是
    callprice: NUMBER(20,4)
        回购价格   
    calldescription: VARCHAR2(500)
        回购说明   
    guarantor: VARCHAR2(300)
        担保人   
    guardescription: VARCHAR2(400)
        担保说明   
    warrantsource: VARCHAR2(40)
        权证来源   
    warrant_num_per_bond: NUMBER(20,4)
        每张债券附认股权证数量   
    bondwindcode: VARCHAR2(10)
        债券wind代码   
    lasttradedate: VARCHAR2(8)
        最后交易日   
    expiredate: VARCHAR2(8)
        停止交易日   
    recorddate_putwarrant: VARCHAR2(8)
        认沽权利股权登记日   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CwarrantDescription"
    object_id = Column(VARCHAR2(100), primary_key=True)
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
    exercisingend = Column(VARCHAR2(8))
    exercode = Column(VARCHAR2(10))
    exername = Column(VARCHAR2(40))
    isratioadjust = Column(NUMBER(5,0))
    adjustratio = Column(VARCHAR2(800))
    progress = Column(VARCHAR2(8))
    prelan_date = Column(VARCHAR2(8))
    smtg_date = Column(VARCHAR2(8))
    typebyissuer = Column(VARCHAR2(40))
    old_shrhldr_ratio = Column(NUMBER(20,4))
    placingrecorddate = Column(VARCHAR2(8))
    offeringobject = Column(VARCHAR2(40))
    guartype = Column(VARCHAR2(40))
    exercisestartdate = Column(VARCHAR2(8))
    ref_price = Column(NUMBER(20,4))
    iscallclause = Column(NUMBER(5,0))
    callprice = Column(NUMBER(20,4))
    calldescription = Column(VARCHAR2(500))
    guarantor = Column(VARCHAR2(300))
    guardescription = Column(VARCHAR2(400))
    warrantsource = Column(VARCHAR2(40))
    warrant_num_per_bond = Column(NUMBER(20,4))
    bondwindcode = Column(VARCHAR2(10))
    lasttradedate = Column(VARCHAR2(8))
    expiredate = Column(VARCHAR2(8))
    recorddate_putwarrant = Column(VARCHAR2(8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
