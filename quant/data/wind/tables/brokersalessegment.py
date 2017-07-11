from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class BrokerSalesSegment(BaseModel):
    """
    券商主营业务构成

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
        项目类别   455001000:产品

    """
    object_id = Column(VARCHAR2(100))
    s_info_compcode = Column(VARCHAR2(40))
    s_info_compname = Column(VARCHAR2(200))
    report_period = Column(VARCHAR2(8))
    crncy_code = Column(VARCHAR2(10))
    s_segment_itemcode = Column(NUMBER(9,0))
    
