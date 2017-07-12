from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondIndustryWind(BaseModel):
    """
    中国Wind债券分类板块

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_industrycode: VARCHAR2(20)
        一级板块代码   
    s_info_industryname: VARCHAR2(100)
        一级板块名称   
    s_info_industrycode2: VARCHAR2(20)
        二级板块代码   
    s_info_industryname2: VARCHAR2(100)
        二级板块名称   

    """
    __tablename__ = "CBondIndustryWind"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_industrycode = Column(VARCHAR2(20))
    s_info_industryname = Column(VARCHAR2(100))
    s_info_industrycode2 = Column(VARCHAR2(20))
    s_info_industryname2 = Column(VARCHAR2(100))
    
