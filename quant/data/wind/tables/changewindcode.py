from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class ChangeWindcode(BaseModel):
    """
    4.222 Wind代码变更表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_oldwindcode: VARCHAR2(40)
        变更前Wind代码   
    s_info_newwindcode: VARCHAR2(40)
        变更后Wind代码   
    change_date: VARCHAR2(8)
        Wind代码变更日期   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "ChangeWindcode"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_oldwindcode = Column(VARCHAR2(40))
    s_info_newwindcode = Column(VARCHAR2(40))
    change_date = Column(VARCHAR2(8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
