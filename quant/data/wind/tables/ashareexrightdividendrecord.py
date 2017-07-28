from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareEXRightDividendRecord(BaseModel):
    """
    4.24 中国A股除权除息记录

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ex_date: VARCHAR2(8)
        除权除息日   
    ex_type: VARCHAR2(40)
        除权类型   
    ex_description: VARCHAR2(100)
        除权说明   
    cash_dividend_ratio: NUMBER(15,4)
        派息比例   
    bonus_share_ratio: NUMBER(15,4)
        送股比例   
    rightsissue_ratio: NUMBER(15,4)
        配股比例   
    rightsissue_price: NUMBER(15,4)
        配股价格   
    conversed_ratio: NUMBER(15,4)
        转增比例   
    seo_price: NUMBER(15,4)
        增发价格   
    seo_ratio: NUMBER(15,4)
        增发比例   
    consolidate_split_ratio: NUMBER(20,6)
        缩减比例   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareEXRightDividendRecord"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ex_date = Column(VARCHAR2(8))
    ex_type = Column(VARCHAR2(40))
    ex_description = Column(VARCHAR2(100))
    cash_dividend_ratio = Column(NUMBER(15,4))
    bonus_share_ratio = Column(NUMBER(15,4))
    rightsissue_ratio = Column(NUMBER(15,4))
    rightsissue_price = Column(NUMBER(15,4))
    conversed_ratio = Column(NUMBER(15,4))
    seo_price = Column(NUMBER(15,4))
    seo_ratio = Column(NUMBER(15,4))
    consolidate_split_ratio = Column(NUMBER(20,6))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
