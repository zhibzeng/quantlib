from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareGICSIndustriesClass(BaseModel):
    """
    中信标普GICS行业分类

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    gics_ind_code: VARCHAR2(50)
        GICS行业代码   
    entry_dt: VARCHAR2(8)
        纳入日期   
    remove_dt: VARCHAR2(8)
        剔除日期   
    cur_sign: VARCHAR2(10)
        最新标志   1:是0:否

    """
    __tablename__ = "AShareGICSIndustriesClass"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    gics_ind_code = Column(VARCHAR2(50))
    entry_dt = Column(VARCHAR2(8))
    remove_dt = Column(VARCHAR2(8))
    cur_sign = Column(VARCHAR2(10))
    