from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareManagementHoldReward(BaseModel):
    """
    中国A股公司管理层持股及报酬

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_date: VARCHAR2(8)
        公告日期   
    end_date: VARCHAR2(8)
        截止日期   
    crny_code: VARCHAR2(10)
        货币代码   
    s_info_manager_name: VARCHAR2(80)
        姓名   
    s_info_manager_post: VARCHAR2(40)
        职务   
    s_manager_return: NUMBER(20,4)
        报酬   
    s_manager_quantity: NUMBER(20,4)
        持股数量   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    ann_date = Column(VARCHAR2(8))
    end_date = Column(VARCHAR2(8))
    crny_code = Column(VARCHAR2(10))
    s_info_manager_name = Column(VARCHAR2(80))
    s_info_manager_post = Column(VARCHAR2(40))
    s_manager_return = Column(NUMBER(20,4))
    s_manager_quantity = Column(NUMBER(20,4))
    
