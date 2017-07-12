from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class ChinaOptionDescription(BaseModel):
    """
    中国期权基本资料

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_code: VARCHAR2(40)
        交易代码   
    s_info_name: VARCHAR2(100)
        月合约名称   
    s_info_sccode: VARCHAR2(50)
        标准合约代码   
    s_info_callput: NUMBER(9,0)
        期权类别   708001000:认购708002000:认沽
    s_info_strikeprice: NUMBER(20,4)
        行权价格   
    s_info_month: VARCHAR2(6)
        结算月份   
    s_info_maturitydate: VARCHAR2(8)
        到期日   
    s_info_ftdate: VARCHAR2(8)
        开始交易日   
    s_info_lasttradingdate: VARCHAR2(8)
        最后交易日   
    s_info_exercisingend: VARCHAR2(8)
        最后行权日   
    s_info_lddate: VARCHAR2(8)
        最后交割日   
    s_info_lprice: NUMBER(20,4)
        挂牌基准价   
    s_info_trade: VARCHAR2(1)
        是否交易   0:否1:是

    """
    __tablename__ = "ChinaOptionDescription"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_code = Column(VARCHAR2(40))
    s_info_name = Column(VARCHAR2(100))
    s_info_sccode = Column(VARCHAR2(50))
    s_info_callput = Column(NUMBER(9,0))
    s_info_strikeprice = Column(NUMBER(20,4))
    s_info_month = Column(VARCHAR2(6))
    s_info_maturitydate = Column(VARCHAR2(8))
    s_info_ftdate = Column(VARCHAR2(8))
    s_info_lasttradingdate = Column(VARCHAR2(8))
    s_info_exercisingend = Column(VARCHAR2(8))
    s_info_lddate = Column(VARCHAR2(8))
    s_info_lprice = Column(NUMBER(20,4))
    s_info_trade = Column(VARCHAR2(1))
    
