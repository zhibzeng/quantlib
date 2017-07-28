from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareholdersmeeting(BaseModel):
    """
    4.101 中国A股召开股东大会

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
        投票通道代码   241001000深圳证券交易所交易系统241002000上海证券交易所交易系统241003000中国证券登记结算有限责任公司网络系统
    smtgrecdate: VARCHAR2(8)
        股东大会股权登记日   
    spotmtgstartdate: VARCHAR2(8)
        会议登记起始日   
    spotmtgenddate: VARCHAR2(8)
        会议登记截止日   
    is_intnet: VARCHAR2(1)
        是否可以网络投票   
    intnetcode: VARCHAR2(10)
        网络投票代码   最近一次网络投票代码
    intnetname: VARCHAR2(20)
        网络投票简称   最近一次网络投票简称
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareholdersmeeting"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    meeting_dt = Column(VARCHAR2(8))
    meeting_type = Column(VARCHAR2(20))
    votingcode = Column(NUMBER(9,0))
    smtgrecdate = Column(VARCHAR2(8))
    spotmtgstartdate = Column(VARCHAR2(8))
    spotmtgenddate = Column(VARCHAR2(8))
    is_intnet = Column(VARCHAR2(1))
    intnetcode = Column(VARCHAR2(10))
    intnetname = Column(VARCHAR2(20))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
