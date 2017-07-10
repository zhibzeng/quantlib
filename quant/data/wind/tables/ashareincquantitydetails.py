from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareIncQuantityDetails(BaseModel):
    """
    中国A股股权激励数量明细

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_inc_sequence: VARCHAR2(6)
        序号   
    s_inc_name: VARCHAR2(80)
        姓名   
    s_inc_post: VARCHAR2(80)
        职位   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_inc_sequence = Column(VARCHAR2(6))
    s_inc_name = Column(VARCHAR2(80))
    s_inc_post = Column(VARCHAR2(80))
    
