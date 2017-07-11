from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareIncExercisePct(BaseModel):
    """
    中国A股股权激励行权比例

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_inc_sequence: VARCHAR2(6)
        序号   
    s_inc_execbatch: VARCHAR2(6)
        行权期   
    s_inc_execpct: NUMBER(20,4)
        行权比例(%)   
    s_inc_intervaltime: NUMBER(20,4)
        首个授权日至行权期间隔时间(月)   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_inc_sequence = Column(VARCHAR2(6))
    s_inc_execbatch = Column(VARCHAR2(6))
    s_inc_execpct = Column(NUMBER(20,4))
    s_inc_intervaltime = Column(NUMBER(20,4))
    
