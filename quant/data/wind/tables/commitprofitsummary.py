from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CommitProfitSummary(BaseModel):
    """
    中国A股盈利承诺汇总表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    event_id: VARCHAR2(40)
        事件ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    report_period: VARCHAR2(8)
        报告期   
    s_info_commitann_dt: VARCHAR2(8)
        承诺公告日   
    ann_dt: VARCHAR2(8)
        最新公告日   
    targetcomp: VARCHAR2(400)
        标的公司   
    commitnetprofit: NUMBER(20,4)
        承诺净利润(元)   
    actualnetprofit: NUMBER(20,4)
        实际净利润(元)   
    iscommitprofitsupply: NUMBER(1,0)
        是否承诺利润补充   
    isneedsupply: NUMBER(1,0)
        是否需要补充   
    supplycontent: NUMBER(9,0)
        补偿内容代码   274004000
    injectedassetnetprofitest: NUMBER(20,4)
        注入资产净利润预测(元)   274001000现金补偿274002000股份回购274003000现金补偿,股份回购
    earningest: NUMBER(20,4)
        上市公司盈利预测(元)   
    supplytype: NUMBER(9,0)
        盈利补偿方法代码   

    """
    __tablename__ = "CommitProfitSummary"
    object_id = Column(VARCHAR2(100), primary_key=True)
    event_id = Column(VARCHAR2(40))
    s_info_windcode = Column(VARCHAR2(40))
    report_period = Column(VARCHAR2(8))
    s_info_commitann_dt = Column(VARCHAR2(8))
    ann_dt = Column(VARCHAR2(8))
    targetcomp = Column(VARCHAR2(400))
    commitnetprofit = Column(NUMBER(20,4))
    actualnetprofit = Column(NUMBER(20,4))
    iscommitprofitsupply = Column(NUMBER(1,0))
    isneedsupply = Column(NUMBER(1,0))
    supplycontent = Column(NUMBER(9,0))
    injectedassetnetprofitest = Column(NUMBER(20,4))
    earningest = Column(NUMBER(20,4))
    supplytype = Column(NUMBER(9,0))
    
