from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareIncDescription(BaseModel):
    """
    中国A股股权激励基本资料

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_inc_sequence: VARCHAR2(6)
        序号   
    s_inc_subject: NUMBER(9,0)
        激励标的   1.期权2.股票3.股票增值权
    s_inc_type: NUMBER(9,0)
        激励方式   1.股东转让股票2.股票增值权3.上市公司定向发行股票4.上市公司提取激励基金买入流通A股5.授予期权,行权股票来源为股东转让股票6.授予期权,行权股票来源为上市公司定向发行股票
    s_inc_quantity: NUMBER(20,4)
        激励总数(万股/万份)   
    s_inc_firstinc: VARCHAR2(8)
        起始日   
    s_inc_endinc: VARCHAR2(8)
        到期日   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_inc_sequence = Column(VARCHAR2(6))
    s_inc_subject = Column(NUMBER(9,0))
    s_inc_type = Column(NUMBER(9,0))
    s_inc_quantity = Column(NUMBER(20,4))
    s_inc_firstinc = Column(VARCHAR2(8))
    s_inc_endinc = Column(VARCHAR2(8))
    
