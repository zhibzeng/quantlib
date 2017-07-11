from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareCompanyfilings(BaseModel):
    """
    中国A股公司公告

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    s_est_flstitle_inst: VARCHAR2(100)
        标题   
    s_est_flsabstract_inst: CLOB
        摘要   

    """
    __tablename__ = "AShareCompanyfilings"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    s_est_flstitle_inst = Column(VARCHAR2(100))
    s_est_flsabstract_inst = Column(CLOB)
    
