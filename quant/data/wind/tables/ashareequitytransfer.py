from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareEquityTransfer(BaseModel):
    """
    中国A股股权转让

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        信息披露方万得代码   
    transferor: VARCHAR2(100)
        转让方名称   
    transferor_disclosure: VARCHAR2(40)
        转让方与披露方关系   
    transferee: VARCHAR2(100)
        受让方名称   
    transferee_disclosure: VARCHAR2(40)
        受让方与披露方关系   
    targetcompany: VARCHAR2(100)
        标的公司   
    targetcompany_disclosure: VARCHAR2(40)
        标的方与披露方关系   
    progress: VARCHAR2(10)
        方案进度   
    trade_dt: VARCHAR2(8)
        交易日期   
    transfermethod: VARCHAR2(40)
        转让方式   
    sharecategorybeftransfer: VARCHAR2(40)
        转让前股份性质   
    sharecategoryafttransfer: VARCHAR2(40)
        转让后股份性质   
    transferredshares: NUMBER(20,4)
        转让数量(万股)   
    transferproporation: NUMBER(20,4)
        本次转让比例(%)   
    transfeefishareholding: NUMBER(20,4)
        受让方最终持股比例(%)   
    transferpricepershare: NUMBER(20,4)
        每股转让价格(元)   
    tradingamount: NUMBER(20,4)
        交易金额(万元)   
    crncy_code: VARCHAR2(10)
        货币代码   
    is_transferred: NUMBER(5,0)
        是否过户   0=未过户1=已过户
    is_reldpartransactions: NUMBER(1,0)
        是否关联交易   1=是0=否
    first_dt: VARCHAR2(8)
        首次公告日期   
    sasacdate: VARCHAR2(8)
        国资委批准公告日期   
    approveddate: VARCHAR2(8)
        证监会批准公告日期   
    ann_dt: VARCHAR2(8)
        公告日期   

    """
    __tablename__ = "AShareEquityTransfer"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    transferor = Column(VARCHAR2(100))
    transferor_disclosure = Column(VARCHAR2(40))
    transferee = Column(VARCHAR2(100))
    transferee_disclosure = Column(VARCHAR2(40))
    targetcompany = Column(VARCHAR2(100))
    targetcompany_disclosure = Column(VARCHAR2(40))
    progress = Column(VARCHAR2(10))
    trade_dt = Column(VARCHAR2(8))
    transfermethod = Column(VARCHAR2(40))
    sharecategorybeftransfer = Column(VARCHAR2(40))
    sharecategoryafttransfer = Column(VARCHAR2(40))
    transferredshares = Column(NUMBER(20,4))
    transferproporation = Column(NUMBER(20,4))
    transfeefishareholding = Column(NUMBER(20,4))
    transferpricepershare = Column(NUMBER(20,4))
    tradingamount = Column(NUMBER(20,4))
    crncy_code = Column(VARCHAR2(10))
    is_transferred = Column(NUMBER(5,0))
    is_reldpartransactions = Column(NUMBER(1,0))
    first_dt = Column(VARCHAR2(8))
    sasacdate = Column(VARCHAR2(8))
    approveddate = Column(VARCHAR2(8))
    ann_dt = Column(VARCHAR2(8))
    
