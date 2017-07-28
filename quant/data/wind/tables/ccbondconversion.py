from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CCBondConversion(BaseModel):
    """
    4.139 中国可转债转股

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    ann_dt: VARCHAR2(8)
        公告日期   
    conv_code: VARCHAR2(10)
        转股代码   
    conv_name: VARCHAR2(10)
        转股简称   
    conv_price: NUMBER(20,4)
        转股价格   
    crncy_code: VARCHAR2(10)
        货币代码   
    conv_startdate: VARCHAR2(8)
        自愿转换期起始日   
    conv_enddate: VARCHAR2(8)
        自愿转换期截止日   
    conv_enddate: VARCHAR2(8)
        可转债停止交易日   
    forced_conv_date: VARCHAR2(8)
        强制转换日   
    forced_conv_price: NUMBER(20,4)
        强制转换价格   
    rel_conv_month: NUMBER(20,4)
        相对转股期(月)   
    isforced: NUMBER(5,0)
        是否强制转股   
    forced_conv_reason: VARCHAR2(500)
        强制转换原因   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CCBondConversion"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    ann_dt = Column(VARCHAR2(8))
    conv_code = Column(VARCHAR2(10))
    conv_name = Column(VARCHAR2(10))
    conv_price = Column(NUMBER(20,4))
    crncy_code = Column(VARCHAR2(10))
    conv_startdate = Column(VARCHAR2(8))
    conv_enddate = Column(VARCHAR2(8))
    conv_enddate = Column(VARCHAR2(8))
    forced_conv_date = Column(VARCHAR2(8))
    forced_conv_price = Column(NUMBER(20,4))
    rel_conv_month = Column(NUMBER(20,4))
    isforced = Column(NUMBER(5,0))
    forced_conv_reason = Column(VARCHAR2(500))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
