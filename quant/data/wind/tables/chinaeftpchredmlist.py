from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class ChinaEFTPchRedmList(BaseModel):
    """
    4.85 中国ETF申购赎回清单

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    f_info_cashdif: NUMBER(20,4)
        现金差额(元)   
    f_info_minpraset: NUMBER(20,4)
        最小申购赎回单位资产净值(元)   
    f_info_esticash: NUMBER(20,4)
        预估现金部分(元)   
    f_info_cashsubuplimit: NUMBER(20,4)
        现金替代比例上限(%)   
    f_info_minprunits: NUMBER(20,4)
        最小申购赎回单位(份)   
    f_info_prpermit: NUMBER(1,0)
        申购赎回允许情况   1：允许
    f_info_connum: NUMBER(20,4)
        标的指数成分股数量   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "ChinaEFTPchRedmList"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    f_info_cashdif = Column(NUMBER(20,4))
    f_info_minpraset = Column(NUMBER(20,4))
    f_info_esticash = Column(NUMBER(20,4))
    f_info_cashsubuplimit = Column(NUMBER(20,4))
    f_info_minprunits = Column(NUMBER(20,4))
    f_info_prpermit = Column(NUMBER(1,0))
    f_info_connum = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
