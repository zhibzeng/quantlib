from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareMonthlyReportsofBrokers(BaseModel):
    """
    中国A股券商月报

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    report_period: VARCHAR2(8)
        报告期   
    statement_typecode: NUMBER(9,0)
        报表类型代码   母公司报表
    acc_sta_code: NUMBER(1,0)
        会计准则代码   1：旧会计准则2：新会计准则
    iflisted_data: NUMBER(5,0)
        是否上市后数据   0：否1：是
    oper_rev: NUMBER(20,4)
        营业收入   
    net_profit_incl_min_int_inc: NUMBER(20,4)
        净利润(含少数股东权益)   
    net_profit_excl_min_int_inc: NUMBER(20,4)
        净利润(不含少数股东权益)   
    tot_shrhldr_eqy_excl_min_int: NUMBER(20,4)
        股东权益合计(不含少数股东权益)   
    tot_shrhldr_eqy_incl_min_int: NUMBER(20,4)
        股东权益合计(含少数股东权益)   
    s_info_compname: VARCHAR2(100)
        公司名称   
    s_info_compcode: VARCHAR2(10)
        公司ID   

    """
    __tablename__ = "AShareMonthlyReportsofBrokers"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_typecode = Column(NUMBER(9,0))
    acc_sta_code = Column(NUMBER(1,0))
    iflisted_data = Column(NUMBER(5,0))
    oper_rev = Column(NUMBER(20,4))
    net_profit_incl_min_int_inc = Column(NUMBER(20,4))
    net_profit_excl_min_int_inc = Column(NUMBER(20,4))
    tot_shrhldr_eqy_excl_min_int = Column(NUMBER(20,4))
    tot_shrhldr_eqy_incl_min_int = Column(NUMBER(20,4))
    s_info_compname = Column(VARCHAR2(100))
    s_info_compcode = Column(VARCHAR2(10))
    
