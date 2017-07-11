from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareIndustriesCode(BaseModel):
    """
    行业代码

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    industriescode: VARCHAR2(38)
        行业代码   
    industriesname: VARCHAR2(50)
        行业名称   
    levelnum: NUMBER(1,0)
        级数   
    used: NUMBER(1,0)
        是否有效   
    industriesalias: VARCHAR2(12)
        板块别名   
    sequence: NUMBER(4,0)
        展示序号   

    """
    __tablename__ = "AShareIndustriesCode"
    object_id = Column(VARCHAR2(100), primary_key=True)
    industriescode = Column(VARCHAR2(38))
    industriesname = Column(VARCHAR2(50))
    levelnum = Column(NUMBER(1,0))
    used = Column(NUMBER(1,0))
    industriesalias = Column(VARCHAR2(12))
    sequence = Column(NUMBER(4,0))
    
