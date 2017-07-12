from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondfloatingrate(BaseModel):
    """
    中国债券浮息债基础利率属性

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    b_info_benchmarkcode: NUMBER(9,0)
        基准利率代码   1、SHIBOR2、LIBOR3、7天回购定盘利率4、7天回购利率平均值5、半年期定期存款利率6、三个月定期存款利率7、1年期定期存款利率
    b_info_marketrateornot: NUMBER(5,0)
        基准利率是否是市场化利率   
    b_info_interestcode: VARCHAR2(20)
        市场化利率代码   
    b_info_interestfloor: NUMBER(20,4)
        保底利率(%)   
    b_info_paymentdaytype: VARCHAR2(2)
        计算基准利率所用付息日类型   1、前次付息日2、前次付息日的前一工作日3、付息日前两个工作日
    b_info_interestpreci: NUMBER(1,0)
        基准利率精度   0、基准利率未明确要求保留多少位小数2、基准利率要求保留两位小数

    """
    __tablename__ = "CBondfloatingrate"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    b_info_benchmarkcode = Column(NUMBER(9,0))
    b_info_marketrateornot = Column(NUMBER(5,0))
    b_info_interestcode = Column(VARCHAR2(20))
    b_info_interestfloor = Column(NUMBER(20,4))
    b_info_paymentdaytype = Column(VARCHAR2(2))
    b_info_interestpreci = Column(NUMBER(1,0))
    
