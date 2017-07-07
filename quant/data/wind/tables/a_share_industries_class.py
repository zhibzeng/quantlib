"""中国A 股Wind 行业分类"""
from sqlalchemy import Column
from sqlalchemy.types import VARCHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base


BaseModel = declarative_base()


class AShareIndustriesClass(BaseModel):
    """
    中国A 股Wind 行业分类

    Attributes
    ----------
    object_id
        主键
    s_info_windcode
        万得代码， eg. 600030.SH
    windcode
        万得代码， eg. 600030.SH
    wind_ind_code
        Wind行业代码
    entry_dt
        纳入日期
    remove_dt
        剔除日期
    cur_sign
        最新标志 1：是 0：否
    """
    __tablename__ = "AShareIndustriesClass"
    object_id = Column(VARCHAR(100), primary_key=True)
    s_info_windcode = Column(VARCHAR(40))
    windcode = Column(VARCHAR(40))
    wind_ind_code = Column(VARCHAR(50))
    entry_dt = Column(VARCHAR(8))
    remove_dt = Column(VARCHAR(8))
    cur_sign = Column(VARCHAR(10))
    opdate = Column(DateTime)
    opmode = Column(VARCHAR(1))
