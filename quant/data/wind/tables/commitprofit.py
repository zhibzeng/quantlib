from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CommitProfit(BaseModel):
    """
    4.103 中国A股盈利承诺明细表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    event_id: VARCHAR2(40)
        事件ID   
    targetcomp_code: VARCHAR2(40)
        标的公司ID   
    targetcompname: VARCHAR2(100)
        [内部]标的公司名称   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_commitann_dt: VARCHAR2(8)
        承诺公告日   
    report_period: VARCHAR2(8)
        报告期   
    commitnetprofit: NUMBER(20,4)
        承诺净利润(元)   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CommitProfit"
    object_id = Column(VARCHAR2(100), primary_key=True)
    event_id = Column(VARCHAR2(40))
    targetcomp_code = Column(VARCHAR2(40))
    targetcompname = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_info_commitann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    commitnetprofit = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
