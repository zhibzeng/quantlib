from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class FileSyncTimeSchedule(BaseModel):
    """
    FileSync调度计划

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    product_name: VARCHAR2(100)
        产品包名   
    frequency: VARCHAR2(10)
        频率   day,weekly,month,quarter,year
    runtime: VARCHAR2(100)
        时间   
    weekly_parameter: VARCHAR2(50)
        周(参数)   0-6:周日-周一

    """
    __tablename__ = "FileSyncTimeSchedule"
    object_id = Column(VARCHAR2(100), primary_key=True)
    product_name = Column(VARCHAR2(100))
    frequency = Column(VARCHAR2(10))
    runtime = Column(VARCHAR2(100))
    weekly_parameter = Column(VARCHAR2(50))
    
