from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CompIntroduction(BaseModel):
    """
    公司简介

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    comp_id: VARCHAR2(40)
        公司ID   
    comp_name: VARCHAR2(100)
        公司名称   
    comp_sname: VARCHAR2(40)
        公司中文简称   
    comp_name_eng: VARCHAR2(100)
        英文名称   
    comp_snameeng: VARCHAR2(100)
        英文名称缩写   
    province: VARCHAR2(20)
        省份   
    city: VARCHAR2(20)
        城市   
    address: VARCHAR2(80)
        注册地址   
    office: VARCHAR2(80)
        办公地址   
    zipcode: VARCHAR2(10)
        邮编   
    phone: VARCHAR2(50)
        电话   
    fax: VARCHAR2(50)
        传真   
    email: VARCHAR2(80)
        电子邮件   
    website: VARCHAR2(80)
        公司网址   
    registernumber: VARCHAR2(20)
        工商登记号   
    chairman: VARCHAR2(38)
        法人代表   
    president: VARCHAR2(38)
        总经理   
    discloser: VARCHAR2(500)
        信息披露人   
    regcapital: NUMBER(20,4)
        注册资本   万元
    currencycode: VARCHAR2(10)
        货币代码   
    founddate: VARCHAR2(8)
        成立日期   
    enddate: VARCHAR2(8)
        公司终止日期   
    briefing: VARCHAR2(2000)
        公司简介   
    comp_type: VARCHAR2(100)
        公司类型   
    comp_property: VARCHAR2(100)
        企业性质   
    country: VARCHAR2(20)
        国籍   
    businessscope: VARCHAR2(2000)
        经营范围   
    company_type: VARCHAR2(10)
        公司类别   
    totalemployees: NUMBER(20,0)
        员工总数(人)   
    main_business: VARCHAR2(1000)
        主要产品及业务   

    """
    __tablename__ = "CompIntroduction"
    object_id = Column(VARCHAR2(100), primary_key=True)
    comp_id = Column(VARCHAR2(40))
    comp_name = Column(VARCHAR2(100))
    comp_sname = Column(VARCHAR2(40))
    comp_name_eng = Column(VARCHAR2(100))
    comp_snameeng = Column(VARCHAR2(100))
    province = Column(VARCHAR2(20))
    city = Column(VARCHAR2(20))
    address = Column(VARCHAR2(80))
    office = Column(VARCHAR2(80))
    zipcode = Column(VARCHAR2(10))
    phone = Column(VARCHAR2(50))
    fax = Column(VARCHAR2(50))
    email = Column(VARCHAR2(80))
    website = Column(VARCHAR2(80))
    registernumber = Column(VARCHAR2(20))
    chairman = Column(VARCHAR2(38))
    president = Column(VARCHAR2(38))
    discloser = Column(VARCHAR2(500))
    regcapital = Column(NUMBER(20,4))
    currencycode = Column(VARCHAR2(10))
    founddate = Column(VARCHAR2(8))
    enddate = Column(VARCHAR2(8))
    briefing = Column(VARCHAR2(2000))
    comp_type = Column(VARCHAR2(100))
    comp_property = Column(VARCHAR2(100))
    country = Column(VARCHAR2(20))
    businessscope = Column(VARCHAR2(2000))
    company_type = Column(VARCHAR2(10))
    totalemployees = Column(NUMBER(20,0))
    main_business = Column(VARCHAR2(1000))
    
