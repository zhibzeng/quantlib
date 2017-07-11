from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class ChinaOptionContpro(BaseModel):
    """
    中国期权标准合约属性

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_code: VARCHAR2(20)
        标准合约代码   
    s_info_name: VARCHAR2(40)
        标准合约中文名称   
    s_info_ename: VARCHAR2(100)
        标准合约英文名称   
    s_info_exname: VARCHAR2(20)
        交易所名称   
    s_info_type: VARCHAR2(20)
        合约类型   
    s_info_euroamericanbermuda: VARCHAR2(10)
        期权行权方式   
    s_info_settlementmethod: VARCHAR2(10)
        结算方式   
    s_info_listeddate: VARCHAR2(8)
        合约上市日期   
    s_info_delistdate: VARCHAR2(8)
        合约退市日期   
    s_info_strikeratio: NUMBER(20,4)
        合约乘数   
    s_info_cevalue: NUMBER(20,4)
        合约价值   
    s_info_covalue: VARCHAR2(80)
        立约价值   
    s_info_lsmonth: VARCHAR2(200)
        合约结算月份   
    s_info_minpricefluct: VARCHAR2(40)
        最小价格波幅   
    s_info_thours: VARCHAR2(200)
        交易时间   
    s_info_lasttradingdate: VARCHAR2(200)
        最后交易日   
    s_info_lsdate: VARCHAR2(200)
        最后结算日   
    s_info_lastsettle: VARCHAR2(200)
        最后结算价   
    s_info_tradefee: VARCHAR2(200)
        交易费用   
    s_info_poslimit: VARCHAR2(800)
        头寸限制   
    s_info_minposlimit: VARCHAR2(800)
        头寸申报下限   
    s_info_optionprice: VARCHAR2(20)
        期权金   
    s_info_exercisingend: VARCHAR2(40)
        期权行权日   
    s_info_strikeprice: VARCHAR2(800)
        期权行权价   
    s_info_simulation: VARCHAR2(1)
        是否仿真交易   0:否1:是
    s_info_quoteunit: VARCHAR2(40)
        报价单位   
    s_info_counit: NUMBER(20)
        合约单位   
    s_info_counitdimension: VARCHAR2(40)
        合约单位量纲   

    """
    __tablename__ = "ChinaOptionContpro"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_code = Column(VARCHAR2(20))
    s_info_name = Column(VARCHAR2(40))
    s_info_ename = Column(VARCHAR2(100))
    s_info_exname = Column(VARCHAR2(20))
    s_info_type = Column(VARCHAR2(20))
    s_info_euroamericanbermuda = Column(VARCHAR2(10))
    s_info_settlementmethod = Column(VARCHAR2(10))
    s_info_listeddate = Column(VARCHAR2(8))
    s_info_delistdate = Column(VARCHAR2(8))
    s_info_strikeratio = Column(NUMBER(20,4))
    s_info_cevalue = Column(NUMBER(20,4))
    s_info_covalue = Column(VARCHAR2(80))
    s_info_lsmonth = Column(VARCHAR2(200))
    s_info_minpricefluct = Column(VARCHAR2(40))
    s_info_thours = Column(VARCHAR2(200))
    s_info_lasttradingdate = Column(VARCHAR2(200))
    s_info_lsdate = Column(VARCHAR2(200))
    s_info_lastsettle = Column(VARCHAR2(200))
    s_info_tradefee = Column(VARCHAR2(200))
    s_info_poslimit = Column(VARCHAR2(800))
    s_info_minposlimit = Column(VARCHAR2(800))
    s_info_optionprice = Column(VARCHAR2(20))
    s_info_exercisingend = Column(VARCHAR2(40))
    s_info_strikeprice = Column(VARCHAR2(800))
    s_info_simulation = Column(VARCHAR2(1))
    s_info_quoteunit = Column(VARCHAR2(40))
    s_info_counit = Column(NUMBER(20))
    s_info_counitdimension = Column(VARCHAR2(40))
    
