from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondRepo(BaseModel):
    """
    中国央行回购交易

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    trade_dt: VARCHAR2(8)
        交易日期   
    b_info_term: NUMBER(20,4)
        期限(天)   
    b_tender_interestrate: NUMBER(20,4)
        招标利率(%)   
    b_tender_amount: NUMBER(20,4)
        招标数量(亿元)   
    b_tender_method: NUMBER(9,0)
        招标方式   1价格招标2利率招标3数量招标
    b_info_repo_type: NUMBER(9,0)
        回购类型   517001000：正回购517002000：逆回购

    """
    object_id = Column(VARCHAR2(100))
    trade_dt = Column(VARCHAR2(8))
    b_info_term = Column(NUMBER(20,4))
    b_tender_interestrate = Column(NUMBER(20,4))
    b_tender_amount = Column(NUMBER(20,4))
    b_tender_method = Column(NUMBER(9,0))
    b_info_repo_type = Column(NUMBER(9,0))
    
