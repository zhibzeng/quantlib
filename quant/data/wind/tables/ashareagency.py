from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareAgency(BaseModel):
    """
    4.10 中国A股发行中介机构

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_agency_name: VARCHAR2(200)
        机构名称   
    s_relation_typcode: VARCHAR2(10)
        关系类型代码   10主承销商11副主承销商12分销商20财务顾问
    s_business_typcode: NUMBER(9,0)
        业务类型代码   464008000首发464009000增发464004000配股464001000收购兼并
    s_agency_nameid: VARCHAR2(200)
        机构名称ID   
    begindate: VARCHAR2(8)
        起始日期   
    enddate: VARCHAR2(8)
        截止日期   
    sequence: VARCHAR2(6)
        序号   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareAgency"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_agency_name = Column(VARCHAR2(200))
    s_relation_typcode = Column(VARCHAR2(10))
    s_business_typcode = Column(NUMBER(9,0))
    s_agency_nameid = Column(VARCHAR2(200))
    begindate = Column(VARCHAR2(8))
    enddate = Column(VARCHAR2(8))
    sequence = Column(VARCHAR2(6))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
