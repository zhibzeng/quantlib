from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class MergerEvent(BaseModel):
    """
    并购事件

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    event_id: VARCHAR2(20)
        并购事件ID   
    s_info_windcode: VARCHAR2(200)
        参与方名称或代码   
    underlying: VARCHAR2(200)
        交易标的   
    trade_value: NUMBER(20，4)
        交易总价值(万元)   
    cash_payment: NUMBER(20，4)
        买方支付现金(万元)   
    crncy_code: VARCHAR2(10)
        货币代码   注1
    ann_date: VARCHAR2(8)
        首次披露日期   
    update_date: VARCHAR2(8)
        最新披露日期   
    completion_date: VARCHAR2(8)
        交易完成日期   

    """
    object_id = Column(VARCHAR2(100))
    event_id = Column(VARCHAR2(20))
    s_info_windcode = Column(VARCHAR2(200))
    underlying = Column(VARCHAR2(200))
    trade_value = Column(NUMBER(20，4))
    cash_payment = Column(NUMBER(20，4))
    crncy_code = Column(VARCHAR2(10))
    ann_date = Column(VARCHAR2(8))
    update_date = Column(VARCHAR2(8))
    completion_date = Column(VARCHAR2(8))
    
