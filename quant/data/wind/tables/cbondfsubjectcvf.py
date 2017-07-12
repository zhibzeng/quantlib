from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondFSubjectcvf(BaseModel):
    """
    中国国债期货标的券

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        月合约Wind代码   
    dls_windcode: VARCHAR2(40)
        标的券Wind代码   
    b_tbf_cvf: NUMBER(20,8)
        转换因子   交易所公布

    """
    __tablename__ = "CBondFSubjectcvf"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    dls_windcode = Column(VARCHAR2(40))
    b_tbf_cvf = Column(NUMBER(20,8))
    
