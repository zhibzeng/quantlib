from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareFreeFloatCalendar(BaseModel):
    """
    中国A股限售股流通日历

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_listdate: VARCHAR2(8)
        限售股上市日期   
    ann_dt: VARCHAR2(8)
        公告日期   
    s_share_lst: NUMBER(20,4)
        上市股份数量(万股)   
    s_share_nonlst: NUMBER(20,4)
        未上市股份数量(万股)   
    s_share_unrestricted: NUMBER(20,4)
        无限售条件股份数量(万股)   
    s_share_lsttypecode: NUMBER(9,0)
        上市股份类型代码   对应:类型编码表中的原始类型代码
    s_share_lst_is_ann: VARCHAR2(1)
        上市数量是否公布值   0：否，为预测值1:是,为实际公布值

    """
    __tablename__ = "AShareFreeFloatCalendar"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_listdate = Column(VARCHAR2(8))
    ann_dt = Column(VARCHAR2(8))
    s_share_lst = Column(NUMBER(20,4))
    s_share_nonlst = Column(NUMBER(20,4))
    s_share_unrestricted = Column(NUMBER(20,4))
    s_share_lsttypecode = Column(NUMBER(9,0))
    s_share_lst_is_ann = Column(VARCHAR2(1))
    
