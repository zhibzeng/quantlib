from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


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

    """
    object_id = Column(VARCHAR2(100))
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
    
