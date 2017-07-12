from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class ChinaETFWeekPchRedm(BaseModel):
    """
    中国ETF每周申购赎回

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        基金Wind代码   
    f_pchredm_begindate: VARCHAR2(8)
        起始日期   
    f_pchredm_enddate: VARCHAR2(8)
        截止日期   
    f_unit_pch: NUMBER(20,4)
        申购份额(亿份)   
    f_unit_redm: NUMBER(20,4)
        赎回份额(亿份)   

    """
    __tablename__ = "ChinaETFWeekPchRedm"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    f_pchredm_begindate = Column(VARCHAR2(8))
    f_pchredm_enddate = Column(VARCHAR2(8))
    f_unit_pch = Column(NUMBER(20,4))
    f_unit_redm = Column(NUMBER(20,4))
    
