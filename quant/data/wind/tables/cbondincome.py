from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondIncome(BaseModel):
    """
    中国债券发行主体利润表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_compcode: VARCHAR2(40)
        公司ID   None

    """
    __tablename__ = "CBondIncome"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_compcode = Column(VARCHAR2(40))
    
