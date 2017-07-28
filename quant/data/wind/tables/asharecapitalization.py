from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareCapitalization(BaseModel):
    """
    4.15 中国A股股本

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
        流通H股(万股)   大陆注册, 香港上市的外资股
    float_overseas_shr: NUMBER(20,4)
        境外流通股(万股)   在境外上市流通的股份, 如S股、N股等
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
    s_share_ntrd_statjur: NUMBER(20,4)
        国有法人股(万股)   
    s_share_ntrd_subdomesjur: NUMBER(20,4)
        境内法人股(万股)   境内发起人股+募集法人股+一般法人股+战略投资者持股+基金持股+STAQ股+NET股
    s_share_ntrd_domesinitor: NUMBER(20,4)
        境内发起人股(万股)   
    s_share_ntrd_ipojuris: NUMBER(20,4)
        募集法人股(万股)   
    s_share_ntrd_genjuris: NUMBER(20,4)
        一般法人股(万股)   
    s_share_ntrd_strtinvestor: NUMBER(20,4)
        战略投资者持股(万股)   
    s_share_ntrd_fundbal: NUMBER(20,4)
        基金持股(万股)   
    s_share_ntrd_ipoinip: NUMBER(20,4)
        自然人股(万股)   
    s_share_ntrd_trfnshare: NUMBER(20,4)
        转配股(万股)   
    s_share_ntrd_snormnger: NUMBER(20,4)
        高管股(万股)   流通股中属于该公司高管持有的部分
    s_share_ntrd_insderemp: NUMBER(20,4)
        内部职工股(万股)   历史遗留的内部职工持股
    s_share_ntrd_prfshare: NUMBER(20,4)
        优先股(万股)   
    s_share_ntrd_nonlstfrgn: NUMBER(20,4)
        非上市外资股(万股)   外资股东持有的非流通股
    s_share_ntrd_staq: NUMBER(20,4)
        STAQ股(万股)   
    s_share_ntrd_net: NUMBER(20,4)
        NET股(万股)   
    s_share_changereason: VARCHAR2(30)
        股本变动原因   见附录对应:类型编码表中的类型代码
    ann_dt: VARCHAR2(8)
        公告日期   
    change_dt1: VARCHAR2(8)
        变动日期1   除权日或上市日或登记日
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AShareCapitalization"
    object_id = Column(VARCHAR2(100), primary_key=True)
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
    s_share_ntrd_statjur = Column(NUMBER(20,4))
    s_share_ntrd_subdomesjur = Column(NUMBER(20,4))
    s_share_ntrd_domesinitor = Column(NUMBER(20,4))
    s_share_ntrd_ipojuris = Column(NUMBER(20,4))
    s_share_ntrd_genjuris = Column(NUMBER(20,4))
    s_share_ntrd_strtinvestor = Column(NUMBER(20,4))
    s_share_ntrd_fundbal = Column(NUMBER(20,4))
    s_share_ntrd_ipoinip = Column(NUMBER(20,4))
    s_share_ntrd_trfnshare = Column(NUMBER(20,4))
    s_share_ntrd_snormnger = Column(NUMBER(20,4))
    s_share_ntrd_insderemp = Column(NUMBER(20,4))
    s_share_ntrd_prfshare = Column(NUMBER(20,4))
    s_share_ntrd_nonlstfrgn = Column(NUMBER(20,4))
    s_share_ntrd_staq = Column(NUMBER(20,4))
    s_share_ntrd_net = Column(NUMBER(20,4))
    s_share_changereason = Column(VARCHAR2(30))
    ann_dt = Column(VARCHAR2(8))
    change_dt1 = Column(VARCHAR2(8))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
