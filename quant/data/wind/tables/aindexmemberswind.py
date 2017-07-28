from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AIndexMembersWIND(BaseModel):
    """
    4.79 中国A股万得指数成份股

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    f_info_windcode: VARCHAR2(40)
        指数Wind代码   
    s_con_windcode: VARCHAR2(40)
        成份股Wind代码   
    s_con_indate: VARCHAR2(8)
        纳入日期   
    s_con_outdate: VARCHAR2(8)
        剔除日期   
    cur_sign: NUMBER(1,0)
        最新标志   1:是0:否
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AIndexMembersWIND"
    object_id = Column(VARCHAR2(100), primary_key=True)
    f_info_windcode = Column(VARCHAR2(40))
    s_con_windcode = Column(VARCHAR2(40))
    s_con_indate = Column(VARCHAR2(8))
    s_con_outdate = Column(VARCHAR2(8))
    cur_sign = Column(NUMBER(1,0))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
