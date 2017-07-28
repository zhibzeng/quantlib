from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondIssuerRating(BaseModel):
    """
    4.145 中国债券主体信用评级

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_compname: VARCHAR2(100)
        公司中文名称   
    ann_dt: VARCHAR2(8)
        公告日期   
    b_rate_style: VARCHAR2(100)
        评级类型   1长期信用评级2短期信用评级
    b_info_creditrating: VARCHAR2(40)
        信用评级   
    b_rate_ratingoutlook: NUMBER(9,0)
        评级展望   518001000：正面518002000：负面518003000：稳定518006000：观望518007000：待决
    b_info_creditratingagency: VARCHAR2(10)
        评级机构代码   1标准普尔评级服务公司10云南省资信评估事务所11北京穆迪投资者服务有限公司12福建省资信评级委员会13中诚信证券评估有限公司14鹏元资信评估有限公司16穆迪投资者服务有限公司17惠誉国际信用评级有限公司2中诚信国际信用评级有限责任公司3上海远东资信评估有限公司4上海新世纪资信评估投资服务有限公司5联合资信评估有限公司6大公国际资信评估有限公司7联合信用评级有限公司8辽宁省资信评估有限公司9长城资信评估有限公司
    s_info_compcode: VARCHAR2(10)
        债券主体公司id   
    b_info_creditratingexplain: VARCHAR2(1000)
        信用评级说明   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondIssuerRating"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_compname = Column(VARCHAR2(100))
    ann_dt = Column(VARCHAR2(8))
    b_rate_style = Column(VARCHAR2(100))
    b_info_creditrating = Column(VARCHAR2(40))
    b_rate_ratingoutlook = Column(NUMBER(9,0))
    b_info_creditratingagency = Column(VARCHAR2(10))
    s_info_compcode = Column(VARCHAR2(10))
    b_info_creditratingexplain = Column(VARCHAR2(1000))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
