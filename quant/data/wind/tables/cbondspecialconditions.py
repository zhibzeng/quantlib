from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondSpecialConditions(BaseModel):
    """
    中国债券特殊条款

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    b_info_provisiontype: VARCHAR2(100)
        条款类型   
    b_info_callbkorputbkprice: NUMBER(20,4)
        赎回价/回售价   元
    b_info_callbkorputbkdate: VARCHAR2(8)
        赎回/回售日期   
    b_info_redemporrepurcdate: VARCHAR2(8)
        赎回/回售告知截止日期   
    b_info_maturityembedded: VARCHAR2(40)
        含权期限说明   
    b_info_execmaturityembedded: NUMBER(20,4)
        行权期限   
    b_info_couponadj_max: NUMBER(20,4)
        票面利率调整上限   
    b_info_couponadj_min: NUMBER(20,4)
        票面利率调整下限   
    b_info_content: VARCHAR2(3000)
        条款内容   

    """
    __tablename__ = "CBondSpecialConditions"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    b_info_provisiontype = Column(VARCHAR2(100))
    b_info_callbkorputbkprice = Column(NUMBER(20,4))
    b_info_callbkorputbkdate = Column(VARCHAR2(8))
    b_info_redemporrepurcdate = Column(VARCHAR2(8))
    b_info_maturityembedded = Column(VARCHAR2(40))
    b_info_execmaturityembedded = Column(NUMBER(20,4))
    b_info_couponadj_max = Column(NUMBER(20,4))
    b_info_couponadj_min = Column(NUMBER(20,4))
    b_info_content = Column(VARCHAR2(3000))
    
