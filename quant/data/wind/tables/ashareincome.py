from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareIncome(BaseModel):
    """
    中国A股利润表

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    wind_code: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    report_period: VARCHAR2(8)
        报告期   
    statement_type: VARCHAR2(10)
        报表类型   报表类型:408001000:合并报表408002000:合并报表(单季度)408003000:合并报表(单季度调整)408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408007000:母公司报表(单季度)408008000:母公司报

    """
    __tablename__ = "AShareIncome"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    wind_code = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_type = Column(VARCHAR2(10))
    
