from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class WindCustomCode(BaseModel):
    """
    4.218 Wind兼容代码

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_asharecode: VARCHAR2(10)
        证券ID   
    s_info_compcode: VARCHAR2(100)
        公司ID   
    s_info_securitiestypes: VARCHAR2(10)
        证券类型   
    s_info_sectypename: VARCHAR2(40)
        类型名称   
    s_info_countryname: VARCHAR2(10)
        国别   
    s_info_countrycode: VARCHAR2(10)
        国别编号   
    s_info_exchmarketname: VARCHAR2(40)
        交易所   
    s_info_exchmarket: VARCHAR2(10)
        交易所编号   
    crncy_name: VARCHAR2(40)
        币种   
    crncy_code: VARCHAR2(10)
        币种编号   
    s_info_isincode: VARCHAR2(40)
        ISIN代码   
    s_info_code: VARCHAR2(40)
        交易代码   
    s_info_name: VARCHAR2(40)
        证券中文简称   
    exchmarket: VARCHAR2(10)
        交易所   外汇:FX,市场原：NIB改为:EX.其他类同:交易所编号
    security_status: NUMBER(9,0)
        存续状态   有效(L):101001000发行(N):101003000摘牌(D):101002000
    s_info_org_code: VARCHAR2(20)
        组织机构代码   
    s_info_typecode: NUMBER(9,0)
        分类代码   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "WindCustomCode"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_asharecode = Column(VARCHAR2(10))
    s_info_compcode = Column(VARCHAR2(100))
    s_info_securitiestypes = Column(VARCHAR2(10))
    s_info_sectypename = Column(VARCHAR2(40))
    s_info_countryname = Column(VARCHAR2(10))
    s_info_countrycode = Column(VARCHAR2(10))
    s_info_exchmarketname = Column(VARCHAR2(40))
    s_info_exchmarket = Column(VARCHAR2(10))
    crncy_name = Column(VARCHAR2(40))
    crncy_code = Column(VARCHAR2(10))
    s_info_isincode = Column(VARCHAR2(40))
    s_info_code = Column(VARCHAR2(40))
    s_info_name = Column(VARCHAR2(40))
    exchmarket = Column(VARCHAR2(10))
    security_status = Column(NUMBER(9,0))
    s_info_org_code = Column(VARCHAR2(20))
    s_info_typecode = Column(NUMBER(9,0))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
