from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondPayment(BaseModel):
    """
    中国债券付息和兑付

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    b_info_announcementdate: VARCHAR2(8)
        公告日期   
    s_div_recorddate: VARCHAR2(8)
        债权登记日   
    s_div_exdate: VARCHAR2(8)
        除息日   
    b_info_paymentdate: VARCHAR2(8)
        付息日   
    b_info_interestperthousands: NUMBER(20,4)
        每手付息数   
    b_info_principalperthousands: NUMBER(20,6)
        每手兑付本金数   
    b_info_principalaftertax: NUMBER(20,4)
        税后每手付息数   
    crncy_code: VARCHAR2(10)
        货币代码   

    """
    __tablename__ = "CBondPayment"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    b_info_announcementdate = Column(VARCHAR2(8))
    s_div_recorddate = Column(VARCHAR2(8))
    s_div_exdate = Column(VARCHAR2(8))
    b_info_paymentdate = Column(VARCHAR2(8))
    b_info_interestperthousands = Column(NUMBER(20,4))
    b_info_principalperthousands = Column(NUMBER(20,6))
    b_info_principalaftertax = Column(NUMBER(20,4))
    crncy_code = Column(VARCHAR2(10))
    
