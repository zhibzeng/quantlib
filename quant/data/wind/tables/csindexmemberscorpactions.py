from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CSIndexMembersCorpActions(BaseModel):
    """
    中证指数成分公司行为

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        指数Wind代码   
    s_con_windcode: VARCHAR2(40)
        成份股Wind代码   
    trade_dt: VARCHAR2(8)
        生效日期英文：EffectiveDate   
    s_ca_type: VARCHAR2(100)
        事件英文：CAType   
    s_div_stock: NUMBER(20,6)
        送股比例英文：BonusIssuesRatio   
    s_rightsissue_pershare: NUMBER(20,6)
        配股比例英文：RightsOfferingRatio   
    s_rightsissue_price: NUMBER(20,4)
        配股价英文：RightsOfferingPrice   
    s_div_cash: NUMBER(20,6)
        分红额英文：Dividendpershare   
    s_share_index: NUMBER(20,2)
        计算用股本英文：Sharesinindex   

    """
    __tablename__ = "CSIndexMembersCorpActions"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_con_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    s_ca_type = Column(VARCHAR2(100))
    s_div_stock = Column(NUMBER(20,6))
    s_rightsissue_pershare = Column(NUMBER(20,6))
    s_rightsissue_price = Column(NUMBER(20,4))
    s_div_cash = Column(NUMBER(20,6))
    s_share_index = Column(NUMBER(20,2))
    
