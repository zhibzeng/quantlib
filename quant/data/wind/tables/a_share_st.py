"""A股ST信息"""
from ....common.db.sql import BaseModel, Column, VARCHAR, Numeric, DateTime


class AShareST(BaseModel):
    """A股ST信息
    Columns:
        object_id: 主键
        s_info_windcode: 万得代码， eg. 600030.SH
        s_type_st: ST类型
        entry_dt: 进入ST日期 YYYYMMDD
        remove_dt: 退出ST日期 YYYYMMDD
        ann_dt: 公告日期 YYYYMMDD
    """
    __tablename__ = "AShareST".upper()
    object_id = Column(VARCHAR(100), primary_key=True)                          # Primary key
    s_info_windcode = Column(VARCHAR(40))                                       # wind code
    s_type_st = Column(VARCHAR(8))
    entry_dt = Column(VARCHAR(8))
    remove_dt = Column(VARCHAR(8))
    ann_dt = Column(VARCHAR(8))
    opdate = Column(DateTime())
    opmode = Column(VARCHAR(1))
