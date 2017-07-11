from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CBondConvprice(BaseModel):
    """
    中国债券转股价格变动

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_enddate: VARCHAR2(8)
        截止日期   
    b_info_announcementdate: VARCHAR2(8)
        公告日期   
    cb_anal_convprice: NUMBER(20,4)
        转股价格   
    b_info_changereason: VARCHAR2(1000)
        变动原因   1发行2换股吸收合并3派息4配股5上市6送股7送转股8送转股,派息9修正10增发11转增,派息

    """
    __tablename__ = "CBondConvprice"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_enddate = Column(VARCHAR2(8))
    b_info_announcementdate = Column(VARCHAR2(8))
    cb_anal_convprice = Column(NUMBER(20,4))
    b_info_changereason = Column(VARCHAR2(1000))
    
