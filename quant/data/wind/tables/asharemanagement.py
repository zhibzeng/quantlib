from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareManagement(BaseModel):
    """
    4.13 中国A股公司管理层成员

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_date: VARCHAR2(8)
        公告日期   
    s_info_manager_name: VARCHAR2(80)
        姓名   
    s_info_manager_gender: VARCHAR2(10)
        性别   m:男f:女
    s_info_manager_education: VARCHAR2(10)
        学历   
    s_info_manager_nationality: VARCHAR2(40)
        国籍   
    s_info_manager_birthyear: VARCHAR2(8)
        出生年份   
    s_info_manager_startdate: VARCHAR2(8)
        任职日期   
    s_info_manager_leavedate: VARCHAR2(8)
        离职日期   
    s_info_manager_type: NUMBER(5,0)
        管理层类别   0：董事会成员1：高管成员2：监事会成员
    s_info_manager_post: VARCHAR2(40)
        职务   
    s_info_manager_introduction: VARCHAR2(2000)
        个人简历   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareManagement"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_date = Column(VARCHAR2(8))
    s_info_manager_name = Column(VARCHAR2(80))
    s_info_manager_gender = Column(VARCHAR2(10))
    s_info_manager_education = Column(VARCHAR2(10))
    s_info_manager_nationality = Column(VARCHAR2(40))
    s_info_manager_birthyear = Column(VARCHAR2(8))
    s_info_manager_startdate = Column(VARCHAR2(8))
    s_info_manager_leavedate = Column(VARCHAR2(8))
    s_info_manager_type = Column(NUMBER(5,0))
    s_info_manager_post = Column(VARCHAR2(40))
    s_info_manager_introduction = Column(VARCHAR2(2000))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
