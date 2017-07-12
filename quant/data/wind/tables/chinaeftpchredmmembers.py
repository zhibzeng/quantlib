from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class ChinaEFTPchRedmMembers(BaseModel):
    """
    中国ETF申购赎回成份

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        基金Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    s_con_windcode: VARCHAR2(40)
        成份股Wind代码   
    s_con_stocknumber: NUMBER(20,4)
        股票数量   
    f_info_cashsubsign: NUMBER(1,0)
        现金替代标志   0：禁止现金替代1：允许现金替代2：必须现金替代
    f_info_casubpremra: NUMBER(20,4)
        现金替代溢价比例(%)   
    f_info_casubamount: NUMBER(20,4)
        固定替代金额(元)   

    """
    __tablename__ = "ChinaEFTPchRedmMembers"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    s_con_windcode = Column(VARCHAR2(40))
    s_con_stocknumber = Column(NUMBER(20,4))
    f_info_cashsubsign = Column(NUMBER(1,0))
    f_info_casubpremra = Column(NUMBER(20,4))
    f_info_casubamount = Column(NUMBER(20,4))
    
