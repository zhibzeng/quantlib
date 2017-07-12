from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AShareIssuingDatePredict(BaseModel):
    """
    中国A股定期报告披露日期

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    report_period: VARCHAR2(8)
        报告期   
    s_stm_predict_issuingdate: VARCHAR2(8)
        预计披露日期   
    s_stm_actual_issuingdate: VARCHAR2(8)
        实际披露日期   
    s_stm_correct_num: VARCHAR2(20)
        更正公告披露次数   
    s_stm_correct_issuingdate: VARCHAR2(100)
        更正公告披露日期   

    """
    __tablename__ = "AShareIssuingDatePredict"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    report_period = Column(VARCHAR2(8))
    s_stm_predict_issuingdate = Column(VARCHAR2(8))
    s_stm_actual_issuingdate = Column(VARCHAR2(8))
    s_stm_correct_num = Column(VARCHAR2(20))
    s_stm_correct_issuingdate = Column(VARCHAR2(100))
    
