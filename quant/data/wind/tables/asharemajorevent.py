from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareMajorEvent(BaseModel):
    """
    中国A股重大事件表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_event_categorycode: NUMBER(9,0)
        事件类型代码   代码与内容的对应见附表“事件类型代码表”对应:类型编码表中的原始类型代码
    s_event_anncedate: VARCHAR2(8)
        披露日期   
    s_event_hapdate: VARCHAR2(8)
        发生日期   
    s_event_expdate: VARCHAR2(8)
        失效日期   
    s_event_content: VARCHAR2(4000)
        事件说明   
    s_event_templateid: NUMBER(12,0)
        模板ID   

    """
    __tablename__ = "AShareMajorEvent"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_event_categorycode = Column(NUMBER(9,0))
    s_event_anncedate = Column(VARCHAR2(8))
    s_event_hapdate = Column(VARCHAR2(8))
    s_event_expdate = Column(VARCHAR2(8))
    s_event_content = Column(VARCHAR2(4000))
    s_event_templateid = Column(NUMBER(12,0))
    
