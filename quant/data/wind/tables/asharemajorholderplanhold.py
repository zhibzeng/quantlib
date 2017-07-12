from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareMajorHolderPlanHold(BaseModel):
    """
    中国A股大股东增持计划

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_holder_name: VARCHAR2(200)
        股东名称   
    s_ph_startdate: VARCHAR2(8)
        增持计划起始日期   
    s_ph_enddate: VARCHAR2(8)
        增持计划截止日期   
    s_ph_conditionornot: NUMBER(5,0)
        是否无条件增持   1是；0否
    s_ph_triggerprice: NUMBER(20,4)
        增持触发价格   
    s_ph_continuousdays: NUMBER(5,0)
        连续天数   
    s_ph_calculatedays: NUMBER(5,0)
        计算天数   
    s_ph_calculatepricemode: VARCHAR2(80)
        价格计算方式   
    s_ph_sharenumdownlimit: NUMBER(20,4)
        增持股数下限(万股)   
    s_ph_sharenumuplimit: NUMBER(20,4)
        增持股数上限(万股)   
    s_ph_intendputmoneydownlimit: NUMBER(20,4)
        拟投入金额下限(亿元)   
    s_ph_intendputmoneyuplimit: NUMBER(20,4)
        拟投入金额上限(亿元)   
    s_ph_priceuplimit: NUMBER(20,4)
        增持价格上限   

    """
    __tablename__ = "AShareMajorHolderPlanHold"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_holder_name = Column(VARCHAR2(200))
    s_ph_startdate = Column(VARCHAR2(8))
    s_ph_enddate = Column(VARCHAR2(8))
    s_ph_conditionornot = Column(NUMBER(5,0))
    s_ph_triggerprice = Column(NUMBER(20,4))
    s_ph_continuousdays = Column(NUMBER(5,0))
    s_ph_calculatedays = Column(NUMBER(5,0))
    s_ph_calculatepricemode = Column(VARCHAR2(80))
    s_ph_sharenumdownlimit = Column(NUMBER(20,4))
    s_ph_sharenumuplimit = Column(NUMBER(20,4))
    s_ph_intendputmoneydownlimit = Column(NUMBER(20,4))
    s_ph_intendputmoneyuplimit = Column(NUMBER(20,4))
    s_ph_priceuplimit = Column(NUMBER(20,4))
    
