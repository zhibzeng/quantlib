from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class MergerParticipant(BaseModel):
    """
    并购事件参与方

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    event_id: VARCHAR2(20)
        情报ID(或事件ID)   
    party_name: VARCHAR2(200)
        参与方名称   
    country_code: VARCHAR2(10)
        所属国家或地区代码   
    party_id: VARCHAR2(10)
        参与方ID   
    s_info_windcode: VARCHAR2(40)
        参与方关联证券Wind代码   
    party_type_code: NUMBER(9，0)
        参与方类型代码   注1
    relationship: NUMBER(9，0)
        参与方与关联证券代码关系   
    party_role_code: NUMBER(9，0)
        参与方角色代码   注2
    pre_proportion: NUMBER(20，4)
        转让前持股比例   
    after_proportion: NUMBER(20，4)
        转让后持股比例   
    agent_id: VARCHAR2(20)
        主要经办人ID   
    stockright_proportion: NUMBER(20，4)
        标的方交易股权占比   
    evalue_value: NUMBER(20，4)
        标的方评估价值   
    appreciation_rate: NUMBER(20，4)
        标的方增值率   

    """
    object_id = Column(VARCHAR2(100))
    event_id = Column(VARCHAR2(20))
    party_name = Column(VARCHAR2(200))
    country_code = Column(VARCHAR2(10))
    party_id = Column(VARCHAR2(10))
    s_info_windcode = Column(VARCHAR2(40))
    party_type_code = Column(NUMBER(9，0))
    relationship = Column(NUMBER(9，0))
    party_role_code = Column(NUMBER(9，0))
    pre_proportion = Column(NUMBER(20，4))
    after_proportion = Column(NUMBER(20，4))
    agent_id = Column(VARCHAR2(20))
    stockright_proportion = Column(NUMBER(20，4))
    evalue_value = Column(NUMBER(20，4))
    appreciation_rate = Column(NUMBER(20，4))
    
