from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CSIndusAnalysis(BaseModel):
    """
    中证行业估值

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    trade_dt: VARCHAR2(8)
        交易日期   
    industriescode: VARCHAR2(10)
        行业代码   证监会行业代码规则:04********中证行业代码规则:66********
    marketcode: NUMBER(9)
        市场代码   沪深两市:639001001深圳市场:639001002深市主板:639001003中小板:639001004创业板:639001005上证A股:639001006上证180A股:639001007上证380A股:639001008上证其它A股:639001009
    indust_val_pe: NUMBER(20,4)
        市盈率-加权平均   
    indust_val_pe_ttm: NUMBER(20,4)
        市盈率【TTM】-加权平均   
    indust_val_pb: NUMBER(20,4)
        市净率   
    sample_num: NUMBER(9)
        样本券个数   

    """
    object_id = Column(VARCHAR2(100))
    trade_dt = Column(VARCHAR2(8))
    industriescode = Column(VARCHAR2(10))
    marketcode = Column(NUMBER(9))
    indust_val_pe = Column(NUMBER(20,4))
    indust_val_pe_ttm = Column(NUMBER(20,4))
    indust_val_pb = Column(NUMBER(20,4))
    sample_num = Column(NUMBER(9))
    
