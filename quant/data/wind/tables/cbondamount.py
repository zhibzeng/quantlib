from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CBondAmount(BaseModel):
    """
    中国债券份额变动

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_enddate: VARCHAR2(8)
        截止日期   
    b_info_changereason: NUMBER(9,0)
        变动原因   1本金提前兑付2到期3回售4可转债上市5上市6赎回7增发8债券调换9转债转股
    b_info_outstandingbalance: NUMBER(20,4)
        债券份额(亿元)   

    """
    __tablename__ = "CBondAmount"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_enddate = Column(VARCHAR2(8))
    b_info_changereason = Column(NUMBER(9,0))
    b_info_outstandingbalance = Column(NUMBER(20,4))
    
