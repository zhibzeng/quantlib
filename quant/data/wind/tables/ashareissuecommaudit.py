from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareIssueCommAudit(BaseModel):
    """
    4.11 中国A股发行审核一览

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_companyname: VARCHAR2(100)
        公司名称   
    s_ic_year: VARCHAR2(4)
        年度   
    s_ic_sessiontimes: VARCHAR2(3)
        会议届次   
    s_ic_audittype: VARCHAR2(40)
        审核类型   
    s_ic_type: NUMBER(9)
        发审委类型   203001000:发行审核委员会203002000:并购重组审核委员会203003000:创业板发行审核委员会
    s_ic_announcementdate: VARCHAR2(8)
        会议公告日期   
    s_ic_date: VARCHAR2(8)
        会议日期   
    s_ic_auditocetype: VARCHAR2(1)
        审核结果类型   1.待表决2.取消审核3.通过4.未通过5.暂缓表决
    s_ic_auditannocedate: VARCHAR2(8)
        审核结果公告日期   
    s_info_expectedissueshares: NUMBER(20,4)
        预计发行股数(万股)   
    s_info_expectedcollection: NUMBER(20,4)
        预计募集资金(万元)   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareIssueCommAudit"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_companyname = Column(VARCHAR2(100))
    s_ic_year = Column(VARCHAR2(4))
    s_ic_sessiontimes = Column(VARCHAR2(3))
    s_ic_audittype = Column(VARCHAR2(40))
    s_ic_type = Column(NUMBER(9))
    s_ic_announcementdate = Column(VARCHAR2(8))
    s_ic_date = Column(VARCHAR2(8))
    s_ic_auditocetype = Column(VARCHAR2(1))
    s_ic_auditannocedate = Column(VARCHAR2(8))
    s_info_expectedissueshares = Column(NUMBER(20,4))
    s_info_expectedcollection = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
