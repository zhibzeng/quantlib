from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareIncDescription(BaseModel):
    """
    4.95 中国A股股权激励基本资料

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_inc_sequence: VARCHAR2(6)
        序号   
    s_inc_subject: NUMBER(9,0)
        激励标的   1.期权2.股票3.股票增值权
    s_inc_type: NUMBER(9,0)
        激励方式   1.股东转让股票2.股票增值权3.上市公司定向发行股票4.上市公司提取激励基金买入流通A股5.授予期权,行权股票来源为股东转让股票6.授予期权,行权股票来源为上市公司定向发行股票
    s_inc_quantity: NUMBER(20,4)
        激励总数(万股/万份)   
    s_inc_firstinc: VARCHAR2(8)
        起始日   
    s_inc_endinc: VARCHAR2(8)
        到期日   
    s_inc_initexecpri: NUMBER(20,4)
        期权初始行权价格(股票转让价格)   
    s_inc_expirydate: NUMBER(20,4)
        有效期   
    ann_dt: VARCHAR2(8)
        公告日期   
    s_inc_programdescript: VARCHAR2(2000)
        方案说明   
    s_inc_incentsharesaledescript: VARCHAR2(1000)
        激励股票出售说明   
    s_inc_incentcondition: VARCHAR2(1000)
        激励授予条件   
    s_inc_optexespecialcondition: VARCHAR2(1000)
        期权行权特别条件   
    progress: VARCHAR2(10)
        方案进度   
    price_description: VARCHAR2(80)
        价格说明   
    inc_numbers_rate: NUMBER(20,4)
        激励数量占当前总股本比例(%)   
    preplan_ann_date: VARCHAR2(8)
        预案公告日   
    gm_date: VARCHAR2(8)
        股东大会公告日   
    implement_date: VARCHAR2(8)
        首次实施公告日   
    inc_fund_description: VARCHAR2(1000)
        激励基金说明   
    interval_months: NUMBER(20,4)
        授权日与首次可行权日间隔时间(月)   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareIncDescription"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_inc_sequence = Column(VARCHAR2(6))
    s_inc_subject = Column(NUMBER(9,0))
    s_inc_type = Column(NUMBER(9,0))
    s_inc_quantity = Column(NUMBER(20,4))
    s_inc_firstinc = Column(VARCHAR2(8))
    s_inc_endinc = Column(VARCHAR2(8))
    s_inc_initexecpri = Column(NUMBER(20,4))
    s_inc_expirydate = Column(NUMBER(20,4))
    ann_dt = Column(VARCHAR2(8))
    s_inc_programdescript = Column(VARCHAR2(2000))
    s_inc_incentsharesaledescript = Column(VARCHAR2(1000))
    s_inc_incentcondition = Column(VARCHAR2(1000))
    s_inc_optexespecialcondition = Column(VARCHAR2(1000))
    progress = Column(VARCHAR2(10))
    price_description = Column(VARCHAR2(80))
    inc_numbers_rate = Column(NUMBER(20,4))
    preplan_ann_date = Column(VARCHAR2(8))
    gm_date = Column(VARCHAR2(8))
    implement_date = Column(VARCHAR2(8))
    inc_fund_description = Column(VARCHAR2(1000))
    interval_months = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
