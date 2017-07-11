from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareMjrHolderTrade(BaseModel):
    """
    中国A股重要股东增减持

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   数据来源：上市公司公告
    ann_dt: VARCHAR2(8)
        公告日期   
    transact_startdate: VARCHAR2(8)
        变动起始日期   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    transact_startdate = Column(VARCHAR2(8))
    
