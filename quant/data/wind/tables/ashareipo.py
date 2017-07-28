from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareIPO(BaseModel):
    """
    4.17 中国A股首次公开发行数据

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    crncy_code: VARCHAR2(10)
        货币代码   
    s_ipo_price: NUMBER(20,4)
        发行价格(元)   网上申购价格
    s_ipo_pre_dilutedpe: NUMBER(20,4)
        发行市盈率(发行前股本)   
    s_ipo_dilutedpe: NUMBER(20,4)
        发行市盈率(发行后股本)   
    s_ipo_amount: NUMBER(20,4)
        发行数量(万股)   
    s_ipo_amtbyplacing: NUMBER(20,4)
        网上发行数量(万股)   
    s_ipo_amttojur: NUMBER(20,4)
        网下发行数量(万股)   
    s_ipo_collection: NUMBER(20,4)
        募集资金(万元)   含发行费用
    s_ipo_cashratio: NUMBER(20,8)
        网上发行中签率(%)   
    s_ipo_purchasecode: VARCHAR2(10)
        网上申购代码   
    s_ipo_subdate: VARCHAR2(8)
        申购日   
    s_ipo_jurisdate: VARCHAR2(8)
        向一般法人配售上市日期   网下机构首次限售上次
    s_ipo_instisdate: VARCHAR2(8)
        向战略投资者配售部分上市日期   
    s_ipo_expectlistdate: VARCHAR2(8)
        预计上市日期   
    s_ipo_fundverificationdate: VARCHAR2(8)
        申购资金验资日   
    s_ipo_ratiodate: VARCHAR2(8)
        中签率公布日   
    s_fellow_unfrozedate: VARCHAR2(8)
        申购资金解冻日   
    s_ipo_listdate: VARCHAR2(8)
        上市日   
    s_ipo_puboffrdate: VARCHAR2(8)
        招股公告日   
    s_ipo_anncedate: VARCHAR2(8)
        发行公告日   
    s_ipo_anncelstdate: VARCHAR2(8)
        上市公告日   
    s_ipo_roadshowstartdate: VARCHAR2(8)
        初步询价(预路演)起始日期   
    s_ipo_roadshowenddate: VARCHAR2(8)
        初步询价(预路演)终止日期   
    s_ipo_placingdate: VARCHAR2(8)
        网下配售发行公告日   
    s_ipo_applystartdate: VARCHAR2(8)
        网下申购起始日期   
    s_ipo_applyenddate: VARCHAR2(8)
        网下申购截止日期   
    s_ipo_priceannouncedate: VARCHAR2(8)
        网下定价公告日   
    s_ipo_placingresultdate: VARCHAR2(8)
        网下配售结果公告日   
    s_ipo_fundenddate: VARCHAR2(8)
        网下申购资金到帐截止日   
    s_ipo_capverificationdate: VARCHAR2(8)
        网下验资日   
    s_ipo_refunddate: VARCHAR2(8)
        网下多余款项退还日   
    s_ipo_expectedcollection: NUMBER(20,4)
        预计募集资金(万元)   
    s_ipo_list_fee: NUMBER(20,4)
        发行费用(万元)   
    s_ipo_namebyplacing: NUMBER(20,4)
        上网发行简称   
    s_ipo_showpricedownlimit: NUMBER(20,4)
        投标询价申购价格下限   
    s_ipo_par: NUMBER(20,4)
        面值   
    s_ipo_purchaseuplimit: NUMBER(20,4)
        网上申购上限(个人)   
    s_ipo_op_uplimit: NUMBER(20,4)
        网下申购上限   
    s_ipo_op_downlimit: NUMBER(20,4)
        网下申购下限   
    s_ipo_purchasemv_dt: VARCHAR2(8)
        网上市值申购登记日   
    s_ipo_pubosdtotisscoll: NUMBER(20,4)
        公开及原股东募集资金总额   
    s_ipo_osdexpoffamount: NUMBER(20,4)
        原股东预计售股数量   
    s_ipo_osdexpoffamountup: NUMBER(20,4)
        原股东预计售股数量上限   
    s_ipo_osdactoffamount: NUMBER(20,4)
        原股东实际售股数量   
    s_ipo_osdactoffprice: NUMBER(20,4)
        原股东实际售股金额   
    s_ipo_osdunderwritingfees: NUMBER(20,4)
        原股东应摊承销费用   
    s_ipo_pureffsubratio: NUMBER(20,4)
        网上投资者有效认购倍数   
    s_ipo_reporate: NUMBER(20,4)
        回拨比例   网下往网上是正的, 网上往网下是负的, 占本次发行数量合计的比例
    ann_dt: VARCHAR2(8)
        最新公告日期   
    is_failure: NUMBER(5,0)
        是否发行失败   0:发行正常;1:发行失败;2:发行暂缓
    s_ipo_otc_cash_pct: NUMBER(24,8)
        网下申购配售比例   网下中签率
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareIPO"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    crncy_code = Column(VARCHAR2(10))
    s_ipo_price = Column(NUMBER(20,4))
    s_ipo_pre_dilutedpe = Column(NUMBER(20,4))
    s_ipo_dilutedpe = Column(NUMBER(20,4))
    s_ipo_amount = Column(NUMBER(20,4))
    s_ipo_amtbyplacing = Column(NUMBER(20,4))
    s_ipo_amttojur = Column(NUMBER(20,4))
    s_ipo_collection = Column(NUMBER(20,4))
    s_ipo_cashratio = Column(NUMBER(20,8))
    s_ipo_purchasecode = Column(VARCHAR2(10))
    s_ipo_subdate = Column(VARCHAR2(8))
    s_ipo_jurisdate = Column(VARCHAR2(8))
    s_ipo_instisdate = Column(VARCHAR2(8))
    s_ipo_expectlistdate = Column(VARCHAR2(8))
    s_ipo_fundverificationdate = Column(VARCHAR2(8))
    s_ipo_ratiodate = Column(VARCHAR2(8))
    s_fellow_unfrozedate = Column(VARCHAR2(8))
    s_ipo_listdate = Column(VARCHAR2(8))
    s_ipo_puboffrdate = Column(VARCHAR2(8))
    s_ipo_anncedate = Column(VARCHAR2(8))
    s_ipo_anncelstdate = Column(VARCHAR2(8))
    s_ipo_roadshowstartdate = Column(VARCHAR2(8))
    s_ipo_roadshowenddate = Column(VARCHAR2(8))
    s_ipo_placingdate = Column(VARCHAR2(8))
    s_ipo_applystartdate = Column(VARCHAR2(8))
    s_ipo_applyenddate = Column(VARCHAR2(8))
    s_ipo_priceannouncedate = Column(VARCHAR2(8))
    s_ipo_placingresultdate = Column(VARCHAR2(8))
    s_ipo_fundenddate = Column(VARCHAR2(8))
    s_ipo_capverificationdate = Column(VARCHAR2(8))
    s_ipo_refunddate = Column(VARCHAR2(8))
    s_ipo_expectedcollection = Column(NUMBER(20,4))
    s_ipo_list_fee = Column(NUMBER(20,4))
    s_ipo_namebyplacing = Column(NUMBER(20,4))
    s_ipo_showpricedownlimit = Column(NUMBER(20,4))
    s_ipo_par = Column(NUMBER(20,4))
    s_ipo_purchaseuplimit = Column(NUMBER(20,4))
    s_ipo_op_uplimit = Column(NUMBER(20,4))
    s_ipo_op_downlimit = Column(NUMBER(20,4))
    s_ipo_purchasemv_dt = Column(VARCHAR2(8))
    s_ipo_pubosdtotisscoll = Column(NUMBER(20,4))
    s_ipo_osdexpoffamount = Column(NUMBER(20,4))
    s_ipo_osdexpoffamountup = Column(NUMBER(20,4))
    s_ipo_osdactoffamount = Column(NUMBER(20,4))
    s_ipo_osdactoffprice = Column(NUMBER(20,4))
    s_ipo_osdunderwritingfees = Column(NUMBER(20,4))
    s_ipo_pureffsubratio = Column(NUMBER(20,4))
    s_ipo_reporate = Column(NUMBER(20,4))
    ann_dt = Column(VARCHAR2(8))
    is_failure = Column(NUMBER(5,0))
    s_ipo_otc_cash_pct = Column(NUMBER(24,8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
