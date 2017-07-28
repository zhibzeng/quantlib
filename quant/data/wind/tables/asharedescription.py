from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareDescription(BaseModel):
    """
    4.1 中国A股基本资料

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_code: VARCHAR2(40)
        交易代码   
    s_info_name: VARCHAR2(50)
        证券简称   
    s_info_compname: VARCHAR2(100)
        公司中文名称   
    s_info_compnameeng: VARCHAR2(100)
        公司英文名称   
    s_info_isincode: VARCHAR2(40)
        ISIN代码   
    s_info_exchmarket: VARCHAR2(10)
        交易所   SSE:上交所SZSE:深交所
    s_info_listboard: VARCHAR2(10)
        上市板类型   上市板类型:434004000:主板434003000:中小企业板434001000:创业板
    s_info_listdate: VARCHAR2(8)
        上市日期   
    s_info_delistdate: VARCHAR2(8)
        退市日期   
    s_info_pinyin: VARCHAR2(10)
        简称拼音   
    s_info_listboardname: VARCHAR2(10)
        上市板   上市板包括：主板创业板中小企业板
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareDescription"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_code = Column(VARCHAR2(40))
    s_info_name = Column(VARCHAR2(50))
    s_info_compname = Column(VARCHAR2(100))
    s_info_compnameeng = Column(VARCHAR2(100))
    s_info_isincode = Column(VARCHAR2(40))
    s_info_exchmarket = Column(VARCHAR2(10))
    s_info_listboard = Column(VARCHAR2(10))
    s_info_listdate = Column(VARCHAR2(8))
    s_info_delistdate = Column(VARCHAR2(8))
    s_info_pinyin = Column(VARCHAR2(10))
    s_info_listboardname = Column(VARCHAR2(10))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
