from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareRalatedTrade(BaseModel):
    """
    中国A股关联交易

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    s_relatedtrade_name: VARCHAR2(80)
        B公司名称   
    s_relatedtrade_relationcode: VARCHAR2(300)
        关联关系   
    s_relatedtrade_control: NUMBER(5,0)
        是否存在控制关系   1：是；0：否
    s_relatedtrade_tradetype: VARCHAR2(300)
        交易类型   
    s_relatedtrade_settletype: VARCHAR2(300)
        结算方式   
    crncy_code: VARCHAR2(10)
        货币代码   CNY
    s_relatedtrade_amount: VARCHAR2(20)
        交易金额   

    """
    __tablename__ = "AShareRalatedTrade"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    s_relatedtrade_name = Column(VARCHAR2(80))
    s_relatedtrade_relationcode = Column(VARCHAR2(300))
    s_relatedtrade_control = Column(NUMBER(5,0))
    s_relatedtrade_tradetype = Column(VARCHAR2(300))
    s_relatedtrade_settletype = Column(VARCHAR2(300))
    crncy_code = Column(VARCHAR2(10))
    s_relatedtrade_amount = Column(VARCHAR2(20))
    
