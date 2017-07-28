from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareHolderNumber(BaseModel):
    """
    4.37 中国A股股东户数

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    s_holder_enddate: VARCHAR2(8)
        截止日期   
    s_holder_num: NUMBER(20,4)
        A股股东户数   
    s_holder_total_num: NUMBER(20,4)
        股东总户数   若纯A股为A股户数；若含B股则为AB股总户数；若含H股则为AH股总户数；若含境外股, 则为A和境外股总户数
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareHolderNumber"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    s_holder_enddate = Column(VARCHAR2(8))
    s_holder_num = Column(NUMBER(20,4))
    s_holder_total_num = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
