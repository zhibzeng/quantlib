from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondPreRelease(BaseModel):
    """
    中国债券预发行资料

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_date: VARCHAR2(8)
        公告日期   
    pre_release_code: VARCHAR2(10)
        预发行代码   
    pre_release_name: VARCHAR2(40)
        预发行简称   
    pre_release_begindate: VARCHAR2(8)
        预发行交易起始日   
    pre_release_enddate: VARCHAR2(8)
        预发行交易截止日   
    s_base_info: NUMBER(24,8)
        基准价格/收益率   根据价格类型代码确定是基准价格还是收益率
    b_anal_rduration: NUMBER(24,8)
        参考久期   
    price_type_code: NUMBER(9,0)
        价格类型代码   利率：530001000价格：530003000

    """
    __tablename__ = "CBondPreRelease"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_date = Column(VARCHAR2(8))
    pre_release_code = Column(VARCHAR2(10))
    pre_release_name = Column(VARCHAR2(40))
    pre_release_begindate = Column(VARCHAR2(8))
    pre_release_enddate = Column(VARCHAR2(8))
    s_base_info = Column(NUMBER(24,8))
    b_anal_rduration = Column(NUMBER(24,8))
    price_type_code = Column(NUMBER(9,0))
    
