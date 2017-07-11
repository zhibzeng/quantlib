from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareTTMAndMRQ(BaseModel):
    """
    中国A股TTM与MRQ

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    report_period: VARCHAR2(80)
        报告期   
    statement_type: VARCHAR2(10)
        报表类型   报表类型:408001000:合并报表408002000:合并报告(单季度)408003000:合并报告(单季度调整)408004000:合并报表(调整)408005000:合并报表(更正前)408006000:母公司报表408007000:母公司报表(单季度)408008000:母公司报告(单季度调整)408009000:母公司报表(调整)408010000:母公司报表(更正前)
    s_fa_or_ttm: NUMBER(20,4)
        营业收入(TTM)   
    s_fa_cost_ttm: NUMBER(20,4)
        营业成本-非金融类   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    report_period = Column(VARCHAR2(80))
    statement_type = Column(VARCHAR2(10))
    s_fa_or_ttm = Column(NUMBER(20,4))
    s_fa_cost_ttm = Column(NUMBER(20,4))
    
