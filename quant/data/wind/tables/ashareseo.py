from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareSEO(BaseModel):
    """
    中国A股增发

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_fellow_progress: VARCHAR2(10)
        方案进度   1.董事会预案2.股东大会通过3.实施4.未通过5.证监会批准8.国资委批准12.停止实施
    s_fellow_issuetype: VARCHAR2(10)
        发行方式   发行方式类型439006000:定向439010000:公开
    crncy_code: VARCHAR2(10)
        货币代码   
    s_fellow_price: NUMBER(20,4)
        发行价格(元)   
    s_fellow_amount: NUMBER(20,4)
        发行数量(万股)   
    s_fellow_collection: NUMBER(20,4)
        募集资金(元)   含发行费用
    s_fellow_recorddate: VARCHAR2(8)
        股权登记日   
    s_fellow_paystartdate: VARCHAR2(8)
        向老股东配售(或优先配售)缴款起始日   
    s_fellow_payenddate: VARCHAR2(8)
        向老股东配售(或优先配售)缴款终止日   
    s_fellow_subdate: VARCHAR2(8)
        网上申购日   
    s_fellow_otcdate: VARCHAR2(8)
        股份登记(定向)日期   
    s_fellow_listdate: VARCHAR2(8)
        向公众增发股份上市日期   
    s_fellow_instlistdate: VARCHAR2(8)
        向机构增发股份上市日期   定向增发部分流通日期
    s_fellow_changedate: VARCHAR2(8)
        定向增发股份变动日期   
    s_fellow_roadshowdate: VARCHAR2(8)
        网上路演日   
    s_fellow_refunddate: VARCHAR2(8)
        网下申购资金(定金)退款日   
    s_fellow_unfrozedate: VARCHAR2(8)
        网上申购资金解冻日   
    s_fellow_preplandate: VARCHAR2(8)
        预案公告日   
    s_fellow_smtganncedate: VARCHAR2(8)
        股东大会公告日   
    s_fellow_passdate: VARCHAR2(8)
        发审委通过公告日   发审委审核通过的公告日
    s_fellow_approveddate: VARCHAR2(8)
        证监会核准公告日   证监会核准发行的公告日
    s_fellow_anncedate: VARCHAR2(8)
        上网发行公告日   
    s_fellow_ratioanncedate: VARCHAR2(8)
        网上中签率公告日   
    s_fellow_offeringdate: VARCHAR2(8)
        增发公告日   
    s_fellow_listanndate: VARCHAR2(8)
        上市公告日   
    s_fellow_offeringobject: VARCHAR2(200)
        发行对象   
    s_fellow_priceuplimit: NUMBER(20,4)
        增发预案价上限   
    s_fellow_pricedownlimit: NUMBER(20,4)
        增发预案价下限   
    s_seo_code: VARCHAR2(10)
        增发代码   
    s_seo_name: VARCHAR2(20)
        增发简称   
    s_seo_pe: NUMBER(20,4)
        发行市盈率(摊薄)   
    s_seo_amtbyplacing: NUMBER(20,4)
        上网发行数量(万股)   
    s_seo_amttojur: NUMBER(20,4)
        网下发行数量(万股)   
    s_seo_holdersubsmode: VARCHAR2(30
        大股东认购方式   
    s_seo_holdersubsrate: NUMBER(20,4)
        大股东认购比例(%)   
    ann_dt: VARCHAR2(8)
        最新公告日期   
    pricingmode: NUMBER(9,0)
        定向增发定价方式代码   竞价:275001000定价:275002000
    s_fellow_orgpricemin: NUMBER(20,4)
        原始预案价下限   
    s_fellow_discntratio: NUMBER(20,4)
        折扣率   
    s_fellow_date: VARCHAR2(8)
        定增发行日期   
    s_fellow_subinvitationdt: VARCHAR2(8)
        认购邀请书日   
    s_fellow_year: VARCHAR2(8)
        增发年度   
    s_fellow_objective_code: NUMBER(9,0)
        定向增发目的代码   关联AShareTypeCode.s_typcode获取类型名称
    pricingdate: VARCHAR2(8)
        定价基准日   
    is_no_public: NUMBER(5,0)
        是否属于非公开发行   0：否1:是

    """
    __tablename__ = "AShareSEO"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_fellow_progress = Column(VARCHAR2(10))
    s_fellow_issuetype = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    s_fellow_price = Column(NUMBER(20,4))
    s_fellow_amount = Column(NUMBER(20,4))
    s_fellow_collection = Column(NUMBER(20,4))
    s_fellow_recorddate = Column(VARCHAR2(8))
    s_fellow_paystartdate = Column(VARCHAR2(8))
    s_fellow_payenddate = Column(VARCHAR2(8))
    s_fellow_subdate = Column(VARCHAR2(8))
    s_fellow_otcdate = Column(VARCHAR2(8))
    s_fellow_listdate = Column(VARCHAR2(8))
    s_fellow_instlistdate = Column(VARCHAR2(8))
    s_fellow_changedate = Column(VARCHAR2(8))
    s_fellow_roadshowdate = Column(VARCHAR2(8))
    s_fellow_refunddate = Column(VARCHAR2(8))
    s_fellow_unfrozedate = Column(VARCHAR2(8))
    s_fellow_preplandate = Column(VARCHAR2(8))
    s_fellow_smtganncedate = Column(VARCHAR2(8))
    s_fellow_passdate = Column(VARCHAR2(8))
    s_fellow_approveddate = Column(VARCHAR2(8))
    s_fellow_anncedate = Column(VARCHAR2(8))
    s_fellow_ratioanncedate = Column(VARCHAR2(8))
    s_fellow_offeringdate = Column(VARCHAR2(8))
    s_fellow_listanndate = Column(VARCHAR2(8))
    s_fellow_offeringobject = Column(VARCHAR2(200))
    s_fellow_priceuplimit = Column(NUMBER(20,4))
    s_fellow_pricedownlimit = Column(NUMBER(20,4))
    s_seo_code = Column(VARCHAR2(10))
    s_seo_name = Column(VARCHAR2(20))
    s_seo_pe = Column(NUMBER(20,4))
    s_seo_amtbyplacing = Column(NUMBER(20,4))
    s_seo_amttojur = Column(NUMBER(20,4))
    s_seo_holdersubsmode = Column(VARCHAR2(30)
    s_seo_holdersubsrate = Column(NUMBER(20,4))
    ann_dt = Column(VARCHAR2(8))
    pricingmode = Column(NUMBER(9,0))
    s_fellow_orgpricemin = Column(NUMBER(20,4))
    s_fellow_discntratio = Column(NUMBER(20,4))
    s_fellow_date = Column(VARCHAR2(8))
    s_fellow_subinvitationdt = Column(VARCHAR2(8))
    s_fellow_year = Column(VARCHAR2(8))
    s_fellow_objective_code = Column(NUMBER(9,0))
    pricingdate = Column(VARCHAR2(8))
    is_no_public = Column(NUMBER(5,0))
    
