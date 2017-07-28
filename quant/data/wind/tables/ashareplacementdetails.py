from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class ASharePlacementDetails(BaseModel):
    """
    4.23 中国A股网下配售机构获配明细

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_holder_name: VARCHAR2(200)
        股东名称   
    s_holder_typecode: NUMBER(9,0)
        股东类型代码   请参考：类型编码表
    s_holder_type: VARCHAR2(20)
        股东类型   
    typeofinvestor: VARCHAR2(20)
        法人投资者类型   
    ordqty: NUMBER(20,4)
        有效报价的申购数量(股)   
    placement: NUMBER(20,4)
        获配数量(股)   
    trade_dt: VARCHAR2(8)
        截止日期   
    ann_dt: VARCHAR2(8)
        公告日期   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "ASharePlacementDetails"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_holder_name = Column(VARCHAR2(200))
    s_holder_typecode = Column(NUMBER(9,0))
    s_holder_type = Column(VARCHAR2(20))
    typeofinvestor = Column(VARCHAR2(20))
    ordqty = Column(NUMBER(20,4))
    placement = Column(NUMBER(20,4))
    trade_dt = Column(VARCHAR2(8))
    ann_dt = Column(VARCHAR2(8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
