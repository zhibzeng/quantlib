from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


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
    object_id = Column(VARCHAR2(100))
    f_info_windcode = Column(VARCHAR2(40))
    end_date = Column(VARCHAR2(8))
    holder = Column(VARCHAR2(200))
    
