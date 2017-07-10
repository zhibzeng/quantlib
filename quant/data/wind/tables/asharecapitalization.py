from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareCapitalization(BaseModel):
    """
    中国A股股本

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    wind_code: VARCHAR2(40)
        Wind代码   
    change_dt: VARCHAR2(8)
        变动日期   上市日期
    tot_shr: NUMBER(20,4)
        总股本   
    float_shr: NUMBER(20,4)
        流通股(万股)   流通A股+流通B股+流通H股+境外流通股
    float_a_shr: NUMBER(20,4)
        流通A股(万股)   人民币普通股
    float_b_shr: NUMBER(20,4)
        流通B股(万股)   以外币计价交易的人民币特种股
    float_h_shr: NUMBER(20,4)
        流通H股(万股)   大陆注册，香港上市的外资股
    float_overseas_shr: NUMBER(20,4)
        境外流通股(万股)   在境外上市流通的股份，如S股、N股等
    restricted_a_shr: NUMBER(20,4)
        限售A股(万股)   限售股份(国家持股)+限售股份(国有法人持股)+限售股份(其他内资持股)+限售股份(外资持股)
    s_share_rtd_state: NUMBER(20,4)
        限售股份(国家持股)(万股)   
    s_share_rtd_statejur: NUMBER(20,4)
        限售股份(国有法人持股)(万股)   
    s_share_rtd_subotherdomes: NUMBER(20,4)
        限售股份(其他内资持股)(万股)   限售股份(境内法人持股)+限售股份(机构配售股份)+限售股份(境内自然人持股)
    s_share_rtd_domesjur: NUMBER(20,4)
        限售股份(境内法人持股)(万股)   
    s_share_rtd_inst: NUMBER(20,4)
        限售股份(机构配售股份)(万股)   
    s_share_rtd_domesnp: NUMBER(20,4)
        限售股份(境内自然人持股)(万股)   包含:限售股份(高管持股)
    s_share_rtd_senmanager: NUMBER(20,4)
        限售股份(高管持股)(万股)   
    s_share_rtd_subfrgn: NUMBER(20,4)
        限售股份(外资持股)(万股)   限售股份(境外法人持股)+限售股份(境外自然人持股)
    s_share_rtd_frgnjur: NUMBER(20,4)
        限售股份(境外法人持股)(万股)   
    s_share_rtd_frgnnp: NUMBER(20,4)
        限售股份(境外自然人持股)(万股)   
    restricted_b_shr: NUMBER(20,4)
        限售B股   
    other_restricted_shr: NUMBER(20,4)
        其他限售股   目前一般为H股限售股
    non_tradable_shr: NUMBER(20,4)
        非流通股   总股本-(A股流通股+B股流通股+H股流通股+境外流通股)
    s_share_ntrd_state_pct: NUMBER(20,4)
        国有股(万股)   国家股+国有法人股
    s_share_ntrd_state: NUMBER(20,4)
        国家股(万股)   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    wind_code = Column(VARCHAR2(40))
    change_dt = Column(VARCHAR2(8))
    tot_shr = Column(NUMBER(20,4))
    float_shr = Column(NUMBER(20,4))
    float_a_shr = Column(NUMBER(20,4))
    float_b_shr = Column(NUMBER(20,4))
    float_h_shr = Column(NUMBER(20,4))
    float_overseas_shr = Column(NUMBER(20,4))
    restricted_a_shr = Column(NUMBER(20,4))
    s_share_rtd_state = Column(NUMBER(20,4))
    s_share_rtd_statejur = Column(NUMBER(20,4))
    s_share_rtd_subotherdomes = Column(NUMBER(20,4))
    s_share_rtd_domesjur = Column(NUMBER(20,4))
    s_share_rtd_inst = Column(NUMBER(20,4))
    s_share_rtd_domesnp = Column(NUMBER(20,4))
    s_share_rtd_senmanager = Column(NUMBER(20,4))
    s_share_rtd_subfrgn = Column(NUMBER(20,4))
    s_share_rtd_frgnjur = Column(NUMBER(20,4))
    s_share_rtd_frgnnp = Column(NUMBER(20,4))
    restricted_b_shr = Column(NUMBER(20,4))
    other_restricted_shr = Column(NUMBER(20,4))
    non_tradable_shr = Column(NUMBER(20,4))
    s_share_ntrd_state_pct = Column(NUMBER(20,4))
    s_share_ntrd_state = Column(NUMBER(20,4))
    
