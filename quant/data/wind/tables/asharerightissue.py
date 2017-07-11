from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareRightIssue(BaseModel):
    """
    中国A股配股

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_rightsissue_progress: VARCHAR2(10)
        方案进度   1.董事会预案2.股东大会通过3.实施4.未通过5.证监会批准8.国资委批准12.停止实施
    s_rightsissue_price: NUMBER(20,4)
        配股价格(元)   
    s_rightsissue_ratio: NUMBER(20,4)
        配股比例   
    s_rightsissue_amount: NUMBER(20,4)
        配股计划数量(万股)   
    s_rightsissue_amountact: NUMBER(20,4)
        配股实际数量(万股)   
    s_rightsissue_netcollection: NUMBER(20,4)
        募集资金(元)   含发行费用
    s_rightsissue_regdateshareb: VARCHAR2(8)
        股权登记日   
    s_rightsissue_exdividenddate: VARCHAR2(8)
        除权日   
    s_rightsissue_listeddate: VARCHAR2(8)
        配股上市日   
    s_rightsissue_paystartdate: VARCHAR2(8)
        缴款起始日   
    s_rightsissue_payenddate: VARCHAR2(8)
        缴款终止日   
    s_rightsissue_preplandate: VARCHAR2(8)
        预案公告日   
    s_rightsissue_smtganncedate: VARCHAR2(8)
        股东大会公告日   
    s_rightsissue_passdate: VARCHAR2(8)
        发审委通过公告日   发审委审核通过的公告日
    s_rightsissue_approveddate: VARCHAR2(8)
        证监会核准公告日   证监会核准发行的公告日
    s_rightsissue_anncedate: VARCHAR2(8)
        配股实施公告日   
    s_rightsissue_resultdate: VARCHAR2(8)
        配股结果公告日   
    s_rightsissue_listanndate: VARCHAR2(8)
        上市公告日   
    s_rightsissue_guarantor: VARCHAR2(8)
        基准年度   
    s_rightsissue_guartype: NUMBER(20,4)
        基准股本(万股)   
    s_rightsissue_code: VARCHAR2(10)
        配售代码   
    ann_dt: VARCHAR2(8)
        最新公告日期   
    s_rightsissue_year: VARCHAR2(8)
        配股年度   
    s_rightsissue_content: VARCHAR2(150)
        配股说明   

    """
    __tablename__ = "AShareRightIssue"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_rightsissue_progress = Column(VARCHAR2(10))
    s_rightsissue_price = Column(NUMBER(20,4))
    s_rightsissue_ratio = Column(NUMBER(20,4))
    s_rightsissue_amount = Column(NUMBER(20,4))
    s_rightsissue_amountact = Column(NUMBER(20,4))
    s_rightsissue_netcollection = Column(NUMBER(20,4))
    s_rightsissue_regdateshareb = Column(VARCHAR2(8))
    s_rightsissue_exdividenddate = Column(VARCHAR2(8))
    s_rightsissue_listeddate = Column(VARCHAR2(8))
    s_rightsissue_paystartdate = Column(VARCHAR2(8))
    s_rightsissue_payenddate = Column(VARCHAR2(8))
    s_rightsissue_preplandate = Column(VARCHAR2(8))
    s_rightsissue_smtganncedate = Column(VARCHAR2(8))
    s_rightsissue_passdate = Column(VARCHAR2(8))
    s_rightsissue_approveddate = Column(VARCHAR2(8))
    s_rightsissue_anncedate = Column(VARCHAR2(8))
    s_rightsissue_resultdate = Column(VARCHAR2(8))
    s_rightsissue_listanndate = Column(VARCHAR2(8))
    s_rightsissue_guarantor = Column(VARCHAR2(8))
    s_rightsissue_guartype = Column(NUMBER(20,4))
    s_rightsissue_code = Column(VARCHAR2(10))
    ann_dt = Column(VARCHAR2(8))
    s_rightsissue_year = Column(VARCHAR2(8))
    s_rightsissue_content = Column(VARCHAR2(150))
    
