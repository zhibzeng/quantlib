from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime, Column, BaseModel
VARCHAR2 = VARCHAR


class AShareRestructuringEvents(BaseModel):
    """
    中国A股重大重组事件

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        万得代码   
    progress: NUMBER(9,0)
        重组进度   324003002董事会预案324003004股东大会通过324003005国资委批准324003006商务部批准324003007证监会受理324003008证监会批准324004000完成324005000失败324005002停止实施具体参考类型编码表
    event: VARCHAR2(200)
        重组事件   
    form: NUMBER(9,0)
        重组形式代码   328001000协议收购328002000要约收购328003000管理层收购328004000回购328005000股权划拨328006000二级市场收购(含产权交易所)328007000吸收合并328012000发行股

    """
    __tablename__ = "AShareRestructuringEvents"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    progress = Column(NUMBER(9,0))
    event = Column(VARCHAR2(200))
    form = Column(NUMBER(9,0))
    
