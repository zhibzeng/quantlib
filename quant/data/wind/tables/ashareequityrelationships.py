from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareEquityRelationships(BaseModel):
    """
    中国A股股权关系

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    enddate: VARCHAR2(8)
        截止日期   
    s_info_compname: VARCHAR2(200)
        公司名称   
    s_info_compcode: VARCHAR2(10)
        公司ID   
    relation_type: VARCHAR2(40)
        公司与披露方关系   公司本身公司股东公司控股参股公司公司其它关联方
    s_holder_name: VARCHAR2(200)
        股东名称   
    s_holder_code: VARCHAR2(10)
        股东ID   
    s_holder_type: NUMBER(5,0)
        股东类型   1:个人2:公司
    s_holder_pct: NUMBER(20,4)
        持股比例(%)   
    is_actualcontroller: NUMBER(5,0)
        股东是否为实际控制人   0:否1:是
    actualcontroller_type: VARCHAR2(80)
        实际控制人类型   大学地方国有企业地方国资委地方政府个人国资委集体企业

    """
    __tablename__ = "AShareEquityRelationships"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    enddate = Column(VARCHAR2(8))
    s_info_compname = Column(VARCHAR2(200))
    s_info_compcode = Column(VARCHAR2(10))
    relation_type = Column(VARCHAR2(40))
    s_holder_name = Column(VARCHAR2(200))
    s_holder_code = Column(VARCHAR2(10))
    s_holder_type = Column(NUMBER(5,0))
    s_holder_pct = Column(NUMBER(20,4))
    is_actualcontroller = Column(NUMBER(5,0))
    actualcontroller_type = Column(VARCHAR2(80))
    
