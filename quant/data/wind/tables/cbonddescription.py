from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


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

    """
    object_id = Column(VARCHAR2(100))
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
    
