from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareLeadUnderwriter(BaseModel):
    """
    中国A股发行主承销商

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_lu_annissuedate: VARCHAR2(8)
        发行公告日   
    s_lu_issuedate: VARCHAR2(8)
        发行日期   
    s_lu_issuetype: VARCHAR2(1)
        发行类型   1.首发

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_lu_annissuedate = Column(VARCHAR2(8))
    s_lu_issuedate = Column(VARCHAR2(8))
    s_lu_issuetype = Column(VARCHAR2(1))
    
