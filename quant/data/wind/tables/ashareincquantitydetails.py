from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


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
    s_inc_quantity: NUMBER(20,4)
        数量(万股/万份)   
    s_inc_totalqtypct: NUMBER(20,4)
        占本次授予总数量比例(%)   
    ann_dt: VARCHAR2(8)
        公告日期   

    """
    __tablename__ = "AShareIncQuantityDetails"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_inc_sequence = Column(VARCHAR2(6))
    s_inc_name = Column(VARCHAR2(80))
    s_inc_post = Column(VARCHAR2(80))
    s_inc_quantity = Column(NUMBER(20,4))
    s_inc_totalqtypct = Column(NUMBER(20,4))
    ann_dt = Column(VARCHAR2(8))
    
