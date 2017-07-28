from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareRestructuringEvents(BaseModel):
    """
    4.110 中国A股重大重组事件

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        万得代码   
    progress: NUMBER(9,0)
        重组进度   324003002董事会预案324003004股东大会通过324003005国资委批准324003006商务部批准324003007证监会受理324003008证监会批准324004000完成324005000失败324005002停止实施具体参考类型编码表
    event: VARCHAR2(200)
        重组事件   
    form: NUMBER(9,0)
        重组形式代码   328001000协议收购328002000要约收购328003000管理层收购328004000回购328005000股权划拨328006000二级市场收购(含产权交易所)328007000吸收合并328012000发行股份购买资产具体参考类型编码表
    purpose: NUMBER(9,0)
        重组目的代码   326001000行业整合326001001横向整合326001002垂直整合326001003业务转型具体参考类型编码表
    type: NUMBER(9,0)
        重组类型代码   287001000借壳上市287002000发股非借壳287003000非发股非借壳具体参考类型编码表
    trading_object: VARCHAR2(200)
        交易标的   
    trading_objectcode: NUMBER(9,0)
        交易标的类型   320001000股权320002000资产320003000股权,资产320004000非股权
    is_m_a: NUMBER(5,0)
        是否并购   1：是0:否
    is_imptrestructuring: NUMBER(5,0)
        是否重大资产重组   1：是0:否
    is_controlchanged: NUMBER(5,0)
        控制权是否变更   1：是0:否
    shares_traded: NUMBER(20,4)
        交易股份占比(%)   
    totalvaluedeals: NUMBER(20,4)
        交易总价值(万元)   
    buyertopaycash: NUMBER(20,4)
        买方支付现金(万元)   
    crncy_code: VARCHAR2(10)
        货币代码   
    paymentmethod: NUMBER(9,0)
        支付方式代码   430001000股权430002000股权+负债430003000股权+现金430004000股权+债权具体参考类型编码表
    injectedassetbooknet: NUMBER(20,4)
        注入资产净资产账面值(万元)   
    assetinjectedassessnet: NUMBER(20,4)
        注入资产净资产评估值(万元)   
    ultimateassessmethod: NUMBER(9,0)
        最后采用评估方法   231001000成本法231002000收益法231003000市场法231004000市场法, 成本法, 收益法具体参考类型编码表
    basedate: VARCHAR2(8)
        资产评估基准日   
    appreciationrate: NUMBER(20,4)
        增值率   
    indepfinaadviser: VARCHAR2(200)
        独立财务顾问   
    acquireradviser: VARCHAR2(200)
        购买方财务顾问   
    suspensiondate: VARCHAR2(8)
        重大资产重组停牌日   
    prelandate: VARCHAR2(8)
        预案公告日   
    smtganncedate: VARCHAR2(8)
        股东大会公告日   
    passdate: VARCHAR2(8)
        发审委通过公告日   
    approveddate: VARCHAR2(8)
        证监会核准公告日   
    seo_dt: VARCHAR2(8)
        增发公告日(交易完成日期)   
    ann_dt: VARCHAR2(8)
        最新公告日   
    institutionlisted_dt: VARCHAR2(8)
        向机构所持增发上市日期   
    orientationseo_dt: VARCHAR2(8)
        定增股份上市日期   
    issuevolume: NUMBER(20,4)
        增发发行数量(万元)   
    seo_price: NUMBER(20,4)
        增发价格(元)   
    seo_downprice: NUMBER(20,4)
        增发预案价下限(元)   
    base_dt_avgp_20_m: NUMBER(20,4)
        定价基准日前20日交易均价   
    base_dt: VARCHAR2(8)
        定价基准日   
    base_dt_type: VARCHAR2(10)
        定价基准日类型   1:董事会决议公告日2:董事会召开日3:发行公告日4:发行期首日5:股东大会决议公告日6:股东大会召开日7:其他
    estimatednetprofit: NUMBER(20,4)
        预测净利润(元)   
    forecastyear: VARCHAR2(10)
        预测年度   
    issuedsharesago_seo_m: NUMBER(20,4)
        重组实施前总股本(万股)   
    issuedsharesago_seo_a: NUMBER(20,4)
        重组实施后总股本(万股)   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareRestructuringEvents"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    progress = Column(NUMBER(9,0))
    event = Column(VARCHAR2(200))
    form = Column(NUMBER(9,0))
    purpose = Column(NUMBER(9,0))
    type = Column(NUMBER(9,0))
    trading_object = Column(VARCHAR2(200))
    trading_objectcode = Column(NUMBER(9,0))
    is_m_a = Column(NUMBER(5,0))
    is_imptrestructuring = Column(NUMBER(5,0))
    is_controlchanged = Column(NUMBER(5,0))
    shares_traded = Column(NUMBER(20,4))
    totalvaluedeals = Column(NUMBER(20,4))
    buyertopaycash = Column(NUMBER(20,4))
    crncy_code = Column(VARCHAR2(10))
    paymentmethod = Column(NUMBER(9,0))
    injectedassetbooknet = Column(NUMBER(20,4))
    assetinjectedassessnet = Column(NUMBER(20,4))
    ultimateassessmethod = Column(NUMBER(9,0))
    basedate = Column(VARCHAR2(8))
    appreciationrate = Column(NUMBER(20,4))
    indepfinaadviser = Column(VARCHAR2(200))
    acquireradviser = Column(VARCHAR2(200))
    suspensiondate = Column(VARCHAR2(8))
    prelandate = Column(VARCHAR2(8))
    smtganncedate = Column(VARCHAR2(8))
    passdate = Column(VARCHAR2(8))
    approveddate = Column(VARCHAR2(8))
    seo_dt = Column(VARCHAR2(8))
    ann_dt = Column(VARCHAR2(8))
    institutionlisted_dt = Column(VARCHAR2(8))
    orientationseo_dt = Column(VARCHAR2(8))
    issuevolume = Column(NUMBER(20,4))
    seo_price = Column(NUMBER(20,4))
    seo_downprice = Column(NUMBER(20,4))
    base_dt_avgp_20_m = Column(NUMBER(20,4))
    base_dt = Column(VARCHAR2(8))
    base_dt_type = Column(VARCHAR2(10))
    estimatednetprofit = Column(NUMBER(20,4))
    forecastyear = Column(VARCHAR2(10))
    issuedsharesago_seo_m = Column(NUMBER(20,4))
    issuedsharesago_seo_a = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
