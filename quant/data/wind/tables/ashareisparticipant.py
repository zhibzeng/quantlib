from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareISParticipant(BaseModel):
    """
    中国A股机构调研参与主体

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
        机构投资者类型   257001001证券公司资管

    """
    object_id = Column(VARCHAR2(100))
    event_id = Column(VARCHAR2(40))
    s_institutionname = Column(VARCHAR2(100))
    s_institutioncode = Column(VARCHAR2(10))
    s_institutiontype = Column(NUMBER(9,0))
    
