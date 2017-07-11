from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class IndexContrastSector(BaseModel):
    """
    指数板块对照

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_indexcode: VARCHAR2(10)
        指数万得代码   
    s_info_name: VARCHAR2(50)
        指数简称   
    s_info_industrycode: VARCHAR2(40)
        板块代码   
    s_info_industryname: VARCHAR2(100)
        板块名称   

    """
    object_id = Column(VARCHAR2(100))
    s_info_indexcode = Column(VARCHAR2(10))
    s_info_name = Column(VARCHAR2(50))
    s_info_industrycode = Column(VARCHAR2(40))
    s_info_industryname = Column(VARCHAR2(100))
    
