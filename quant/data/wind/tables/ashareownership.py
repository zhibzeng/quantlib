from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareOwnership(BaseModel):
    """
    4.9 中国A股企业所有制板块

    Attributes
    ----------
    object_id: VARCHAR2(38)
        对象ID   
    s_info_compcode: VARCHAR2(40)
        公司id   
    s_info_compname: VARCHAR2(200)
        公司名称   
    wind_sec_code: VARCHAR2(10)
        板块代码   一级：国有企业:0805010000(二级：中央国有企业:0805010100)(二级：地方国有企业:0805010200)民营企业:0805020000外资企业:0805030000(二级：中外合资企业:0805030100)(二级：外商独资企业:0805030200)集体企业:0805040000公众企业:0805050000其他企业:0805060000
    entry_dt: VARCHAR2(8)
        纳入日期   
    remove_dt: VARCHAR2(8)
        剔除日期   
    cur_sign: NUMBER(1,0)
        最新标志   1:是；0：否
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareOwnership"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_compcode = Column(VARCHAR2(40))
    s_info_compname = Column(VARCHAR2(200))
    wind_sec_code = Column(VARCHAR2(10))
    entry_dt = Column(VARCHAR2(8))
    remove_dt = Column(VARCHAR2(8))
    cur_sign = Column(NUMBER(1,0))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
