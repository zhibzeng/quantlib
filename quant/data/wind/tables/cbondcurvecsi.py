from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondCurveCSI(BaseModel):
    """
    中证收益率曲线

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    trade_dt: VARCHAR2(8)
        交易日期   
    b_anal_curvenumber: VARCHAR2(5)
        曲线编号   
    b_anal_curvename: VARCHAR2(200)
        曲线名称   
    b_anal_curvetype: VARCHAR2(20)
        曲线类型   1:即期2:到期
    b_anal_curveterm: NUMBER(20,4)
        年限   
    b_anal_yield: NUMBER(20,4)
        收益率(%)   

    """
    __tablename__ = "CBondCurveCSI"
    object_id = Column(VARCHAR2(100), primary_key=True)
    trade_dt = Column(VARCHAR2(8))
    b_anal_curvenumber = Column(VARCHAR2(5))
    b_anal_curvename = Column(VARCHAR2(200))
    b_anal_curvetype = Column(VARCHAR2(20))
    b_anal_curveterm = Column(NUMBER(20,4))
    b_anal_yield = Column(NUMBER(20,4))
    
