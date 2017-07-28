from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareLeadUnderwriter(BaseModel):
    """
    4.12 中国A股发行主承销商

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_lu_annissuedate: VARCHAR2(8)
        发行公告日   
    s_lu_issuedate: VARCHAR2(8)
        发行日期   
    s_lu_issuetype: VARCHAR2(1)
        发行类型   1.首发2.增发3.配股
    s_lu_totalissuecollection: NUMBER(20,4)
        募集资金合计(万元)   
    s_lu_totalissueexpenses: NUMBER(20,4)
        发行费用合计(万元)   
    s_lu_totaluderandsponefee: NUMBER(20,4)
        承销与保荐费用(万元)   
    s_lu_number: VARCHAR2(1)
        参与主承销商个数   
    s_lu_name: VARCHAR2(100)
        参与主承销商名称   
    s_lu_institype: VARCHAR2(40)
        主承销商类型   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareLeadUnderwriter"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_lu_annissuedate = Column(VARCHAR2(8))
    s_lu_issuedate = Column(VARCHAR2(8))
    s_lu_issuetype = Column(VARCHAR2(1))
    s_lu_totalissuecollection = Column(NUMBER(20,4))
    s_lu_totalissueexpenses = Column(NUMBER(20,4))
    s_lu_totaluderandsponefee = Column(NUMBER(20,4))
    s_lu_number = Column(VARCHAR2(1))
    s_lu_name = Column(VARCHAR2(100))
    s_lu_institype = Column(VARCHAR2(40))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
