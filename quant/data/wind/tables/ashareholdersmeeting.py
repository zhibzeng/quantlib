from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareholdersmeeting(BaseModel):
    """
    中国A股召开股东大会

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    meeting_dt: VARCHAR2(8)
        会议日期   
    meeting_type: VARCHAR2(20)
        会议类型   
    votingcode: NUMBER(9,0)
        投票通道代码   241001000深圳证券交易所交易系统241002000上海证券交易所交易系统241003000中国证券登记结算有限责任公司网络系

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    meeting_dt = Column(VARCHAR2(8))
    meeting_type = Column(VARCHAR2(20))
    votingcode = Column(NUMBER(9,0))
    
