from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CfuturesContractMapping(BaseModel):
    """
    中国期货连续(主力)合约和月合约映射表

    Attributes
    ----------
    object_id: VARCHAR2(38)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        连续(主力)合约Wind代码   
    fs_mapping_windcode: VARCHAR2(40)
        映射月合约Wind代码   
    startdate: VARCHAR2(8)
        起始日期   
    enddate: VARCHAR2(8)
        截止日期   
    contract_id: VARCHAR2(10)
        合约ID   

    """
    object_id = Column(VARCHAR2(38))
    s_info_windcode = Column(VARCHAR2(40))
    fs_mapping_windcode = Column(VARCHAR2(40))
    startdate = Column(VARCHAR2(8))
    enddate = Column(VARCHAR2(8))
    contract_id = Column(VARCHAR2(10))
    
