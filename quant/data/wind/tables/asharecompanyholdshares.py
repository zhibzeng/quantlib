from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareCompanyHoldShares(BaseModel):
    """
    中国A股控股参股

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    enddate: VARCHAR2(8)
        截止日期   
    s_capitaloperation_companyname: VARCHAR2(100)
        被参控公司名称   
    s_capitaloperation_companyid: VARCHAR2(10)
        被参控公司ID   
    s_capitaloperation_comainbus: VARCHAR2(100)
        被参控公司主营业务   
    relations_code: VARCHAR2(40)
        关系代码   2子公司3同一母公司4合营企业5联营企业6公司股东8同一控股公司9N/A10同一关键人员11孙公司
    s_capitaloperation_pct: NUMBER(20,4)
        直接持股比例   
    voting_rights: NUMBER(20,4)
        表决权比例   
    s_capitaloperation_amount: NUMBER(20,4)
        投资金额(万元)   
    operationcrncy_code: VARCHAR2(10)
        货币代码   
    s_capitaloperation_coregcap: NUMBER(20,4)
        被参股公司注册资本(万元)   
    crncy_code: VARCHAR2(10)
        货币代码2   
    is_consolidate: NUMBER(5,4)
        是否合并报表   
    notconsolidate_reason: VARCHAR2(500)
        未纳入合并报表原因   

    """
    __tablename__ = "AShareCompanyHoldShares"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    enddate = Column(VARCHAR2(8))
    s_capitaloperation_companyname = Column(VARCHAR2(100))
    s_capitaloperation_companyid = Column(VARCHAR2(10))
    s_capitaloperation_comainbus = Column(VARCHAR2(100))
    relations_code = Column(VARCHAR2(40))
    s_capitaloperation_pct = Column(NUMBER(20,4))
    voting_rights = Column(NUMBER(20,4))
    s_capitaloperation_amount = Column(NUMBER(20,4))
    operationcrncy_code = Column(VARCHAR2(10))
    s_capitaloperation_coregcap = Column(NUMBER(20,4))
    crncy_code = Column(VARCHAR2(10))
    is_consolidate = Column(NUMBER(5,4))
    notconsolidate_reason = Column(VARCHAR2(500))
    
