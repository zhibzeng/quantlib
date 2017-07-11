from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class SIndexPerformance(BaseModel):
    """
    中国股票指数业绩表现

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    pct_chg_recent1m: NUMBER(20,6)
        最近1月涨跌幅   
    pct_chg_recent3m: NUMBER(20,6)
        最近3月涨跌幅   
    pct_chg_recent6m: NUMBER(20,6)
        最近6月涨跌幅   
    pct_chg_recent1y: NUMBER(20,6)
        最近1年涨跌幅   
    pct_chg_recent2y: NUMBER(20,6)
        最近2年涨跌幅   
    pct_chg_recent3y: NUMBER(20,6)
        最近3年涨跌幅   
    pct_chg_recent4y: NUMBER(20,6)
        最近4年涨跌幅   
    pct_chg_recent5y: NUMBER(20,6)
        最近5年涨跌幅   
    pct_chg_recent6y: NUMBER(20,6)
        最近6年涨跌幅   
    pct_chg_thisweek: NUMBER(20,6)
        本周以来涨跌幅   
    pct_chg_thismonth: NUMBER(20,6)
        本月以来涨跌幅   
    pct_chg_thisquarter: NUMBER(20,6)
        本季以来涨跌幅   
    pct_chg_thisyear: NUMBER(20,6)
        本年以来涨跌幅   
    si_pct_chg: NUMBER(20,6)
        发布以来涨跌幅   
    annualyeild: NUMBER(20,6)
        年化收益率   
    std_dev_6m: NUMBER(20,6)
        6个月标准差   
    std_dev_1y: NUMBER(20,6)
        1年标准差   
    std_dev_2y: NUMBER(20,6)
        2年标准差   
    std_dev_3y: NUMBER(20,6)
        3年标准差   
    sharpratio_6m: NUMBER(20,6)
        6个月夏普比率   
    sharpratio_1y: NUMBER(20,6)
        1年夏普比率   
    sharpratio_2y: NUMBER(20,6)
        2年夏普比率   
    sharpratio_3y: NUMBER(20,6)
        3年夏普比率   

    """
    __tablename__ = "SIndexPerformance"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    pct_chg_recent1m = Column(NUMBER(20,6))
    pct_chg_recent3m = Column(NUMBER(20,6))
    pct_chg_recent6m = Column(NUMBER(20,6))
    pct_chg_recent1y = Column(NUMBER(20,6))
    pct_chg_recent2y = Column(NUMBER(20,6))
    pct_chg_recent3y = Column(NUMBER(20,6))
    pct_chg_recent4y = Column(NUMBER(20,6))
    pct_chg_recent5y = Column(NUMBER(20,6))
    pct_chg_recent6y = Column(NUMBER(20,6))
    pct_chg_thisweek = Column(NUMBER(20,6))
    pct_chg_thismonth = Column(NUMBER(20,6))
    pct_chg_thisquarter = Column(NUMBER(20,6))
    pct_chg_thisyear = Column(NUMBER(20,6))
    si_pct_chg = Column(NUMBER(20,6))
    annualyeild = Column(NUMBER(20,6))
    std_dev_6m = Column(NUMBER(20,6))
    std_dev_1y = Column(NUMBER(20,6))
    std_dev_2y = Column(NUMBER(20,6))
    std_dev_3y = Column(NUMBER(20,6))
    sharpratio_6m = Column(NUMBER(20,6))
    sharpratio_1y = Column(NUMBER(20,6))
    sharpratio_2y = Column(NUMBER(20,6))
    sharpratio_3y = Column(NUMBER(20,6))
    
