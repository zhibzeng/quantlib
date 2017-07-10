from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondTenderresult(BaseModel):
    """
    中国债券招标结果

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    b_tender_object: NUMBER(9,0)
        招标标的   530001000利率530002000利差530003000价格530004000数量
    b_tendrst_documtnumber: VARCHAR2(80)
        招标书编号   
    b_tendrst_payamount: NUMBER(20,4)
        缴款总金额(元)   
    b_tendrst_amountad: NUMBER(20,4)
        追加发行总量(万元)   
    b_tendrst_underwriting: NUMBER(20,4)
        基本承购总额(万元)   
    b_tendrst_amountact: NUMBER(20,4)
        实际发行总额(万元)   
    b_tendrst_amnt: NUMBER(20,4)
        招标总量(万元)   
    b_tendrst_oughttender: NUMBER(20,4)
        应投家数   
    b_tendrst_investortendered: NUMBER(20,4)
        投标家数   
    b_tendrst_tenders: NUMBER(20,4)
        投标笔数   
    b_tendrst_effecttender: NUMBER(20,4)
        有效笔数   
    b_tendrst_ineffecttender: NUMBER(20,4)
        无效笔数   
    b_tendrst_effectamnt: NUMBER(20,4)
        有效投标总量(万元)   
    b_tendrst_hightest: NUMBER(20,4)
        最高投标价位   
    b_tendrst_lowest: NUMBER(20,4)
        最低投标价位   
    b_tendrst_winningamnt: NUMBER(20,4)
        中标总量(万元)   
    b_tendrst_winnerbidder: NUMBER(20,4)
        中标家数   
    b_tendrst_winningbidder: NUMBER(20,4)
        中标笔数   
    b_tendrst_privatetrade: NUMBER(20,4)
        自营中标总量(万元)   
    b_tendrst_hightprice: NUMBER(20,4)
        最高中标价位   
    b_tendrst_lowprice: NUMBER(20,4)
        最低中标价位   
    b_tendrst_margamnt: NUMBER(20,4)
        边际中标价位投标总量(万元)   
    b_tendrst_margwinbidder: NUMBER(20,4)
        边际中标价位中标总量(万元)   
    b_tendrst_finalprice: NUMBER(20,4)
        最终发行价格   
    b_tendrst_referyield: NUMBER(20,4)
        参考收益率(%)   
    b_tendrst_financoupon: NUMBER(20,4)
        最终票面利率(%)   
    b_tendrst_bidrate: NUMBER(20,4)
        全场中标利率(%)   
    b_tendrst_bidprice: NUMBER(20,4)
        全场中标价格(元)   
    b_tendrst_bidspread: NUMBER(20,4)
        全场中标利差(%)   
    s_ipo_ovrsubratio: NUMBER(20,4)
        超额认购倍数   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    b_tender_object = Column(NUMBER(9,0))
    b_tendrst_documtnumber = Column(VARCHAR2(80))
    b_tendrst_payamount = Column(NUMBER(20,4))
    b_tendrst_amountad = Column(NUMBER(20,4))
    b_tendrst_underwriting = Column(NUMBER(20,4))
    b_tendrst_amountact = Column(NUMBER(20,4))
    b_tendrst_amnt = Column(NUMBER(20,4))
    b_tendrst_oughttender = Column(NUMBER(20,4))
    b_tendrst_investortendered = Column(NUMBER(20,4))
    b_tendrst_tenders = Column(NUMBER(20,4))
    b_tendrst_effecttender = Column(NUMBER(20,4))
    b_tendrst_ineffecttender = Column(NUMBER(20,4))
    b_tendrst_effectamnt = Column(NUMBER(20,4))
    b_tendrst_hightest = Column(NUMBER(20,4))
    b_tendrst_lowest = Column(NUMBER(20,4))
    b_tendrst_winningamnt = Column(NUMBER(20,4))
    b_tendrst_winnerbidder = Column(NUMBER(20,4))
    b_tendrst_winningbidder = Column(NUMBER(20,4))
    b_tendrst_privatetrade = Column(NUMBER(20,4))
    b_tendrst_hightprice = Column(NUMBER(20,4))
    b_tendrst_lowprice = Column(NUMBER(20,4))
    b_tendrst_margamnt = Column(NUMBER(20,4))
    b_tendrst_margwinbidder = Column(NUMBER(20,4))
    b_tendrst_finalprice = Column(NUMBER(20,4))
    b_tendrst_referyield = Column(NUMBER(20,4))
    b_tendrst_financoupon = Column(NUMBER(20,4))
    b_tendrst_bidrate = Column(NUMBER(20,4))
    b_tendrst_bidprice = Column(NUMBER(20,4))
    b_tendrst_bidspread = Column(NUMBER(20,4))
    s_ipo_ovrsubratio = Column(NUMBER(20,4))
    
