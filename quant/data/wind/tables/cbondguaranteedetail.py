from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondGuaranteeDetail(BaseModel):
    """
    4.133 债券发行人担保数据（明细）

    Attributes
    ----------
    object_id: VARCHAR2(38)
        对象ID   
    s_info_compcode: VARCHAR2(10)
        公司id   
    enddate: VARCHAR2(8)
        截止日期   
    ann_date: VARCHAR2(8)
        公告日期   
    company_guaranteed: VARCHAR2(100)
        被担保公司名称   
    amountofguarantee: NUMBER(20,0)
        担保金额(万元)   
    guaranteecompanytype: VARCHAR2(20)
        担保公司类别   内部;外部:
    crncy_code: VARCHAR2(10)
        货币代码   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondGuaranteeDetail"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_compcode = Column(VARCHAR2(10))
    enddate = Column(VARCHAR2(8))
    ann_date = Column(VARCHAR2(8))
    company_guaranteed = Column(VARCHAR2(100))
    amountofguarantee = Column(NUMBER(20,0))
    guaranteecompanytype = Column(VARCHAR2(20))
    crncy_code = Column(VARCHAR2(10))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
