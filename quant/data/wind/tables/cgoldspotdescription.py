from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CGoldSpotDescription(BaseModel):
    """
    中国黄金现货基本资料

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_code: VARCHAR2(40)
        交易代码   
    s_info_name: VARCHAR2(50)
        证券中文简称   
    s_info_exchmarket: VARCHAR2(10)
        交易所   SGE：上海黄金交易所
    s_info_punit: VARCHAR2(40)
        交易单位   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_info_code = Column(VARCHAR2(40))
    s_info_name = Column(VARCHAR2(50))
    s_info_exchmarket = Column(VARCHAR2(10))
    s_info_punit = Column(VARCHAR2(40))
    
