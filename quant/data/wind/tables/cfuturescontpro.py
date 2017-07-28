from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CFuturescontpro(BaseModel):
    """
    4.178 中国期货标准合约属性

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_code: VARCHAR2(20)
        标准合约代码   
    s_info_name: VARCHAR2(40)
        标准合约名称   
    s_info_tunit: VARCHAR2(40)
        交易计量单位   
    s_info_punit: NUMBER(20,4)
        交易单位(每手)   
    s_info_mfprice: VARCHAR2(200)
        最小报价单位说明   
    s_info_ftmargins: VARCHAR2(800)
        保证金要求说明   
    s_info_cdmonths: VARCHAR2(200)
        合约月份说明   
    s_info_thours: VARCHAR2(800)
        交易时间说明   
    s_info_ltdated: VARCHAR2(200)
        最后交易日说明   
    s_info_ddate: VARCHAR2(400)
        交割日期说明   
    s_info_cemultiplier: NUMBER(20,4)
        合约乘数   
    s_info_listdate: VARCHAR2(8)
        合约上市日期   
    s_info_delistdate: VARCHAR2(8)
        退市日期   
    s_info_exname: VARCHAR2(20)
        交易所简称   
    s_info_dmean: VARCHAR2(400)
        交割方式说明   
    s_info_dsite: VARCHAR2(400)
        交割地点说明   
    s_info_ltdatehour: VARCHAR2(400)
        最后交易日交易时间说明   
    s_info_cevalue: VARCHAR2(400)
        合约价值说明   
    s_info_maxpricefluct: VARCHAR2(800)
        最大价格波动说明   
    s_info_poslimit: VARCHAR2(800)
        头寸限制说明   
    s_info_udlsecode: VARCHAR2(20)
        标的证券代码   
    fs_info_punit: VARCHAR2(200)
        报价单位   
    s_info_rtd: NUMBER(20,4)
        均价计算使用值   
    s_sub_typcode: NUMBER(9,0)
        品种细类代码   703001001:贵金属703001002:有色703001003:煤焦钢矿703001004:非金属建材703001005:能源703001006:化工703001007:谷物703001008:油脂油料703001009:软商品703001010:农副产品
    contract_id: VARCHAR2(10)
        合约ID   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CFuturescontpro"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_code = Column(VARCHAR2(20))
    s_info_name = Column(VARCHAR2(40))
    s_info_tunit = Column(VARCHAR2(40))
    s_info_punit = Column(NUMBER(20,4))
    s_info_mfprice = Column(VARCHAR2(200))
    s_info_ftmargins = Column(VARCHAR2(800))
    s_info_cdmonths = Column(VARCHAR2(200))
    s_info_thours = Column(VARCHAR2(800))
    s_info_ltdated = Column(VARCHAR2(200))
    s_info_ddate = Column(VARCHAR2(400))
    s_info_cemultiplier = Column(NUMBER(20,4))
    s_info_listdate = Column(VARCHAR2(8))
    s_info_delistdate = Column(VARCHAR2(8))
    s_info_exname = Column(VARCHAR2(20))
    s_info_dmean = Column(VARCHAR2(400))
    s_info_dsite = Column(VARCHAR2(400))
    s_info_ltdatehour = Column(VARCHAR2(400))
    s_info_cevalue = Column(VARCHAR2(400))
    s_info_maxpricefluct = Column(VARCHAR2(800))
    s_info_poslimit = Column(VARCHAR2(800))
    s_info_udlsecode = Column(VARCHAR2(20))
    fs_info_punit = Column(VARCHAR2(200))
    s_info_rtd = Column(NUMBER(20,4))
    s_sub_typcode = Column(NUMBER(9,0))
    contract_id = Column(VARCHAR2(10))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
