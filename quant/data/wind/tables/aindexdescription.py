from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AIndexDescription(BaseModel):
    """
    中国A股指数基本资料

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_code: VARCHAR2(40)
        交易代码   
    s_info_name: VARCHAR2(50)
        证券简称   
    s_info_compname: VARCHAR2(100)
        指数名称   
    s_info_exchmarket: VARCHAR2(40)
        交易所   SSE:上交所SZSE:深交所WIND:万得Others:其他
    s_info_index_baseper: VARCHAR2(8)
        基期   
    s_info_index_basept: NUMBER(20,4)
        基点   
    s_info_listdate: VARCHAR2(8)
        发布日期   
    s_info_index_weightsrule: VARCHAR2(10)
        加权方式   1：自由流通股本2：总股本3：分级靠档14：分级靠档25：新华富时6：MSCI7：沪深300反算权数8：分级靠档3

    """
    __tablename__ = "AIndexDescription"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_code = Column(VARCHAR2(40))
    s_info_name = Column(VARCHAR2(50))
    s_info_compname = Column(VARCHAR2(100))
    s_info_exchmarket = Column(VARCHAR2(40))
    s_info_index_baseper = Column(VARCHAR2(8))
    s_info_index_basept = Column(NUMBER(20,4))
    s_info_listdate = Column(VARCHAR2(8))
    s_info_index_weightsrule = Column(VARCHAR2(10))
    
