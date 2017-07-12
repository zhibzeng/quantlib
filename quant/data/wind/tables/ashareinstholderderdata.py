from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareinstHolderDerData(BaseModel):
    """
    中国A股机构持股衍生数据

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    report_period: VARCHAR2(8)
        报告期   
    s_holder_compcode: VARCHAR2(40)
        股东公司id   
    s_holder_name: VARCHAR2(200)
        股东名称   
    s_holder_holdercategory: VARCHAR2(40)
        股东类型   
    s_holder_quantity: NUMBER(20,4)
        持股数   股
    s_holder_pct: NUMBER(20,4)
        持股比例(计算)   占流通股比例
    ann_date: VARCHAR2(8)
        公告日期   

    """
    __tablename__ = "AShareinstHolderDerData"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    report_period = Column(VARCHAR2(8))
    s_holder_compcode = Column(VARCHAR2(40))
    s_holder_name = Column(VARCHAR2(200))
    s_holder_holdercategory = Column(VARCHAR2(40))
    s_holder_quantity = Column(NUMBER(20,4))
    s_holder_pct = Column(NUMBER(20,4))
    ann_date = Column(VARCHAR2(8))
    
