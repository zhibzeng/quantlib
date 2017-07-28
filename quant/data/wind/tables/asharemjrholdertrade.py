from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareMjrHolderTrade(BaseModel):
    """
    4.36 中国A股重要股东增减持

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   数据来源：上市公司公告
    ann_dt: VARCHAR2(8)
        公告日期   
    transact_startdate: VARCHAR2(8)
        变动起始日期   
    transact_enddate: VARCHAR2(8)
        变动截至日期   
    holder_name: VARCHAR2(200)
        持有人   
    holder_type: VARCHAR2(1)
        持有人类型   1:个人；2:公司；3:高管
    transact_type: VARCHAR2(4)
        买卖方向   1:增持；2:减持
    transact_quantity: NUMBER(20,4)
        变动数量   
    transact_quantity_ratio: NUMBER(20,4)
        变动数量占流通量比例(%)   
    holder_quantity_new: NUMBER(20,4)
        最新持有流通数量   
    holder_quantity_new_ratio: NUMBER(20,4)
        最新持有流通数量占流通量比例(%)   
    avg_price: NUMBER(20,4)
        平均价格   
    whether_agreed_repur_trans: NUMBER(1)
        是否约定购回式交易   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareMjrHolderTrade"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    transact_startdate = Column(VARCHAR2(8))
    transact_enddate = Column(VARCHAR2(8))
    holder_name = Column(VARCHAR2(200))
    holder_type = Column(VARCHAR2(1))
    transact_type = Column(VARCHAR2(4))
    transact_quantity = Column(NUMBER(20,4))
    transact_quantity_ratio = Column(NUMBER(20,4))
    holder_quantity_new = Column(NUMBER(20,4))
    holder_quantity_new_ratio = Column(NUMBER(20,4))
    avg_price = Column(NUMBER(20,4))
    whether_agreed_repur_trans = Column(NUMBER(1))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
