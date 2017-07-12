from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareEODDerivativeIndicator(BaseModel):
    """
    中国A股日行情估值指标

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    crncy_code: VARCHAR2(10)
        货币代码   CNY人民币
    s_val_mv: NUMBER(20,4)
        当日总市值   股价*总股本
    s_dq_mv: NUMBER(20,4)
        当日流通市值   
    s_pq_high_52w_: NUMBER(20,4)
        52周最高价   
    s_pq_low_52w_: NUMBER(20,4)
        52周最低价   
    s_val_pe: NUMBER(20,4)
        市盈率(PE)   总市值/净利润
    s_val_pb_new: NUMBER(20,4)
        市净率(PB)   总市值/净资产(LF)
    s_val_pe_ttm: NUMBER(20,4)
        市盈率(PE,TTM)   总市值/净利润(TTM)
    s_val_pcf_ocf: NUMBER(20,4)
        市现率(PCF,经营现金流)   
    s_val_pcf_ocfttm: NUMBER(20,4)
        市现率(PCF,经营现金流TTM)   
    s_val_pcf_ncf: NUMBER(20,4)
        市现率(PCF,现金净流量)   
    s_val_pcf_ncfttm: NUMBER(20,4)
        市现率(PCF,现金净流量TTM)   
    s_val_ps: NUMBER(20,4)
        市销率(PS)   
    s_val_ps_ttm: NUMBER(20,4)
        市销率(PS,TTM)   
    s_dq_turn: NUMBER(20,4)
        换手率   
    s_dq_freeturnover: NUMBER(20,4)
        换手率(基准.自由流通股本)   
    tot_shr_today: NUMBER(20,4)
        当日总股本   
    float_a_shr_today: NUMBER(20,4)
        当日流通股本   
    s_dq_close_today: NUMBER(20,4)
        当日收盘价   
    s_price_div_dps: NUMBER(20,4)
        股价/每股派息   
    s_pq_adjhigh_52w: NUMBER(20,4)
        52周最高价(复权)   
    s_pq_adjlow_52w: NUMBER(20,4)
        52周最低价(复权)   

    """
    __tablename__ = "AShareEODDerivativeIndicator"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    crncy_code = Column(VARCHAR2(10))
    s_val_mv = Column(NUMBER(20,4))
    s_dq_mv = Column(NUMBER(20,4))
    s_pq_high_52w_ = Column(NUMBER(20,4))
    s_pq_low_52w_ = Column(NUMBER(20,4))
    s_val_pe = Column(NUMBER(20,4))
    s_val_pb_new = Column(NUMBER(20,4))
    s_val_pe_ttm = Column(NUMBER(20,4))
    s_val_pcf_ocf = Column(NUMBER(20,4))
    s_val_pcf_ocfttm = Column(NUMBER(20,4))
    s_val_pcf_ncf = Column(NUMBER(20,4))
    s_val_pcf_ncfttm = Column(NUMBER(20,4))
    s_val_ps = Column(NUMBER(20,4))
    s_val_ps_ttm = Column(NUMBER(20,4))
    s_dq_turn = Column(NUMBER(20,4))
    s_dq_freeturnover = Column(NUMBER(20,4))
    tot_shr_today = Column(NUMBER(20,4))
    float_a_shr_today = Column(NUMBER(20,4))
    s_dq_close_today = Column(NUMBER(20,4))
    s_price_div_dps = Column(NUMBER(20,4))
    s_pq_adjhigh_52w = Column(NUMBER(20,4))
    s_pq_adjlow_52w = Column(NUMBER(20,4))
    
