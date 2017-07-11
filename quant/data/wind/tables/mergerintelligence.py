from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class MergerIntelligence(BaseModel):
    """
    前瞻性情报

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    intelligence_id: VARCHAR2(20)
        情报ID   
    title: VARCHAR2(400)
        标题   
    ann_date: VARCHAR2(8)
        公告日期   
    involved_amount: VARCHAR2(1000)
        涉及金额   
    subject_typecode: NUMBER(9，0)
        主题分类代码   
    wind_ind_code: VARCHAR2(10)
        所属Wind行业代码   
    level_code: NUMBER(9，0)
        情报等级代码   
    key_words: VARCHAR2(100)
        情报关键字   
    data_source: VARCHAR2(200)
        来源名称   
    involved_equity: VARCHAR2(200)
        涉及股权   
    content: VARCHAR2(3000)
        正文内容   
    event_id: VARCHAR2(20)
        交易事件ID   
    progress_code: NUMBER(9，0)
        事件进度代码   
    receipt_date: DATE
        收录时间   
    is_important: NUMBER(1，0)
        是否重要   
    effective_date: VARCHAR2(8)
        生效日期   

    """
    __tablename__ = "MergerIntelligence"
    object_id = Column(VARCHAR2(100), primary_key=True)
    intelligence_id = Column(VARCHAR2(20))
    title = Column(VARCHAR2(400))
    ann_date = Column(VARCHAR2(8))
    involved_amount = Column(VARCHAR2(1000))
    subject_typecode = Column(NUMBER(9，0))
    wind_ind_code = Column(VARCHAR2(10))
    level_code = Column(NUMBER(9，0))
    key_words = Column(VARCHAR2(100))
    data_source = Column(VARCHAR2(200))
    involved_equity = Column(VARCHAR2(200))
    content = Column(VARCHAR2(3000))
    event_id = Column(VARCHAR2(20))
    progress_code = Column(NUMBER(9，0))
    receipt_date = Column(DATE)
    is_important = Column(NUMBER(1，0))
    effective_date = Column(VARCHAR2(8))
    
