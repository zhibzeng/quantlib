from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class SWIndexMembers(BaseModel):
    """
    申万指数成份明细

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        指数Wind代码   
    s_con_windcode: VARCHAR2(40)
        成份股Wind代码   
    s_con_indate: VARCHAR2(8)
        纳入日期   
    s_con_outdate: VARCHAR2(8)
        剔除日期   
    cur_sign: NUMBER(1,0)
        最新标志   1:是0:否

    """
    __tablename__ = "SWIndexMembers"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_con_windcode = Column(VARCHAR2(40))
    s_con_indate = Column(VARCHAR2(8))
    s_con_outdate = Column(VARCHAR2(8))
    cur_sign = Column(NUMBER(1,0))
    
