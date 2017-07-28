from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareFinancialExpense(BaseModel):
    """
    4.58 中国A股财务费用明细

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
        报表类型代码   报表类型:408001000:合并报表408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408009000:母公司报表(调整)408010000:母公司报表(更正前)
    s_stmnote_intexp: NUMBER(20,4)
        利息支出(元)   
    s_stmnote_intinc: NUMBER(20,4)
        减：利息收入(元)   
    s_stmnote_exch: NUMBER(20,4)
        汇兑损益(元)   
    s_stmnote_fee: NUMBER(20,4)
        手续费(元)   
    s_stmnote_others: NUMBER(20,4)
        其他(元)   
    s_stmnote_finexp: NUMBER(20,4)
        合计(元)   
    s_stmnote_finexp_1: NUMBER(20,4)
        减：利息资本化金额(元)   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareFinancialExpense"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    report_period = Column(VARCHAR2(8))
    statement_typecode = Column(NUMBER(9,0))
    s_stmnote_intexp = Column(NUMBER(20,4))
    s_stmnote_intinc = Column(NUMBER(20,4))
    s_stmnote_exch = Column(NUMBER(20,4))
    s_stmnote_fee = Column(NUMBER(20,4))
    s_stmnote_others = Column(NUMBER(20,4))
    s_stmnote_finexp = Column(NUMBER(20,4))
    s_stmnote_finexp_1 = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
