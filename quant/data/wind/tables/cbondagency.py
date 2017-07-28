from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondAgency(BaseModel):
    """
    4.128 中国债券中介机构

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    b_info_windcode: VARCHAR2(40)
        Wind代码   
    b_agency_name: VARCHAR2(200)
        机构名称   
    b_relation_typcode: VARCHAR2(10)
        关系类型代码   10主承销商11保荐人12分销商21托管人34簿记场所39配售承销商
    b_agency_nameid: VARCHAR2(200)
        机构名称ID   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondAgency"
    object_id = Column(VARCHAR2(100), primary_key=True)
    b_info_windcode = Column(VARCHAR2(40))
    b_agency_name = Column(VARCHAR2(200))
    b_relation_typcode = Column(VARCHAR2(10))
    b_agency_nameid = Column(VARCHAR2(200))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
