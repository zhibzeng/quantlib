from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareProfitNotice(BaseModel):
    """
    中国A股业绩预告

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_profitnotice_date: VARCHAR2(8)
        公告日期   
    s_profitnotice_period: VARCHAR2(8)
        报告期   
    s_profitnotice_style: NUMBER(9,0)
        业绩预告类型代码   业绩预告类型：不确定454001000略减454002000略增454003000扭亏454004000其他454005000首亏454006000续亏454007000续盈454008000预减454009000预增454010000
    s_profitnotice_signchange: VARCHAR2(10)
        是否变脸   1：是；0：否
    s_profitnotice_changemin: NUMBER(20,4)
        预告净利润变动幅度下限(%)   
    s_profitnotice_changemax: NUMBER(20,4)
        预告净利润变动幅度上限(%)   
    s_profitnotice_netprofitmin: NUMBER(20,4)
        预告净利润下限(万元)   
    s_profitnotice_netprofitmax: NUMBER(20,4)
        预告净利润上限(万元)   
    s_profitnotice_number: NUMBER(15,4)
        公布次数   
    s_profitnotice_firstanndate: VARCHAR2(8)
        首次公告日   
    s_profitnotice_abstract: VARCHAR2(200)
        业绩预告摘要   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_profitnotice_date = Column(VARCHAR2(8))
    s_profitnotice_period = Column(VARCHAR2(8))
    s_profitnotice_style = Column(NUMBER(9,0))
    s_profitnotice_signchange = Column(VARCHAR2(10))
    s_profitnotice_changemin = Column(NUMBER(20,4))
    s_profitnotice_changemax = Column(NUMBER(20,4))
    s_profitnotice_netprofitmin = Column(NUMBER(20,4))
    s_profitnotice_netprofitmax = Column(NUMBER(20,4))
    s_profitnotice_number = Column(NUMBER(15,4))
    s_profitnotice_firstanndate = Column(VARCHAR2(8))
    s_profitnotice_abstract = Column(VARCHAR2(200))
    
