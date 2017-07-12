from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondIndustriesCode(BaseModel):
    """
    中国债券板块代码

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    industriescode: VARCHAR2(38)
        板块代码   
    industriesname: VARCHAR2(50)
        板块名称   
    levelnum: NUMBER(1,0)
        级数   
    used: NUMBER(1,0)
        是否有效   
    industriestype: VARCHAR2(50)
        板块类型   1:中国Wind债券分类2:中债债券分类3:中国Wind债券概念分类
    industriescode1: VARCHAR2(38)
        板块代码(父)   

    """
    __tablename__ = "CBondIndustriesCode"
    object_id = Column(VARCHAR2(100), primary_key=True)
    industriescode = Column(VARCHAR2(38))
    industriesname = Column(VARCHAR2(50))
    levelnum = Column(NUMBER(1,0))
    used = Column(NUMBER(1,0))
    industriestype = Column(VARCHAR2(50))
    industriescode1 = Column(VARCHAR2(38))
    
