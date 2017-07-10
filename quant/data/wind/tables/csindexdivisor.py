from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CSIndexDivisor(BaseModel):
    """
    中证指数除数

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

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    i_cur_divisor = Column(NUMBER(20,4))
    i_new_divisor = Column(NUMBER(20,4))
    
