from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


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

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    wind_code = Column(VARCHAR2(40))
    s_div_progress = Column(VARCHAR2(10))
    stk_dvd_per_sh = Column(Number(20,4))
    cash_dvd_per_sh_pre_tax = Column(Number(20,6))
    cash_dvd_per_sh_after_tax = Column(Number(20,6))
    eqy_record_dt = Column(VARCHAR2(8))
    
