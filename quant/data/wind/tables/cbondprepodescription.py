from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondPRepoDescription(BaseModel):
    """
    4.167 中国债券回购基本资料

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_subjectwindcode: VARCHAR2(40)
        标的债券Wind代码   
    b_info_repo_type: VARCHAR2(40)
        回购类型   1封闭式;2买断式
    b_info_repo_days: NUMBER(5,0)
        回购天数   
    b_info_repo_firstdate: VARCHAR2(8)
        首次交易日期   
    b_info_repo_pcntbond: NUMBER(20,4)
        履约金比例   
    s_info_name: VARCHAR2(50)
        证券简称   
    s_info_exchmarket: VARCHAR2(10)
        交易所   SSE:上交所SZSE:深交所NIB:银行间债券
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondPRepoDescription"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_subjectwindcode = Column(VARCHAR2(40))
    b_info_repo_type = Column(VARCHAR2(40))
    b_info_repo_days = Column(NUMBER(5,0))
    b_info_repo_firstdate = Column(VARCHAR2(8))
    b_info_repo_pcntbond = Column(NUMBER(20,4))
    s_info_name = Column(VARCHAR2(50))
    s_info_exchmarket = Column(VARCHAR2(10))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
