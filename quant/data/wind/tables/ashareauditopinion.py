from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareAuditOpinion(BaseModel):
    """
    中国A股审计意见

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    report_period: VARCHAR2(8)
        报告期   
    s_stmnote_audit_category: NUMBER(9,0)
        审计结果类别代码   405001000:标准无保留意见405002000:带强调事项段的无保留意见405010000:基本不保留意见405003000:保留意见405004000:否定意见405005000:无法表示意见
    s_stmnote_audit_agency: VARCHAR2(100)
        会计师事务所   境内
    s_stmnote_audit_cpa: VARCHAR2(100)
        签字会计师   

    """
    __tablename__ = "AShareAuditOpinion"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    s_stmnote_audit_category = Column(NUMBER(9,0))
    s_stmnote_audit_agency = Column(VARCHAR2(100))
    s_stmnote_audit_cpa = Column(VARCHAR2(100))
    
