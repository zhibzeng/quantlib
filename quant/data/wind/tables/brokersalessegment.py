from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class BrokerSalesSegment(BaseModel):
    """
    4.71 券商主营业务构成

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_compcode: VARCHAR2(40)
        公司ID   
    s_info_compname: VARCHAR2(200)
        公司名称   
    report_period: VARCHAR2(8)
        报告期   
    crncy_code: VARCHAR2(10)
        货币代码   
    s_segment_itemcode: NUMBER(9,0)
        项目类别   455001000:产品455002000:地区455003000:其他455004000:行业455005000:缴费方式
    s_segment_item: VARCHAR2(100)
        主营业务项目   
    s_segment_sales: NUMBER(20,4)
        主营业务收入(元)   
    s_segment_profit: NUMBER(20,4)
        主营业务利润(元)   
    s_segment_cost: NUMBER(20,4)
        主营业务成本(元)   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "BrokerSalesSegment"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_compcode = Column(VARCHAR2(40))
    s_info_compname = Column(VARCHAR2(200))
    report_period = Column(VARCHAR2(8))
    crncy_code = Column(VARCHAR2(10))
    s_segment_itemcode = Column(NUMBER(9,0))
    s_segment_item = Column(VARCHAR2(100))
    s_segment_sales = Column(NUMBER(20,4))
    s_segment_profit = Column(NUMBER(20,4))
    s_segment_cost = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
