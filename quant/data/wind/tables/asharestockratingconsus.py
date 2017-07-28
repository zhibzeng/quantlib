from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareStockRatingConsus(BaseModel):
    """
    4.76 中国A股投资评级汇总

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    rating_dt: VARCHAR2(8)
        日期   
    s_wrating_avg: NUMBER(20,4)
        综合评级   
    s_wrating_instnum: NUMBER(20,4)
        评级机构数量   
    s_wrating_upgrade: NUMBER(20,4)
        调高家数(相比一月前)   
    s_wrating_downgrade: NUMBER(20,4)
        调低家数(相比一月前)   
    s_wrating_maintain: NUMBER(20,4)
        维持家数(相比一月前)   
    s_wrating_numofbuy: NUMBER(20,4)
        买入家数   
    s_wrating_numofoutperform: NUMBER(20,4)
        增持家数   
    s_wrating_numofhold: NUMBER(20,4)
        中性家数   
    s_wrating_numofunderperform: NUMBER(20,4)
        减持家数   
    s_wrating_numofsell: NUMBER(20,4)
        卖出家数   
    s_wrating_cycle: VARCHAR2(10)
        周期   综合值周期类型:263001000:30天263002000:90天263003000:180天
    s_est_price: NUMBER(20,4)
        一致预测目标价   
    s_est_priceinstnum: NUMBER(20,4)
        目标价预测机构数   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareStockRatingConsus"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    rating_dt = Column(VARCHAR2(8))
    s_wrating_avg = Column(NUMBER(20,4))
    s_wrating_instnum = Column(NUMBER(20,4))
    s_wrating_upgrade = Column(NUMBER(20,4))
    s_wrating_downgrade = Column(NUMBER(20,4))
    s_wrating_maintain = Column(NUMBER(20,4))
    s_wrating_numofbuy = Column(NUMBER(20,4))
    s_wrating_numofoutperform = Column(NUMBER(20,4))
    s_wrating_numofhold = Column(NUMBER(20,4))
    s_wrating_numofunderperform = Column(NUMBER(20,4))
    s_wrating_numofsell = Column(NUMBER(20,4))
    s_wrating_cycle = Column(VARCHAR2(10))
    s_est_price = Column(NUMBER(20,4))
    s_est_priceinstnum = Column(NUMBER(20,4))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
