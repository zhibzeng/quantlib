from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondAnalysisCNBD(BaseModel):
    """
    中债登估值

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    b_anal_matu_cnbd: NUMBER(20,4)
        待偿期(年)   
    b_anal_dirty_cnbd: NUMBER(20,4)
        估价全价   
    b_anal_accrint_cnbd: NUMBER(20,4)
        应计利息   
    b_anal_net_cnbd: NUMBER(20,4)
        估价净价   
    b_anal_yield_cnbd: NUMBER(20,4)
        估价收益率(%)   
    b_anal_modidura_cnbd: NUMBER(20,4)
        估价修正久期   
    b_anal_cnvxty_cnbd: NUMBER(20,4)
        估价凸性   
    b_anal_vobp_cnbd: NUMBER(20,4)
        估价基点价值   
    b_anal_sprdura_cnbd: NUMBER(20,4)
        估价利差久期   
    b_anal_sprcnxt_cnbd: NUMBER(20,4)
        估价利差凸性   
    b_anal_accrintclose_cnbd: NUMBER(20,4)
        日终应计利息   
    b_anal_price: NUMBER(20,4)
        市场全价   
    b_anal_netprice: NUMBER(20,4)
        市场净价   
    b_anal_yield: NUMBER(20,4)
        市场收益率(%)   
    b_anal_modifiedduration: NUMBER(20,4)
        市场修正久期   
    b_anal_convexity: NUMBER(20,4)
        市场凸性   
    b_anal_bpvalue: NUMBER(20,4)
        市场基点价值   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    b_anal_matu_cnbd = Column(NUMBER(20,4))
    b_anal_dirty_cnbd = Column(NUMBER(20,4))
    b_anal_accrint_cnbd = Column(NUMBER(20,4))
    b_anal_net_cnbd = Column(NUMBER(20,4))
    b_anal_yield_cnbd = Column(NUMBER(20,4))
    b_anal_modidura_cnbd = Column(NUMBER(20,4))
    b_anal_cnvxty_cnbd = Column(NUMBER(20,4))
    b_anal_vobp_cnbd = Column(NUMBER(20,4))
    b_anal_sprdura_cnbd = Column(NUMBER(20,4))
    b_anal_sprcnxt_cnbd = Column(NUMBER(20,4))
    b_anal_accrintclose_cnbd = Column(NUMBER(20,4))
    b_anal_price = Column(NUMBER(20,4))
    b_anal_netprice = Column(NUMBER(20,4))
    b_anal_yield = Column(NUMBER(20,4))
    b_anal_modifiedduration = Column(NUMBER(20,4))
    b_anal_convexity = Column(NUMBER(20,4))
    b_anal_bpvalue = Column(NUMBER(20,4))
    
