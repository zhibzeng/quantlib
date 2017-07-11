from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareFinancialExpense(BaseModel):
    """
    中国A股财务费用明细

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
    statement_typecode: NUMBER(9,0)
        报表类型代码   报表类型:408001000:合并报表408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408009000:

    """
    __tablename__ = "AShareFinancialExpense"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_typecode = Column(NUMBER(9,0))
    
