from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


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
    object_id = Column(VARCHAR2(100))
    product_name = Column(VARCHAR2(100))
    frequency = Column(VARCHAR2(10))
    runtime = Column(VARCHAR2(100))
    weekly_parameter = Column(VARCHAR2(50))
    
