from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareEquityPledgeInfo(BaseModel):
    """
    中国A股股权质押信息

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    s_pledge_bgdate: VARCHAR2(8)
        质押起始时间   
    s_pledge_enddate: VARCHAR2(8)
        质押结束时间   
    s_holder_name: VARCHAR2(200)
        股东名称   
    s_pledge_shares: NUMBER(20,4)
        质押数量(万股)   
    s_pledgor: VARCHAR2(200)
        质押方   
    s_discharge_date: VARCHAR2(8)
        解押日期   
    s_remark: VARCHAR2(1000)
        备注   

    """
    __tablename__ = "AShareEquityPledgeInfo"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    s_pledge_bgdate = Column(VARCHAR2(8))
    s_pledge_enddate = Column(VARCHAR2(8))
    s_holder_name = Column(VARCHAR2(200))
    s_pledge_shares = Column(NUMBER(20,4))
    s_pledgor = Column(VARCHAR2(200))
    s_discharge_date = Column(VARCHAR2(8))
    s_remark = Column(VARCHAR2(1000))
    
