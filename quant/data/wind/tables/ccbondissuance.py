from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CCBondIssuance(BaseModel):
    """
    中国可转债发行

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    crncy_code: VARCHAR2(10)
        货币代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    cb_info_preplandate: VARCHAR2(8)
        预案公告日   
    cb_info_smtganncedate: VARCHAR2(8)
        股东大会公告日   
    cb_issue_anncelstdate: VARCHAR2(8)
        上市公告日   
    cb_info_listeddate: VARCHAR2(8)
        上市日期   
    cb_info_listdate: VARCHAR2(20)
        方案进度   
    cb_info_isseparation: NUMBER(7,3)
        是否分离交易可转债   
    cb_info_distributo: VARCHAR2(1000)
        分销商ID   
    cb_info_recommender: VARCHAR2(200)
        上市推荐人   
    cb_clause_ischainterest: NUMBER(5,0)
        利率是否随存款利率调整   
    cb_clause_iscominterest: NUMBER(5,0)
        是否有利息补偿条款   
    cb_clause_cominterest: NUMBER(20,4)
        补偿利率   
    cb_clause_cominterestitem: VARCHAR2(500)
        利率补偿说明   
    cb_clause_conversionitem: VARCHAR2(1000)
        初始转股价条款   
    cb_clause_convchangeitem: VARCHAR2(1000)
        转股价格调整条款   
    cb_clause_convmonth: VARCHAR2(1000)
        转换期条款   
    cb_clause_iniconvprice: NUMBER(20,4)
        初始转股价格   
    cb_clause_iniconvproportion: NUMBER(20,4)
        初始转股价比例   
    cb_clause_callitem: VARCHAR2(1000)
        回售条款   
    cb_clause_reset_item: VARCHAR2(1000)
        赎回条款   
    cb_clause_resetitem: VARCHAR2(1000)
        特别向下修正条款   
    cb_clause_rationitem: VARCHAR2(2000)
        向原股东配售安排条款   
    cb_list_passdate: VARCHAR2(8)
        发审委通过公告日   
    cb_list_permitdate: VARCHAR2(8)
        证监会核准公告日   
    cb_list_announcedate: VARCHAR2(8)
        发行公告日   
    cb_list_annocedate: VARCHAR2(8)
        发行结果公告日   
    cb_list_type: VARCHAR2(40)
        发行方式   
    cb_list_fee: NUMBER(20,4)
        发行费用   
    cb_list_rationdate: VARCHAR2(8)
        老股东配售日期   
    cb_list_rationchkindate: VARCHAR2(8)
        老股东配售股权登记日   
    cb_list_rationpaymtdate: VARCHAR2(8)
        老股东配售缴款日   
    cb_list_rationcode: VARCHAR2(10)
        老股东配售代码   
    cb_list_rationname: VARCHAR2(40)
        老股东配售简称   
    cb_list_rationprice: NUMBER(20,4)
        老股东配售价格   
    cb_list_rationratiode: NUMBER(20,4)
        老股东配售比例分母   
    cb_list_rationratiomo: NUMBER(20,4)
        老股东配售比例分子   
    cb_list_rationvol: NUMBER(20,4)
        向老股东配售数量(张)   
    cb_list_originals: NUMBER(20,4)
        老股东配售户数   
    cb_list_dtonl: VARCHAR2(8)
        网上发行日期   
    cb_list_pchasecodeonl: VARCHAR2(10)
        网上发行申购代码   
    cb_list_pchnameonl: VARCHAR2(40)
        网上发行申购名称   
    cb_list_pchpriceonl: NUMBER(20,4)
        网上发行申购价格   
    cb_list_issuevolonl: NUMBER(20,4)
        网上发行数量(不含优先配售)(张)   
    cb_list_codeonl: NUMBER(20,4)
        网上发行配号总数   
    cb_list_excesspchonl: NUMBER(20,4)
        网上发行超额认购倍数(不含优先配售)   
    cb_result_efsubscrpoff: NUMBER(20,4)
        网上有效申购户数(不含优先配售)   
    cb_result_sucrateoff: NUMBER(20,4)
        网上有效申购手数(不含优先配售)   
    cb_list_dateinstoff: VARCHAR2(8)
        网下向机构投资者发行日期   
    cb_list_volinstoff: NUMBER(20,4)
        网下向机构投资者发行数量(不含优先配售)   
    cb_result_sucrateon: NUMBER(20,10)
        网上中签率(不含优先配售)   
    cb_list_effectpchvoloff: NUMBER(20,4)
        网下有效申购手数(不含优先配售)   
    cb_list_effpchof: NUMBER(20,4)
        网下有效申购户数(不含优先配售)   
    cb_list_sucrateoff: NUMBER(20,4)
        网下中签率(不含优先配售)   
    cb_list_prerationvol: NUMBER(20,4)
        网下优先配售数量(张)   

    """
    __tablename__ = "CCBondIssuance"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    crncy_code = Column(VARCHAR2(10))
    ann_dt = Column(VARCHAR2(8))
    cb_info_preplandate = Column(VARCHAR2(8))
    cb_info_smtganncedate = Column(VARCHAR2(8))
    cb_issue_anncelstdate = Column(VARCHAR2(8))
    cb_info_listeddate = Column(VARCHAR2(8))
    cb_info_listdate = Column(VARCHAR2(20))
    cb_info_isseparation = Column(NUMBER(7,3))
    cb_info_distributo = Column(VARCHAR2(1000))
    cb_info_recommender = Column(VARCHAR2(200))
    cb_clause_ischainterest = Column(NUMBER(5,0))
    cb_clause_iscominterest = Column(NUMBER(5,0))
    cb_clause_cominterest = Column(NUMBER(20,4))
    cb_clause_cominterestitem = Column(VARCHAR2(500))
    cb_clause_conversionitem = Column(VARCHAR2(1000))
    cb_clause_convchangeitem = Column(VARCHAR2(1000))
    cb_clause_convmonth = Column(VARCHAR2(1000))
    cb_clause_iniconvprice = Column(NUMBER(20,4))
    cb_clause_iniconvproportion = Column(NUMBER(20,4))
    cb_clause_callitem = Column(VARCHAR2(1000))
    cb_clause_reset_item = Column(VARCHAR2(1000))
    cb_clause_resetitem = Column(VARCHAR2(1000))
    cb_clause_rationitem = Column(VARCHAR2(2000))
    cb_list_passdate = Column(VARCHAR2(8))
    cb_list_permitdate = Column(VARCHAR2(8))
    cb_list_announcedate = Column(VARCHAR2(8))
    cb_list_annocedate = Column(VARCHAR2(8))
    cb_list_type = Column(VARCHAR2(40))
    cb_list_fee = Column(NUMBER(20,4))
    cb_list_rationdate = Column(VARCHAR2(8))
    cb_list_rationchkindate = Column(VARCHAR2(8))
    cb_list_rationpaymtdate = Column(VARCHAR2(8))
    cb_list_rationcode = Column(VARCHAR2(10))
    cb_list_rationname = Column(VARCHAR2(40))
    cb_list_rationprice = Column(NUMBER(20,4))
    cb_list_rationratiode = Column(NUMBER(20,4))
    cb_list_rationratiomo = Column(NUMBER(20,4))
    cb_list_rationvol = Column(NUMBER(20,4))
    cb_list_originals = Column(NUMBER(20,4))
    cb_list_dtonl = Column(VARCHAR2(8))
    cb_list_pchasecodeonl = Column(VARCHAR2(10))
    cb_list_pchnameonl = Column(VARCHAR2(40))
    cb_list_pchpriceonl = Column(NUMBER(20,4))
    cb_list_issuevolonl = Column(NUMBER(20,4))
    cb_list_codeonl = Column(NUMBER(20,4))
    cb_list_excesspchonl = Column(NUMBER(20,4))
    cb_result_efsubscrpoff = Column(NUMBER(20,4))
    cb_result_sucrateoff = Column(NUMBER(20,4))
    cb_list_dateinstoff = Column(VARCHAR2(8))
    cb_list_volinstoff = Column(NUMBER(20,4))
    cb_result_sucrateon = Column(NUMBER(20,10))
    cb_list_effectpchvoloff = Column(NUMBER(20,4))
    cb_list_effpchof = Column(NUMBER(20,4))
    cb_list_sucrateoff = Column(NUMBER(20,4))
    cb_list_prerationvol = Column(NUMBER(20,4))
    
