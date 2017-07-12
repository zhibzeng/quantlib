from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareConsensusData(BaseModel):
    """
    中国A股盈利预测汇总

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    wind_code: VARCHAR2(40)
        Wind代码   
    est_dt: VARCHAR2(8)
        预测日期   
    est_report_dt: VARCHAR2(8)
        预测报告期   
    num_est_inst: NUMBER(20,0)
        预测机构家数   
    eps_avg: NUMBER(20,4)
        每股收益平均值(元)   
    main_bus_inc_avg: NUMBER(20,4)
        主营业务收入平均值(万元)   
    net_profit_avg: NUMBER(20,4)
        净利润平均值(万元)   
    ebit_avg: NUMBER(20,4)
        息税前利润平均值(万元)   
    ebitda_avg: NUMBER(20,4)
        息税折旧摊销前利润平均值(万元)   
    eps_median: NUMBER(20,4)
        每股收益中值(元)   
    main_bus_inc_median: NUMBER(20,4)
        主营业务收入中值(万元)   
    net_profit_median: NUMBER(20,4)
        净利润中值(万元)   
    ebit_median: NUMBER(20,4)
        息税前利润中值(万元)   
    ebitda_median: NUMBER(20,4)
        息税折旧摊销前利润中值(万元)   
    consen_data_cycle_typ: VARCHAR2(10)
        综合值周期类型   综合值周期类型:263001000:30天263002000:90天

    """
    __tablename__ = "AShareConsensusData"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    wind_code = Column(VARCHAR2(40))
    est_dt = Column(VARCHAR2(8))
    est_report_dt = Column(VARCHAR2(8))
    num_est_inst = Column(NUMBER(20,0))
    eps_avg = Column(NUMBER(20,4))
    main_bus_inc_avg = Column(NUMBER(20,4))
    net_profit_avg = Column(NUMBER(20,4))
    ebit_avg = Column(NUMBER(20,4))
    ebitda_avg = Column(NUMBER(20,4))
    eps_median = Column(NUMBER(20,4))
    main_bus_inc_median = Column(NUMBER(20,4))
    net_profit_median = Column(NUMBER(20,4))
    ebit_median = Column(NUMBER(20,4))
    ebitda_median = Column(NUMBER(20,4))
    consen_data_cycle_typ = Column(VARCHAR2(10))
    
