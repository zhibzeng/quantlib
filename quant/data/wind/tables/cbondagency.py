from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondAgency(BaseModel):
    """
    中国债券中介机构

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    b_info_windcode: VARCHAR2(40)
        Wind代码   
    b_info_redemptionprice: NUMBER(20,4)
        赎回价   

    """
    object_id = Column(VARCHAR2(100))
    b_info_windcode = Column(VARCHAR2(40))
    b_info_redemptionprice = Column(NUMBER(20,4))
    
