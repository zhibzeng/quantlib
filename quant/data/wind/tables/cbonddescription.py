from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondDescription(BaseModel):
    """
    中国债券基本资料

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    b_info_fullname: VARCHAR2(100)
        债券名称   
    b_info_issuer: VARCHAR2(100)
        发行人   
    b_issue_announcement: VARCHAR2(8)
        发行公告日   
    b_issue_firstissue: VARCHAR2(8)
        发行起始日   
    b_issue_lastissue: VARCHAR2(8)
        发行截止日   
    b_issue_amountplan: NUMBER(20,4)
        计划发行总量(亿元)   
    b_issue_amountact: NUMBER(20,4)
        实际发行总量(亿元)   
    b_info_issueprice: NUMBER(20,4)
        发行价格   
    b_info_par: NUMBER(20,0)
        面值   
    b_info_couponrate: NUMBER(20,4)
        发行票面利率(%)   
    b_info_spread: NUMBER(20,4)
        利差(%)   
    b_info_carrydate: VARCHAR2(8)
        计息起始日   
    b_info_enddate: VARCHAR2(8)
        计息截止日   
    b_info_maturitydate: VARCHAR2(8)
        到期日   
    b_info_term_year_: NUMBER(20,4)
        债券期限(年)   
    b_info_term_day_: NUMBER(20,4)
        债券期限(天)   
    b_info_paymentdate: VARCHAR2(8)
        兑付日   
    b_info_paymenttype: NUMBER(9,0)
        计息方式   502001000单利502002000复利
    b_info_interestfrequency: VARCHAR2(20)
        付息频率   M1按月付息M3按季付息M6半年付息Y1按年付息
    b_info_form: VARCHAR2(10)
        债券形式   1记账式2凭证式3实物券
    b_info_coupon: NUMBER(9,0)
        息票品种   505001000附息505002000零息505003000贴现
    b_info_interesttype: NUMBER(9,0)
        附息利率品种   501001000浮动利率501002000固定利率501003000累进利率
    b_info_act: NUMBER(20,4)
        特殊年计息天数   
    b_issue_fee: NUMBER(20,4)
        发行手续费率(%)   
    b_redemption_feeration: NUMBER(20,4)
        兑付手续费率(%)   
    b_info_taxrate: NUMBER(20,4)
        所得税率   
    crncy_code: VARCHAR2(10)
        货币代码   
    s_info_name: VARCHAR2(50)
        债券简称   
    s_info_exchmarket: VARCHAR2(10)
        交易所   SSE:上交所SZSE:深交所NIB:银行间债券NBC:银行柜台债券
    b_info_guarantor: VARCHAR2(100)
        担保人   
    b_info_guartype: NUMBER(9,0)
        担保方式   507002000不可撤销连带责任担保507003000抵押担保507006000豁免担保507007000连带责任担保507012000质押担保507013000质押担保及抵押担保
    b_info_listdate: VARCHAR2(8)
        上市日期   
    b_info_yearsnumber: NUMBER(20,0)
        年内序号   
    s_div_recorddate: VARCHAR2(8)
        兑付登记起始日   
    b_info_codebyplacing: VARCHAR2(10)
        上网发行认购代码   
    b_info_delistdate: VARCHAR2(8)
        退市日期   
    b_info_issuetype: NUMBER(9,0)
        发行方式   439002000：包销团包销439004000：比例配售439006000：定向439010000：公开发行439012000：公募439019000：平价发行439022000：上网定价439025000：上网定价和网下配售439030000：私募439032000：贴现发行439033000：网上发行439037000：网下发行439045000：优先配售, 定向配售和网上定价439047000：优先配售, 网上定价和网下配售439048000：优先配售, 网下配售439049000：优先配售和上网定价
    b_info_guarintroduction: VARCHAR2(100)
        担保简介   
    b_info_bgndbyplacing: VARCHAR2(8)
        上网发行起始日期   
    b_info_enddbyplacing: VARCHAR2(8)
        上网发行截止日期   
    b_info_amountbyplacing: NUMBER(20,4)
        上网发行数量(亿元)   
    b_info_underwritingcode: NUMBER(9,0)
        承销方式代码   438001000:代销438002000:全额包销438003000:全额包销,代销438004000:余额包销438005000:余额包销,代销438006000:限额包销
    b_info_issuercode: VARCHAR2(100)
        发行人编号   万得自编公司ID
    b_info_formercode: VARCHAR2(40)
        原债券代码   针对增发和续发债
    b_info_coupontxt: VARCHAR2(1000)
        利率说明   
    is_failure: NUMBER(5,0)
        是否发行失败   0：正常发行1：发行失败(包括未能达到最低募集资金额以及停止发行)
    is_crossmarket: NUMBER(5,0)
        是否跨市场   
    b_info_coupondatetxt: VARCHAR2(1000)
        付息日说明   
    b_info_subordinateornot: NUMBER(5,0)
        是否次级债或混合资本债   1：次级债2:混合资本债
    b_tendrst_referyield: NUMBER(20,4)
        参考收益率   
    b_info_curpar: NUMBER(20,4)
        最新面值   
    s_info_formerwindcode: VARCHAR2(40)
        原Wind代码   
    is_corporate_bond: NUMBER(5,0)
        是否公司债   0：否1：是
    b_info_issuertype: VARCHAR2(40)
        发行人类型   发行人类型包括：财政部城市商业银行地方政府股份制商业银行国际机构国有商业银行其它金融机构企业证券公司政策性银行中国人民银行
    b_info_specialbondtype: VARCHAR2(40)
        特殊债券类型   特殊债券类型包括：地方政府债短期融资券公司债可分离转债可转债央行票据中期票据
    is_payadvanced: VARCHAR2(1)
        是否可提前兑付   0:否1：是
    is_callable: VARCHAR2(1)
        是否可赎回   0:否1：是
    is_chooseright: VARCHAR2(1)
        是否有选择权   0:否1：是

    """
    __tablename__ = "CBondDescription"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    b_info_fullname = Column(VARCHAR2(100))
    b_info_issuer = Column(VARCHAR2(100))
    b_issue_announcement = Column(VARCHAR2(8))
    b_issue_firstissue = Column(VARCHAR2(8))
    b_issue_lastissue = Column(VARCHAR2(8))
    b_issue_amountplan = Column(NUMBER(20,4))
    b_issue_amountact = Column(NUMBER(20,4))
    b_info_issueprice = Column(NUMBER(20,4))
    b_info_par = Column(NUMBER(20,0))
    b_info_couponrate = Column(NUMBER(20,4))
    b_info_spread = Column(NUMBER(20,4))
    b_info_carrydate = Column(VARCHAR2(8))
    b_info_enddate = Column(VARCHAR2(8))
    b_info_maturitydate = Column(VARCHAR2(8))
    b_info_term_year_ = Column(NUMBER(20,4))
    b_info_term_day_ = Column(NUMBER(20,4))
    b_info_paymentdate = Column(VARCHAR2(8))
    b_info_paymenttype = Column(NUMBER(9,0))
    b_info_interestfrequency = Column(VARCHAR2(20))
    b_info_form = Column(VARCHAR2(10))
    b_info_coupon = Column(NUMBER(9,0))
    b_info_interesttype = Column(NUMBER(9,0))
    b_info_act = Column(NUMBER(20,4))
    b_issue_fee = Column(NUMBER(20,4))
    b_redemption_feeration = Column(NUMBER(20,4))
    b_info_taxrate = Column(NUMBER(20,4))
    crncy_code = Column(VARCHAR2(10))
    s_info_name = Column(VARCHAR2(50))
    s_info_exchmarket = Column(VARCHAR2(10))
    b_info_guarantor = Column(VARCHAR2(100))
    b_info_guartype = Column(NUMBER(9,0))
    b_info_listdate = Column(VARCHAR2(8))
    b_info_yearsnumber = Column(NUMBER(20,0))
    s_div_recorddate = Column(VARCHAR2(8))
    b_info_codebyplacing = Column(VARCHAR2(10))
    b_info_delistdate = Column(VARCHAR2(8))
    b_info_issuetype = Column(NUMBER(9,0))
    b_info_guarintroduction = Column(VARCHAR2(100))
    b_info_bgndbyplacing = Column(VARCHAR2(8))
    b_info_enddbyplacing = Column(VARCHAR2(8))
    b_info_amountbyplacing = Column(NUMBER(20,4))
    b_info_underwritingcode = Column(NUMBER(9,0))
    b_info_issuercode = Column(VARCHAR2(100))
    b_info_formercode = Column(VARCHAR2(40))
    b_info_coupontxt = Column(VARCHAR2(1000))
    is_failure = Column(NUMBER(5,0))
    is_crossmarket = Column(NUMBER(5,0))
    b_info_coupondatetxt = Column(VARCHAR2(1000))
    b_info_subordinateornot = Column(NUMBER(5,0))
    b_tendrst_referyield = Column(NUMBER(20,4))
    b_info_curpar = Column(NUMBER(20,4))
    s_info_formerwindcode = Column(VARCHAR2(40))
    is_corporate_bond = Column(NUMBER(5,0))
    b_info_issuertype = Column(VARCHAR2(40))
    b_info_specialbondtype = Column(VARCHAR2(40))
    is_payadvanced = Column(VARCHAR2(1))
    is_callable = Column(VARCHAR2(1))
    is_chooseright = Column(VARCHAR2(1))
    
