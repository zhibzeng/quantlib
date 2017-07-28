from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareISParticipant(BaseModel):
    """
    4.115 中国A股机构调研参与主体

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    event_id: VARCHAR2(40)
        事件ID   
    s_institutionname: VARCHAR2(100)
        机构投资者名称   
    s_institutioncode: VARCHAR2(10)
        机构投资者ID   
    s_institutiontype: NUMBER(9,0)
        机构投资者类型   257001001证券公司资管257001002证券公司自营257001003基金公司257001004保险公司257001005投资公司257001006外资机构257001007其他257002001证券公司
    s_analystname: VARCHAR2(20)
        机构参与人员姓名   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareISParticipant"
    object_id = Column(VARCHAR2(100), primary_key=True)
    event_id = Column(VARCHAR2(40))
    s_institutionname = Column(VARCHAR2(100))
    s_institutioncode = Column(VARCHAR2(10))
    s_institutiontype = Column(NUMBER(9,0))
    s_analystname = Column(VARCHAR2(20))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
