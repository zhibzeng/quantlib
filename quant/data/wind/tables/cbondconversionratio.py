from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CBondConversionRatio(BaseModel):
    """
    中国债券回购标准券折算率

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    b_cvn_startdate: VARCHAR2(8)
        开始适用日   
    b_cvn_enddate: VARCHAR2(8)
        结束适用日   
    b_cvn_rateofstdbnd: NUMBER(20,4)
        折算比例   
    b_cvn_cvntperhundred: NUMBER(20,4)
        折合标准券   每张债券折合标准券金额

    """
    __tablename__ = "CBondConversionRatio"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    b_cvn_startdate = Column(VARCHAR2(8))
    b_cvn_enddate = Column(VARCHAR2(8))
    b_cvn_rateofstdbnd = Column(NUMBER(20,4))
    b_cvn_cvntperhundred = Column(NUMBER(20,4))
    
