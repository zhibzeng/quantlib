from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondCurveCNBD(BaseModel):
    """
    中债登收益率曲线

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    trade_dt: VARCHAR2(8)
        交易日期   
    b_anal_curvenumber: NUMBER(10,0)
        曲线编号   
    b_anal_curvename: VARCHAR2(200)
        曲线名称   
    b_anal_curvetype: VARCHAR2(80)
        曲线类型   1:即期2:到期
    b_anal_curveterm: NUMBER(20,4)
        标准期限(年)   
    b_anal_yield: NUMBER(20,4)
        收益率(%)   

    """
    object_id = Column(VARCHAR2(100))
    trade_dt = Column(VARCHAR2(8))
    b_anal_curvenumber = Column(NUMBER(10,0))
    b_anal_curvename = Column(VARCHAR2(200))
    b_anal_curvetype = Column(VARCHAR2(80))
    b_anal_curveterm = Column(NUMBER(20,4))
    b_anal_yield = Column(NUMBER(20,4))
    
