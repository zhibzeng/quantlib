from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CWarrantHolder(BaseModel):
    """
    中国权证持有人

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    f_info_windcode: VARCHAR2(40)
        Wind代码   
    end_date: VARCHAR2(8)
        日期   
    holder: VARCHAR2(200)
        持有人   

    """
    __tablename__ = "CWarrantHolder"
    object_id = Column(VARCHAR2(100), primary_key=True)
    f_info_windcode = Column(VARCHAR2(40))
    end_date = Column(VARCHAR2(8))
    holder = Column(VARCHAR2(200))
    
