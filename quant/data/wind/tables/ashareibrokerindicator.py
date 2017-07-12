from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareIBrokerIndicator(BaseModel):
    """
    中国A股券商专用指标

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    report_period: VARCHAR2(8)
        报告期   
    statement_type: VARCHAR2(40)
        报表类型   报表类型:408001000:合并报

    """
    __tablename__ = "AShareIBrokerIndicator"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(40))
    
