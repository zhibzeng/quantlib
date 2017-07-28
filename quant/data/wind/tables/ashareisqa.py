from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class AshareISQA(BaseModel):
    """
    4.116 中国A股机构调研问答明细

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    event_id: VARCHAR2(40)
        事件ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_askdate: VARCHAR2(8)
        提问日期   
    s_questiontype: NUMBER(9,0)
        问题内容分类代码   259001000生产经营259002000行业状况259003000融资259004000并购重组259005000人力资源259006000管理层259007000股权259008000重大事项259009000其他
    s_questioncontent: VARCHAR2(2000)
        问题内容   
    s_answercontent: VARCHAR2(4000)
        回答内容   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "AshareISQA"
    object_id = Column(VARCHAR2(100), primary_key=True)
    event_id = Column(VARCHAR2(40))
    s_info_windcode = Column(VARCHAR2(40))
    s_askdate = Column(VARCHAR2(8))
    s_questiontype = Column(NUMBER(9,0))
    s_questioncontent = Column(VARCHAR2(2000))
    s_answercontent = Column(VARCHAR2(4000))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
