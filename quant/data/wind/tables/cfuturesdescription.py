from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CFuturesDescription(BaseModel):
    """
    中国期货基本资料

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_code: VARCHAR2(40)
        交易代码   
    s_info_name: VARCHAR2(50)
        证券中文简称   
    s_info_ename: VARCHAR2(50)
        证券英文简称   
    fs_info_sccode: VARCHAR2(50)
        标准合约代码   
    fs_info_type: Number(1,0)
        合约类型   1:月合约2:连续合约
    fs_info_cctype: Number(9,0)
        连续合约类型   706001000:连续(当月)706002000:连一(次月)706003000:连二(当季)706004000:连三(下季)706005000:连四706006000:活跃
    s_info_exchmarket: VARCHAR2(10)
        交易所   CZCE:郑州商品交易所CFFEX:中国金融期货交易所DCE:大连商品交易所SHFE:上海期货交易所
    s_info_listdate: VARCHAR2(8)
        上市日期   
    s_info_delistdate: VARCHAR2(8)
        最后交易日期   
    fs_info_dlmonth: VARCHAR2(8)
        交割月份   
    fs_info_lprice: Number(20,4)
        挂牌基准价   
    fs_info_ltdldate: VARCHAR2(8)
        最后交割日   

    """
    __tablename__ = "CFuturesDescription"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_code = Column(VARCHAR2(40))
    s_info_name = Column(VARCHAR2(50))
    s_info_ename = Column(VARCHAR2(50))
    fs_info_sccode = Column(VARCHAR2(50))
    fs_info_type = Column(Number(1,0))
    fs_info_cctype = Column(Number(9,0))
    s_info_exchmarket = Column(VARCHAR2(10))
    s_info_listdate = Column(VARCHAR2(8))
    s_info_delistdate = Column(VARCHAR2(8))
    fs_info_dlmonth = Column(VARCHAR2(8))
    fs_info_lprice = Column(Number(20,4))
    fs_info_ltdldate = Column(VARCHAR2(8))
    
