from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondFCTD(BaseModel):
    """
    4.187 中国国债期货最便宜可交割券

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        月合约Wind代码   
    trade_dt: VARCHAR2(8)
        日期   
    ctd_windcode: VARCHAR2(40)
        CTD证券Wind代码   
    ctd_irr: NUMBER(20,4)
        IRR   
    ib_ctd_windcode: VARCHAR2(40)
        银行间CTD证券Wind代码   
    ib_ctd_irr: NUMBER(20,4)
        银行间IRR   
    sh_ctd_windcode: VARCHAR2(40)
        沪市CTD证券Wind代码   
    sh_ctd_irr: NUMBER(20,4)
        沪市IRR   
    sz_ctd_windcode: VARCHAR2(40)
        深市CTD证券Wind代码   
    sz_ctd_irr: NUMBER(20,4)
        深市IRR   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondFCTD"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    ctd_windcode = Column(VARCHAR2(40))
    ctd_irr = Column(NUMBER(20,4))
    ib_ctd_windcode = Column(VARCHAR2(40))
    ib_ctd_irr = Column(NUMBER(20,4))
    sh_ctd_windcode = Column(VARCHAR2(40))
    sh_ctd_irr = Column(NUMBER(20,4))
    sz_ctd_windcode = Column(VARCHAR2(40))
    sz_ctd_irr = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
