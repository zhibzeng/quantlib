from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondCall(BaseModel):
    """
    4.124 中国债券赎回条款执行说明

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    b_info_redemptiondate: VARCHAR2(8)
        赎回日   
    b_info_redemptionprice: NUMBER(20,4)
        每百元面值赎回价格(元)   
    b_info_callannouncementdate: VARCHAR2(8)
        赎回公告日   
    b_info_callexdate: VARCHAR2(8)
        赎回履行结果公告日   
    b_info_callamount: NUMBER(20,4)
        赎回总面额(亿元)   
    b_info_calloutstanding: NUMBER(20,4)
        继续托管总面额(亿元)   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondCall"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    b_info_redemptiondate = Column(VARCHAR2(8))
    b_info_redemptionprice = Column(NUMBER(20,4))
    b_info_callannouncementdate = Column(VARCHAR2(8))
    b_info_callexdate = Column(VARCHAR2(8))
    b_info_callamount = Column(NUMBER(20,4))
    b_info_calloutstanding = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
