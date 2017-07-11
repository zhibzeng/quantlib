from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareBlockTrade(BaseModel):
    """
    中国A股大宗交易数据

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    s_block_price: NUMBER(20,4)
        成交价(元)   
    s_block_volume: NUMBER(20,4)
        成交量(万股)   
    s_block_amount: NUMBER(20,4)
        成交金额(万元)   
    crncy_code: VARCHAR2(10)
        货币代码   CNY
    s_block_buyername: VARCHAR2(200)
        买方营业部名称   
    s_block_sellername: VARCHAR2(200)
        卖方营业部名称   
    s_block_frequency: NUMBER(20,4)
        笔数   (同一代码+同一日期+同一机构+同一成交价+同一成交量)累计的笔数

    """
    __tablename__ = "AShareBlockTrade"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    s_block_price = Column(NUMBER(20,4))
    s_block_volume = Column(NUMBER(20,4))
    s_block_amount = Column(NUMBER(20,4))
    crncy_code = Column(VARCHAR2(10))
    s_block_buyername = Column(VARCHAR2(200))
    s_block_sellername = Column(VARCHAR2(200))
    s_block_frequency = Column(NUMBER(20,4))
    
