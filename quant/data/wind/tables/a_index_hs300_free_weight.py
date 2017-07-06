"""A股指数每日收盘行情"""
from ....common.db.sql import BaseModel, Column, VARCHAR, Numeric, DateTime


class AIndexHS300FreeWeight(BaseModel):
    """A沪深300权重

    Attributes
    ----------
    object_id
        主键
    s_info_windcode
        指数万得代码
	s_con_windcode
		股票万得代码
    trade_dt
        日期 YYYYMMDD
	i_weight
		权重
		
    opdate

    opmode
    """
    __tablename__ = "AIndexHS300FreeWeight"
    object_id = Column(VARCHAR(100), primary_key=True)
    s_info_windcode = Column(VARCHAR(40))
    s_con_windcode = Column(VARCHAR(40))
    trade_dt = Column(VARCHAR(8))
    i_weight = Column(Numeric(20, 4))
    opdate = Column(DateTime)
    opmode = Column(VARCHAR(1))
