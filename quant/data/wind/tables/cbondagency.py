from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


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
    b_info_bgndt: VARCHAR2(8)
        起始日期   
    b_info_enddt: VARCHAR2(8)
        截止日期   
    b_info_trnsrt: NUMBER(20,4)
        触发比例(%)   

    """
    __tablename__ = "CBondAgency"
    object_id = Column(VARCHAR2(100), primary_key=True)
    b_info_windcode = Column(VARCHAR2(40))
    b_info_redemptionprice = Column(NUMBER(20,4))
    b_info_bgndt = Column(VARCHAR2(8))
    b_info_enddt = Column(VARCHAR2(8))
    b_info_trnsrt = Column(NUMBER(20,4))
    
