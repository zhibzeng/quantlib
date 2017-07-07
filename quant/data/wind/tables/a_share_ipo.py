"""A股IPO信息"""
from sqlalchemy import Column
from sqlalchemy.types import VARCHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base


BaseModel = declarative_base()


class AShareIPO(BaseModel):
    """
    A股IPO信息

    Attributes
    ----------
    object_id
        主键
    s_info_windcode
        万得代码， eg. 600030.SH
    s_ipo_listdate
        上市日期, YYYYMMDD
    """
    __tablename__ = "AShareIPO"
    object_id = Column(VARCHAR(100), primary_key=True)
    s_info_windcode = Column(VARCHAR(40))
    s_ipo_listdate = Column(VARCHAR(8))
    opdate = Column(DateTime)
    opmode = Column(VARCHAR(1))
