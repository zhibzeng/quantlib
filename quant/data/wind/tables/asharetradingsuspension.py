from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareTradingSuspension(BaseModel):
    """
    中国A股停复牌信息

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_dq_suspenddate: VARCHAR2(8)
        停牌日期   
    s_dq_suspendtype: NUMBER(9,0)
        停牌类型代码   停牌类型：444001000上午停牌444002000下午停牌444003000今起停牌444004000盘中停牌444007000停牌1小时444016000停牌一天
    s_dq_resumpdate: VARCHAR2(8)
        复牌日期   
    s_dq_changereason: VARCHAR2(400)
        停牌原因   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_dq_suspenddate = Column(VARCHAR2(8))
    s_dq_suspendtype = Column(NUMBER(9,0))
    s_dq_resumpdate = Column(VARCHAR2(8))
    s_dq_changereason = Column(VARCHAR2(400))
    
