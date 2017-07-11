from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondAnalysisCSI(BaseModel):
    """
    中证估值

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    b_info_type: VARCHAR2(50)
        信用类型   
    b_info_listingmarketnumbers: NUMBER(20,4)
        发行市场数   
    b_anal_dirty_csi: NUMBER(20,4)
        计算价格   
    b_anal_yield_csi: NUMBER(20,4)
        计算收益率(%)   
    b_anal_modidura_csi: NUMBER(20,4)
        修正久期   
    b_anal_cnvxty_csi: NUMBER(20,4)
        凸性   
    b_anal_net_csi: NUMBER(20,4)
        净价   
    b_anal_accrint_csi: NUMBER(20,4)
        应计利息   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    b_info_type = Column(VARCHAR2(50))
    b_info_listingmarketnumbers = Column(NUMBER(20,4))
    b_anal_dirty_csi = Column(NUMBER(20,4))
    b_anal_yield_csi = Column(NUMBER(20,4))
    b_anal_modidura_csi = Column(NUMBER(20,4))
    b_anal_cnvxty_csi = Column(NUMBER(20,4))
    b_anal_net_csi = Column(NUMBER(20,4))
    b_anal_accrint_csi = Column(NUMBER(20,4))
    
