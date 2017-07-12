from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondFValuation(BaseModel):
    """
    中国国债期货可交割券衍生指标

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        月合约Wind代码   
    dls_windcode: VARCHAR2(40)
        可交割券Wind代码   
    trade_dt: VARCHAR2(8)
        日期   
    dl_interest: NUMBER(24,8)
        交割利息   
    intervalinterest: NUMBER(24,8)
        区间利息   
    dl_cost: NUMBER(20,4)
        交割成本   
    fs_spread: NUMBER(20,4)
        期现价差   
    irr: NUMBER(20,4)
        IRR   
    rt_spread: NUMBER(20,4)
        基差   

    """
    __tablename__ = "CBondFValuation"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    dls_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    dl_interest = Column(NUMBER(24,8))
    intervalinterest = Column(NUMBER(24,8))
    dl_cost = Column(NUMBER(20,4))
    fs_spread = Column(NUMBER(20,4))
    irr = Column(NUMBER(20,4))
    rt_spread = Column(NUMBER(20,4))
    
