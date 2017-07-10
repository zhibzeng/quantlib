from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareIPO(BaseModel):
    """
    中国A股首次公开发行数据

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

    """
    object_id = Column(VARCHAR2(100))
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
    
