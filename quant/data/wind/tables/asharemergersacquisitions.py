from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareMergersAcquisitions(BaseModel):
    """
    4.109 中国A股收购兼并

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        信息披露方万得代码   
    targetofacquisn: VARCHAR2(100)
        被收购方名称   
    targetofacquisn_disclosure: VARCHAR2(40)
        被收购方与披露方关系   
    acquiringfirm: VARCHAR2(100)
        收购方名称   
    acquiringfirm_disclosure: VARCHAR2(40)
        收购方与披露方关系   
    progress: VARCHAR2(10)
        方案进度   
    crncy_code: VARCHAR2(10)
        货币代码   
    paymentmethod: VARCHAR2(40)
        支付方式   
    trade_dt: VARCHAR2(8)
        交易日期   
    tradingamount: NUMBER(20,4)
        交易金额(万元)   
    is_reldpartransactions: NUMBER(1,0)
        是否关联交易   
    first_dt: VARCHAR2(8)
        首次公告日期   
    ann_dt: VARCHAR2(8)
        最新公告日期   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareMergersAcquisitions"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    targetofacquisn = Column(VARCHAR2(100))
    targetofacquisn_disclosure = Column(VARCHAR2(40))
    acquiringfirm = Column(VARCHAR2(100))
    acquiringfirm_disclosure = Column(VARCHAR2(40))
    progress = Column(VARCHAR2(10))
    crncy_code = Column(VARCHAR2(10))
    paymentmethod = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    tradingamount = Column(NUMBER(20,4))
    is_reldpartransactions = Column(NUMBER(1,0))
    first_dt = Column(VARCHAR2(8))
    ann_dt = Column(VARCHAR2(8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
