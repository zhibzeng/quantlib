from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareIntroduction(BaseModel):
    """
    4.2 中国A股公司简介

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_province: VARCHAR2(20)
        省份   
    s_info_city: VARCHAR2(20)
        城市   
    s_info_chairman: VARCHAR2(38)
        法人代表   
    s_info_president: VARCHAR2(38)
        总经理   
    s_info_bdsecretary: VARCHAR2(500)
        董事会秘书   
    s_info_regcapital: NUMBER(20,4)
        注册资本(万元)   
    s_info_founddate: VARCHAR2(8)
        成立日期   
    s_info_chineseintroduction: VARCHAR2(2000)
        公司中文简介   
    s_info_comptype: VARCHAR2(20)
        公司类型   
    s_info_website: VARCHAR2(80)
        主页   
    s_info_email: VARCHAR2(80)
        电子邮箱   
    s_info_office: VARCHAR2(80)
        办公地址   
    ann_dt: VARCHAR2(8)
        公告日期   
    s_info_country: VARCHAR2(20)
        国籍   
    s_info_businessscope: VARCHAR2(2000)
        经营范围   
    s_info_company_type: VARCHAR2(10)
        公司类别   
    s_info_totalemployees: NUMBER(20,0)
        员工总数(人)   
    s_info_main_business: VARCHAR2(1000)
        主要产品及业务   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareIntroduction"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_province = Column(VARCHAR2(20))
    s_info_city = Column(VARCHAR2(20))
    s_info_chairman = Column(VARCHAR2(38))
    s_info_president = Column(VARCHAR2(38))
    s_info_bdsecretary = Column(VARCHAR2(500))
    s_info_regcapital = Column(NUMBER(20,4))
    s_info_founddate = Column(VARCHAR2(8))
    s_info_chineseintroduction = Column(VARCHAR2(2000))
    s_info_comptype = Column(VARCHAR2(20))
    s_info_website = Column(VARCHAR2(80))
    s_info_email = Column(VARCHAR2(80))
    s_info_office = Column(VARCHAR2(80))
    ann_dt = Column(VARCHAR2(8))
    s_info_country = Column(VARCHAR2(20))
    s_info_businessscope = Column(VARCHAR2(2000))
    s_info_company_type = Column(VARCHAR2(10))
    s_info_totalemployees = Column(NUMBER(20,0))
    s_info_main_business = Column(VARCHAR2(1000))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
