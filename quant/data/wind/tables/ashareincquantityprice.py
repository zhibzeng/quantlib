from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareIncQuantityPrice(BaseModel):
    """
    中国A股股权激励数量与价格

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_inc_sequence: VARCHAR2(6)
        序号   
    s_inc_transferpriper: NUMBER(20,4)
        每股转让价格(行权价格)   
    s_inc_quantity: NUMBER(20,4)
        激励数量(万份)   
    s_inc_getfundqty: NUMBER(20,4)
        提取激励基金数量(元)   
    s_inc_iscompleted: NUMBER(5,0)
        股权激励是否全部完成   1是0否
    s_inc_grantdate: VARCHAR2(8)
        期权授权日   
    s_inc_dnexec_quantity: NUMBER(20,4)
        已授权未行权的期权数量(万份)   
    s_inc_enddate: VARCHAR2(8)
        截止日期   
    ann_dt: VARCHAR2(8)
        公告日期   

    """
    __tablename__ = "AShareIncQuantityPrice"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_inc_sequence = Column(VARCHAR2(6))
    s_inc_transferpriper = Column(NUMBER(20,4))
    s_inc_quantity = Column(NUMBER(20,4))
    s_inc_getfundqty = Column(NUMBER(20,4))
    s_inc_iscompleted = Column(NUMBER(5,0))
    s_inc_grantdate = Column(VARCHAR2(8))
    s_inc_dnexec_quantity = Column(NUMBER(20,4))
    s_inc_enddate = Column(VARCHAR2(8))
    ann_dt = Column(VARCHAR2(8))
    
