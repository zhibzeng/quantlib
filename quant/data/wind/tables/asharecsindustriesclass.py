from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareCSIndustriesClass(BaseModel):
    """
    4.88 中国A股中证行业成分明细

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    cs_ind_code: VARCHAR2(50)
        中证行业代码   
    entry_dt: VARCHAR2(8)
        纳入日期   
    remove_dt: VARCHAR2(8)
        剔除日期   
    cur_sign: VARCHAR2(10)
        最新标志   1:是0:否
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareCSIndustriesClass"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    cs_ind_code = Column(VARCHAR2(50))
    entry_dt = Column(VARCHAR2(8))
    remove_dt = Column(VARCHAR2(8))
    cur_sign = Column(VARCHAR2(10))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
