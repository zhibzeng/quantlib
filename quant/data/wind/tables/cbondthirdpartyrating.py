from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondThirdPartyRating(BaseModel):
    """
    4.149 中国债券第三方信用评级

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_compname: VARCHAR2(100)
        公司名称   
    s_info_compcode: VARCHAR2(10)
        公司id   
    b_rate_style: NUMBER(9,0)
        品种类别代码   1：证券2：公司
    b_info_listdate: VARCHAR2(8)
        发布日期   
    b_typcode: NUMBER(9,0)
        评级类型代码   477001000：长期信用评级477002000：短期信用评级
    b_est_rating_inst: VARCHAR2(40)
        信用等级   
    b_est_institute: VARCHAR2(100)
        评估机构公司   
    b_rate_ratingoutlook: VARCHAR2(10)
        评级展望   
    b_est_prerating_inst: VARCHAR2(40)
        前次评级   
    b_rate_preratingoutlook: VARCHAR2(10)
        前次评级展望   
    b_est_rating_change: VARCHAR2(10)
        评级变动方向   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondThirdPartyRating"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_compname = Column(VARCHAR2(100))
    s_info_compcode = Column(VARCHAR2(10))
    b_rate_style = Column(NUMBER(9,0))
    b_info_listdate = Column(VARCHAR2(8))
    b_typcode = Column(NUMBER(9,0))
    b_est_rating_inst = Column(VARCHAR2(40))
    b_est_institute = Column(VARCHAR2(100))
    b_rate_ratingoutlook = Column(VARCHAR2(10))
    b_est_prerating_inst = Column(VARCHAR2(40))
    b_rate_preratingoutlook = Column(VARCHAR2(10))
    b_est_rating_change = Column(VARCHAR2(10))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
