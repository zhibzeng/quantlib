from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareIncExecQtyPri(BaseModel):
    """
    中国A股股权激励行权数量与价格

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
    s_inc_execqty: NUMBER(20,4)
        行权数量(万份)   
    s_inc_execpri: NUMBER(20,4)
        行权价格   
    s_inc_execdate: VARCHAR2(8)
        行权日期   

    """
    __tablename__ = "AShareIncExecQtyPri"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_inc_sequence = Column(VARCHAR2(6))
    s_inc_name = Column(VARCHAR2(80))
    s_inc_execqty = Column(NUMBER(20,4))
    s_inc_execpri = Column(NUMBER(20,4))
    s_inc_execdate = Column(VARCHAR2(8))
    
