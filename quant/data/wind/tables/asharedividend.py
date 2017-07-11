from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareDividend(BaseModel):
    """
    中国A股分红

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    wind_code: VARCHAR2(40)
        Wind代码   
    s_div_progress: VARCHAR2(10)
        方案进度   1.董事会预案2.股东大会通过3.实施4.未通过12.停止实施17.股东提议19.董事会预案预披露
    stk_dvd_per_sh: Number(20,4)
        每股送转   
    cash_dvd_per_sh_pre_tax: Number(20,6)
        每股派息(税前)(元)   
    cash_dvd_per_sh_after_tax: Number(20,6)
        每股派息(税后)(元)   
    eqy_record_dt: VARCHAR2(8)
        股权登记日   
    ex_dt: VARCHAR2(8)
        除权除息日   
    dvd_payout_dt: VARCHAR2(8)
        派息日   
    listing_dt_of_dvd_shr: VARCHAR2(8)
        红股上市日   
    s_div_prelandate: VARCHAR2(8)
        预案公告日   
    s_div_smtgdate: VARCHAR2(8)
        股东大会公告日   
    dvd_ann_dt: VARCHAR2(8)
        分红实施公告日   
    s_div_basedate: VARCHAR2(8)
        基准日期   
    s_div_baseshare: Number(20,4)
        基准股本(万股)   
    crncy_code: VARCHAR2(10)
        货币代码   
    ann_dt: VARCHAR2(8)
        最新公告日期   
    is_changed: Number(5,0)
        方案是否变更   
    report_period: VARCHAR2(8)
        分红年度   
    s_div_change: VARCHAR2(500)
        方案变更说明   
    s_div_bonusrate: Number(20,8)
        每股送股比例   
    s_div_conversedrate: Number(20,8)
        每股转增比例   

    """
    __tablename__ = "AShareDividend"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    wind_code = Column(VARCHAR2(40))
    s_div_progress = Column(VARCHAR2(10))
    stk_dvd_per_sh = Column(Number(20,4))
    cash_dvd_per_sh_pre_tax = Column(Number(20,6))
    cash_dvd_per_sh_after_tax = Column(Number(20,6))
    eqy_record_dt = Column(VARCHAR2(8))
    ex_dt = Column(VARCHAR2(8))
    dvd_payout_dt = Column(VARCHAR2(8))
    listing_dt_of_dvd_shr = Column(VARCHAR2(8))
    s_div_prelandate = Column(VARCHAR2(8))
    s_div_smtgdate = Column(VARCHAR2(8))
    dvd_ann_dt = Column(VARCHAR2(8))
    s_div_basedate = Column(VARCHAR2(8))
    s_div_baseshare = Column(Number(20,4))
    crncy_code = Column(VARCHAR2(10))
    ann_dt = Column(VARCHAR2(8))
    is_changed = Column(Number(5,0))
    report_period = Column(VARCHAR2(8))
    s_div_change = Column(VARCHAR2(500))
    s_div_bonusrate = Column(Number(20,8))
    s_div_conversedrate = Column(Number(20,8))
    
