from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondCF(BaseModel):
    """
    中国债券现金流

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    b_info_carrydate: VARCHAR2(8)
        计息起始日   
    b_info_enddate: VARCHAR2(8)
        计息截止日   
    b_info_couponrate: NUMBER(22,6)
        票面利率(%)   
    b_info_paymentdate: VARCHAR2(8)
        现金流发放日   
    b_info_paymentinterest: NUMBER(22,6)
        期末每百元面额应付利息   
    b_info_paymentparvalue: NUMBER(22,6)
        期末每百元面额应付本金   
    b_info_paymentsum: NUMBER(22,6)
        期末每百元面额现金流合计   

    """
    __tablename__ = "CBondCF"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    b_info_carrydate = Column(VARCHAR2(8))
    b_info_enddate = Column(VARCHAR2(8))
    b_info_couponrate = Column(NUMBER(22,6))
    b_info_paymentdate = Column(VARCHAR2(8))
    b_info_paymentinterest = Column(NUMBER(22,6))
    b_info_paymentparvalue = Column(NUMBER(22,6))
    b_info_paymentsum = Column(NUMBER(22,6))
    
