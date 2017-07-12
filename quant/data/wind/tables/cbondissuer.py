from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondIssuer(BaseModel):
    """
    中国债券主体

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
        债券主体公司所属Wind四级行   

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
    
