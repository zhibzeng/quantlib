from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CBondTender(BaseModel):
    """
    中国债券招标

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    b_tender_tenderdate: VARCHAR2(8)
        招投标日期   
    b_tender_method: NUMBER(9,0)
        招标方式   529001000荷兰式529002000美国式529003000混合式529004000簿记建档
    b_tender_object: NUMBER(9,0)
        招标标的   530001000利率530002000利差530003000价格530004000数量
    b_tender_amountplan: NUMBER(20,4)
        计划招标总额   
    b_tender_cmptamnt: NUMBER(20,4)
        竞争性招标总额   竞争性招标总额=计划发行总额-基本承销额度
    b_tender_underwriting: NUMBER(20,4)
        基本承销额度   
    b_tender_additiverights: VARCHAR2(200)
        基本承销额增加权利   
    b_tender_addratio: NUMBER(20,4)
        基本承销额追加比例(%)   
    b_tender_threshold: NUMBER(20,4)
        投标价位下限   利率招标为利率下限、价格招标为价格下限、利差招标为利差下限
    b_tender_ceiling: NUMBER(20,4)
        投标价位上限   利率招标为利率上限、价格招标为价格上限、利差招标为利差上限
    b_tender_tenderunit: NUMBER(20,4)
        基本投标单位   
    b_tender_lowestamnt: NUMBER(20,4)
        每标位最低投标量   
    b_tender_highestamnt: NUMBER(20,4)
        每标位最高投标量   
    b_tender_paymentdate: VARCHAR2(40)
        缴款日期   
    b_tender_confirmdate: VARCHAR2(8)
        资金到账确认时间   
    b_tender_transferdate: VARCHAR2(8)
        债券过户时间   
    b_tender_distribbegin: VARCHAR2(8)
        分销起始日期   
    b_tender_distribend: VARCHAR2(8)
        分销截止日期   
    b_tender_underwritingcost: NUMBER(20,4)
        承揽费率(%)   
    b_tender_spread: VARCHAR2(20)
        标位步长   
    b_tender_concatenationornot: NUMBER(1,0)
        是否要求标位连续   1是；0否

    """
    __tablename__ = "CBondTender"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    b_tender_tenderdate = Column(VARCHAR2(8))
    b_tender_method = Column(NUMBER(9,0))
    b_tender_object = Column(NUMBER(9,0))
    b_tender_amountplan = Column(NUMBER(20,4))
    b_tender_cmptamnt = Column(NUMBER(20,4))
    b_tender_underwriting = Column(NUMBER(20,4))
    b_tender_additiverights = Column(VARCHAR2(200))
    b_tender_addratio = Column(NUMBER(20,4))
    b_tender_threshold = Column(NUMBER(20,4))
    b_tender_ceiling = Column(NUMBER(20,4))
    b_tender_tenderunit = Column(NUMBER(20,4))
    b_tender_lowestamnt = Column(NUMBER(20,4))
    b_tender_highestamnt = Column(NUMBER(20,4))
    b_tender_paymentdate = Column(VARCHAR2(40))
    b_tender_confirmdate = Column(VARCHAR2(8))
    b_tender_transferdate = Column(VARCHAR2(8))
    b_tender_distribbegin = Column(VARCHAR2(8))
    b_tender_distribend = Column(VARCHAR2(8))
    b_tender_underwritingcost = Column(NUMBER(20,4))
    b_tender_spread = Column(VARCHAR2(20))
    b_tender_concatenationornot = Column(NUMBER(1,0))
    
