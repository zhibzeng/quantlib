from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareCompRestricted(BaseModel):
    """
    中国A股限售股解禁公司明细

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_listdate: VARCHAR2(8)
        可流通日期   
    s_holder_name: VARCHAR2(200)
        股东名称   
    s_share_lsttypecode: NUMBER(9,0)
        股份类型代码   请参考：类型编码表
    s_share_lsttypename: VARCHAR2(200)
        股份类型   
    s_share_lst: NUMBER(20,4)
        可流通数量(股)   
    s_share_ratio: NUMBER(20,4)
        可流通数量占总股本比例(%)   
    s_share_placement_enddt: VARCHAR2(8)
        配售截止日期   

    """
    __tablename__ = "AShareCompRestricted"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_listdate = Column(VARCHAR2(8))
    s_holder_name = Column(VARCHAR2(200))
    s_share_lsttypecode = Column(NUMBER(9,0))
    s_share_lsttypename = Column(VARCHAR2(200))
    s_share_lst = Column(NUMBER(20,4))
    s_share_ratio = Column(NUMBER(20,4))
    s_share_placement_enddt = Column(VARCHAR2(8))
    
