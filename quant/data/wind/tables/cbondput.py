from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondPut(BaseModel):
    """
    4.125 中国债券回售条款执行说明

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    b_info_repurchasedate: VARCHAR2(8)
        回售日   
    b_info_repurchaseprice: NUMBER(20,4)
        每百元面值回售价格(元)   
    b_info_putannouncementdate: VARCHAR2(8)
        回售公告日   
    b_info_putexdate: VARCHAR2(8)
        回售履行结果公告日   
    b_info_putamount: NUMBER(20,4)
        回售总面额(亿元)   
    b_info_putoutstanding: NUMBER(20,4)
        继续托管总面额(亿元)   
    b_info_repurchasestartdate: VARCHAR2(8)
        回售行使开始日   
    b_info_repurchaseenddate: VARCHAR2(8)
        回售行使截止日   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondPut"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    b_info_repurchasedate = Column(VARCHAR2(8))
    b_info_repurchaseprice = Column(NUMBER(20,4))
    b_info_putannouncementdate = Column(VARCHAR2(8))
    b_info_putexdate = Column(VARCHAR2(8))
    b_info_putamount = Column(NUMBER(20,4))
    b_info_putoutstanding = Column(NUMBER(20,4))
    b_info_repurchasestartdate = Column(VARCHAR2(8))
    b_info_repurchaseenddate = Column(VARCHAR2(8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
