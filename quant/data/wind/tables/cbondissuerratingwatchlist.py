from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondIssuerRatingWatchlist(BaseModel):
    """
    债券主体信用评级观察名单明细

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    b_subject_id: VARCHAR2(40)
        公司ID   
    s_info_compname: VARCHAR2(100)
        公司名称   
    ann_dt: NUMBER(9,0)
        公告日期   
    b_event_hapdate: NUMBER(9,0)
        发生日期   
    b_event_categorycode: NUMBER(9,0)
        事件类型代码   
    b_event_category: VARCHAR2(80)
        事件类型名称   
    b_event_title: VARCHAR2(200)
        事件标题   
    b_ann_abstract: VARCHAR2(3000)
        公告摘要   

    """
    object_id = Column(VARCHAR2(100))
    b_subject_id = Column(VARCHAR2(40))
    s_info_compname = Column(VARCHAR2(100))
    ann_dt = Column(NUMBER(9,0))
    b_event_hapdate = Column(NUMBER(9,0))
    b_event_categorycode = Column(NUMBER(9,0))
    b_event_category = Column(VARCHAR2(80))
    b_event_title = Column(VARCHAR2(200))
    b_ann_abstract = Column(VARCHAR2(3000))
    
