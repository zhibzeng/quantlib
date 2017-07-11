from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondRating(BaseModel):
    """
    中国债券信用评级

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    b_rate_style: VARCHAR2(100)
        评级类型   1长期信用评级2短期信用评级
    b_info_creditrating: VARCHAR2(40)
        信用评级   
    b_info_creditratingagency: VARCHAR2(10)
        评级机构代码   1标准普尔评级服务公司10云南省资信评估事务所11北京穆迪投资者服务有限

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    b_rate_style = Column(VARCHAR2(100))
    b_info_creditrating = Column(VARCHAR2(40))
    b_info_creditratingagency = Column(VARCHAR2(10))
    
