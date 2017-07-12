from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondBillRate(BaseModel):
    """
    票据利率

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    b_info_ratetype: VARCHAR2(100)
        利率类型   票据转贴利率(月息):6个月票据直贴利率(月息):6个月:中西部票据直贴利率(月息):6个月:环渤海票据直贴利率(月息):6个月:珠三角票据直贴利率(月息):6个月:长三角
    trade_dt: VARCHAR2(8)
        交易日期   
    b_info_rate: NUMBER(20,6)
        利率(%)   

    """
    __tablename__ = "CBondBillRate"
    object_id = Column(VARCHAR2(100), primary_key=True)
    b_info_ratetype = Column(VARCHAR2(100))
    trade_dt = Column(VARCHAR2(8))
    b_info_rate = Column(NUMBER(20,6))
    
