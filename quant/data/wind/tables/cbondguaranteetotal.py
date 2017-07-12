from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondGuaranteeTotal(BaseModel):
    """
    债券发行人担保数据（合计）

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
    guar_balance: NUMBER(20,0)
        担保余额(亿元)   
    guar_inwards: NUMBER(20,0)
        对内担保余额(亿元)   
    guar_outwards: NUMBER(20,0)
        对外担保余额(亿元)   
    memo: VARCHAR2(2000)
        备注   

    """
    __tablename__ = "CBondGuaranteeTotal"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_compcode = Column(VARCHAR2(10))
    enddate = Column(VARCHAR2(8))
    ann_date = Column(VARCHAR2(8))
    guar_balance = Column(NUMBER(20,0))
    guar_inwards = Column(NUMBER(20,0))
    guar_outwards = Column(NUMBER(20,0))
    memo = Column(VARCHAR2(2000))
    
