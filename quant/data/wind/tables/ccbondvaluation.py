from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CCBondValuation(BaseModel):
    """
    4.141 中国可转债衍生指标

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    cb_anal_accrueddays: NUMBER(20,4)
        已计息天数   分析日－计息起始日－计息起始日与分析日之间所含闰年2月29日的天数＋1
    cb_anal_accruedinterest: NUMBER(20,4)
        应计利息   当期票面利率现金流*已计利息天数/365
    cb_anal_ptm: NUMBER(20,4)
        剩余期限(年)   到期日-分析日
    cb_anal_curyield: NUMBER(20,4)
        当期收益率   当期票面利率*面值/转债全价
    cb_anal_ytm: NUMBER(20,4)
        纯债到期收益率   ∑(各期利息＋面值)/(1+到期收益率)
    cb_anal_strbvalue: NUMBER(20,4)
        纯债价值   ∑各期息票现金流折现+本金折现+期末回售补偿价值
    cb_anal_strbpremium: NUMBER(20,4)
        纯债溢价   转债价格-纯债价值
    cb_anal_strbpremiumratio: NUMBER(20,4)
        纯债溢价率   (转债价格－纯债价值)/纯债价值×100％
    cb_anal_convprice: NUMBER(20,4)
        转股价   
    cb_anal_convratio: NUMBER(20,4)
        转股比例   100/转股价格
    cb_anal_convvalue: NUMBER(20,4)
        转股价值   指定日正股收盘价*[100/最新转股价格]
    cb_anal_convpremium: NUMBER(20,4)
        转股溢价   指定日转债收盘价－转换价值
    cb_anal_convpremiumratio: NUMBER(20,4)
        转股溢价率   [指定日转债收盘价－转换价值]/转换价值
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CCBondValuation"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    cb_anal_accrueddays = Column(NUMBER(20,4))
    cb_anal_accruedinterest = Column(NUMBER(20,4))
    cb_anal_ptm = Column(NUMBER(20,4))
    cb_anal_curyield = Column(NUMBER(20,4))
    cb_anal_ytm = Column(NUMBER(20,4))
    cb_anal_strbvalue = Column(NUMBER(20,4))
    cb_anal_strbpremium = Column(NUMBER(20,4))
    cb_anal_strbpremiumratio = Column(NUMBER(20,4))
    cb_anal_convprice = Column(NUMBER(20,4))
    cb_anal_convratio = Column(NUMBER(20,4))
    cb_anal_convvalue = Column(NUMBER(20,4))
    cb_anal_convpremium = Column(NUMBER(20,4))
    cb_anal_convpremiumratio = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
