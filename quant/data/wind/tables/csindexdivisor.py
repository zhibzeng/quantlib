from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CSIndexDivisor(BaseModel):
    """
    4.207 中证指数除数

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        指数Wind代码   
    trade_dt: VARCHAR2(8)
        除数生效日期英文：EffectiveDate   
    i_cur_divisor: NUMBER(20,4)
        原除数英文：CurrentDivisor   
    i_new_divisor: NUMBER(20,4)
        调整后除数英文：NewDivisor   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CSIndexDivisor"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    i_cur_divisor = Column(NUMBER(20,4))
    i_new_divisor = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
