from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareStockRatingConsus(BaseModel):
    """
    中国A股投资评级汇总

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    rating_dt: VARCHAR2(8)
        日期   
    s_wrating_avg: NUMBER(20,4)
        综合评级   
    s_wrating_instnum: NUMBER(20,4)
        评级机构数量   
    s_wrating_upgrade: NUMBER(20,4)
        调高家数(相比一月前)   
    s_wrating_downgrade: NUMBER(20,4)
        调低家数(相比一月前)   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    rating_dt = Column(VARCHAR2(8))
    s_wrating_avg = Column(NUMBER(20,4))
    s_wrating_instnum = Column(NUMBER(20,4))
    s_wrating_upgrade = Column(NUMBER(20,4))
    s_wrating_downgrade = Column(NUMBER(20,4))
    
