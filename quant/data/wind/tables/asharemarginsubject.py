from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareMarginSubject(BaseModel):
    """
    中国A股融资融券标的及担保物

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_margin_sharetype: NUMBER(9,0)
        融资融券相关证券类型代码   244000001：融资标的；244000002：融券标的；244000003：担保物
    s_margin_effectdate: VARCHAR2(8)
        生效日   
    s_margin_elimindate: VARCHAR2(8)
        剔除日   
    s_margin_marginrate: NUMBER(20,4)
        保证金比例   
    s_margin_conversionrate: NUMBER(20,4)
        折算率   
    s_margin_rateeffectdate: VARCHAR2(8)
        保证金比例或折算率生效日   

    """
    __tablename__ = "AShareMarginSubject"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_margin_sharetype = Column(NUMBER(9,0))
    s_margin_effectdate = Column(VARCHAR2(8))
    s_margin_elimindate = Column(VARCHAR2(8))
    s_margin_marginrate = Column(NUMBER(20,4))
    s_margin_conversionrate = Column(NUMBER(20,4))
    s_margin_rateeffectdate = Column(VARCHAR2(8))
    
