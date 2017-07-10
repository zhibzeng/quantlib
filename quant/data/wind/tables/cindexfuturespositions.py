from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CIndexFuturesPositions(BaseModel):
    """
    中国股指期货成交及持仓

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    fs_info_membername: VARCHAR2(40)
        会员简称   
    fs_info_type: VARCHAR2(1)
        类型   1：成交量2：持买单量3：持卖单量
    fs_info_positionsnum: NUMBER(20,4)
        持仓数量   
    fs_info_rank: NUMBER(5,0)
        名次   
    s_oi_positionsnumc: NUMBER(20,4)
        比上交易日增减   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    fs_info_membername = Column(VARCHAR2(40))
    fs_info_type = Column(VARCHAR2(1))
    fs_info_positionsnum = Column(NUMBER(20,4))
    fs_info_rank = Column(NUMBER(5,0))
    s_oi_positionsnumc = Column(NUMBER(20,4))
    
