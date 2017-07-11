from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class CBondBenchmark(BaseModel):
    """
    法定存贷款利率

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    trade_dt: VARCHAR2(8)
        交易日期   
    b_info_benchmark: VARCHAR2(10)
        存贷款利率类型   01010100个人活期01010201个人定期(整存整取)三个月01010202个人定期(整存整取)半年01010203个人定期(整存整取)一年01010204个人定期(整存整取)二年01010205个人定期(整存整取)三年01010206个人定期(整存整取)五年01010207个人定期(整存整取)八年及以上01010301个人定期(零存整取,整存零取,存本取息)一年01010302个人定期(零存整取,整存零取,存本取息)三年01010303个人定期(零存整取,整存零取,存本取息)五年01010700通知存款01010702通知存款七天01010701通知存款一天01010600协定存款02020206短期贷款六个月02020207短期贷款一年02020208中长期贷款一至三年(含)02020209中长期贷款三至五年(含)02020210中长期贷款五年以上

    """
    __tablename__ = "CBondBenchmark"
    object_id = Column(VARCHAR2(100), primary_key=True)
    trade_dt = Column(VARCHAR2(8))
    b_info_benchmark = Column(VARCHAR2(10))
    
