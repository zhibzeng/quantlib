from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareSalesSegment(BaseModel):
    """
    中国A股主营业务构成

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
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

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    report_period = Column(VARCHAR2(8))
    crncy_code = Column(VARCHAR2(10))
    s_segment_itemcode = Column(NUMBER(9,0))
    s_segment_item = Column(VARCHAR2(100))
    s_segment_sales = Column(NUMBER(20,4))
    s_segment_profit = Column(NUMBER(20,4))
    s_segment_cost = Column(NUMBER(20,4))
    
