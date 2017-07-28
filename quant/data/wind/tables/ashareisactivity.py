from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AshareISActivity(BaseModel):
    """
    4.114 中国A股机构调研活动

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    event_id: VARCHAR2(40)
        事件ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_activitiestype: NUMBER(9,0)
        投资者关系活动类别代码   254001000:特定对象调研254002000:分析师会议254003000:媒体采访254004000:业绩说明会254005000:新闻发布会254006000:路演活动254007000:现场参观254008000:其他254009000:投资者接待日活动254010000:一对一沟通
    s_surveydate: VARCHAR2(8)
        调研日期   
    s_surveytime: VARCHAR2(20)
        调研具体时间   
    ann_dt: VARCHAR2(8)
        公告日期   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AshareISActivity"
    object_id = Column(VARCHAR2(100), primary_key=True)
    event_id = Column(VARCHAR2(40))
    s_info_windcode = Column(VARCHAR2(40))
    s_activitiestype = Column(NUMBER(9,0))
    s_surveydate = Column(VARCHAR2(8))
    s_surveytime = Column(VARCHAR2(20))
    ann_dt = Column(VARCHAR2(8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
