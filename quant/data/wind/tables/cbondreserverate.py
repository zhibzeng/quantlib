from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class CBondReserveRate(BaseModel):
    """
    法定存款准备金率

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    trade_dt: VARCHAR2(8)
        交易日期   
    s_info_reserveratetype: VARCHAR2(80)
        准备金率品种   1超额存款准备金利率2存款准备金率3存款准备金率(大型机构)4法定存款准备金利率5对金融机构贷款利率(1年)6对金融机构贷款利率(20天以内)7对金融机构贷款利率(3个月以内)8对金融机构贷款利率(6个月以内)9外汇存款准备金率10再贴现利率
    b_info_rate: NUMBER(20,4)
        准备金率(%)   

    """
    object_id = Column(VARCHAR2(100))
    trade_dt = Column(VARCHAR2(8))
    s_info_reserveratetype = Column(VARCHAR2(80))
    b_info_rate = Column(NUMBER(20,4))
    
