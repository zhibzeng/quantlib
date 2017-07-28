from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondIssuer(BaseModel):
    """
    4.117 中国债券主体

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_compname: VARCHAR2(100)
        债券主体公司名称   
    s_info_compcode: VARCHAR2(10)
        债券主体公司id   
    used: NUMBER(1,0)
        是否有效   是否是债券最新的债务主体
    s_info_compind_code1: VARCHAR2(50)
        债券主体公司所属Wind一级行业代码   
    s_info_compind_name1: VARCHAR2(100)
        债券主体公司所属Wind一级行业名称   
    s_info_compind_code2: VARCHAR2(50)
        债券主体公司所属Wind二级行业代码   
    s_info_compind_name2: VARCHAR2(100)
        债券主体公司所属Wind二级行业名称   
    s_info_compind_code3: VARCHAR2(50)
        债券主体公司所属Wind三级行业代码   
    s_info_compind_name3: VARCHAR2(100)
        债券主体公司所属Wind三级行业名称   
    s_info_compind_code4: VARCHAR2(50)
        债券主体公司所属Wind四级行业代码   
    s_info_compind_name4: VARCHAR2(100)
        债券主体公司所属Wind四级行业名称   
    s_info_compregaddress: VARCHAR2(80)
        债券主体公司国籍(注册地)   
    s_info_comptype: VARCHAR2(40)
        债券主体类型   
    s_info_listcompornot: number(1,0)
        是否上市公司   1:是0:否
    s_info_effective_dt: VARCHAR2(8)
        生效日期   
    s_info_invalid_dt: VARCHAR2(8)
        失效日期   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondIssuer"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_compname = Column(VARCHAR2(100))
    s_info_compcode = Column(VARCHAR2(10))
    used = Column(NUMBER(1,0))
    s_info_compind_code1 = Column(VARCHAR2(50))
    s_info_compind_name1 = Column(VARCHAR2(100))
    s_info_compind_code2 = Column(VARCHAR2(50))
    s_info_compind_name2 = Column(VARCHAR2(100))
    s_info_compind_code3 = Column(VARCHAR2(50))
    s_info_compind_name3 = Column(VARCHAR2(100))
    s_info_compind_code4 = Column(VARCHAR2(50))
    s_info_compind_name4 = Column(VARCHAR2(100))
    s_info_compregaddress = Column(VARCHAR2(80))
    s_info_comptype = Column(VARCHAR2(40))
    s_info_listcompornot = Column(NUMBER(1,0))
    s_info_effective_dt = Column(VARCHAR2(8))
    s_info_invalid_dt = Column(VARCHAR2(8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
