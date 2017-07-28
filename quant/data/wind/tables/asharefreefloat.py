from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareFreeFloat(BaseModel):
    """
    4.16 中国A股自由流通股本

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    change_dt: VARCHAR2(8)
        变动日期(除权日)   
    s_share_freeshares: NUMBER(20,4)
        自由流通股本(万股)   
    change_dt1: VARCHAR2(8)
        变动日期(上市日)   
    ann_dt: VARCHAR2(8)
        公告日期   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareFreeFloat"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    change_dt = Column(VARCHAR2(8))
    s_share_freeshares = Column(NUMBER(20,4))
    change_dt1 = Column(VARCHAR2(8))
    ann_dt = Column(VARCHAR2(8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
