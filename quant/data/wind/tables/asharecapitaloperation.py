from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareCapitalOperation(BaseModel):
    """
    中国A股资本运作

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    s_capitaloperation_enddate: VARCHAR2(8)
        截止日期   
    s_capitaloperation_share: NUMBER(20,4)
        股票数量   
    s_capitaloperation_amount: NUMBER(20,4)
        投资金额   
    crncy_code: VARCHAR2(3)
        货币代码   CNY
    s_capitaloperation_companyname: VARCHAR2(100)
        参股公司名称   
    s_capitaloperat_compwindcode: VARCHAR2(40)
        参股公司Wind代码   记录上市公司A股代码
    s_end_bal: NUMBER(20,4)
        期末账面值   

    """
    __tablename__ = "AShareCapitalOperation"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    s_capitaloperation_enddate = Column(VARCHAR2(8))
    s_capitaloperation_share = Column(NUMBER(20,4))
    s_capitaloperation_amount = Column(NUMBER(20,4))
    crncy_code = Column(VARCHAR2(3))
    s_capitaloperation_companyname = Column(VARCHAR2(100))
    s_capitaloperat_compwindcode = Column(VARCHAR2(40))
    s_end_bal = Column(NUMBER(20,4))
    
