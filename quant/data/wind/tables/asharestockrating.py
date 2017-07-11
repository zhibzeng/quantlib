from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareStockRating(BaseModel):
    """
    中国A股投资评级明细

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_est_institute: VARCHAR2(100)
        研究机构名称   
    s_est_ratinganalyst: VARCHAR2(100)
        分析师名称   
    s_est_estnewtime_inst: VARCHAR2(8)
        评级日期   
    s_est_scorerating_inst: NUMBER(20,4)
        本次标准评级   
    s_est_prescorerating_inst: NUMBER(20,4)
        前次标准评级   
    s_est_lowprice_inst: NUMBER(20,4)
        本次最低目标价   
    s_est_highprice_inst: NUMBER(20,4)
        本次最高目标价   
    s_est_prelowprice_inst: NUMBER(20,4)
        前次最低目标价   
    s_est_prehighprice_inst: NUMBER(20,4)
        前次最高目标价   
    ann_dt: VARCHAR2(8)
        公告日期(内部)   记录了盈利预测信息到达万得平台的时间，该字段精确到”日”，未保存具体的时点。
    s_est_rating_inst: VARCHAR(20)
        本次评级   
    s_est_prerating_inst: VARCHAR(20)
        前次评级   

    """
    __tablename__ = "AShareStockRating"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_est_institute = Column(VARCHAR2(100))
    s_est_ratinganalyst = Column(VARCHAR2(100))
    s_est_estnewtime_inst = Column(VARCHAR2(8))
    s_est_scorerating_inst = Column(NUMBER(20,4))
    s_est_prescorerating_inst = Column(NUMBER(20,4))
    s_est_lowprice_inst = Column(NUMBER(20,4))
    s_est_highprice_inst = Column(NUMBER(20,4))
    s_est_prelowprice_inst = Column(NUMBER(20,4))
    s_est_prehighprice_inst = Column(NUMBER(20,4))
    ann_dt = Column(VARCHAR2(8))
    s_est_rating_inst = Column(VARCHAR(20))
    s_est_prerating_inst = Column(VARCHAR(20))
    
