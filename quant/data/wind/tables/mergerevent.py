from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class MergerEvent(BaseModel):
    """
    并购事件

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    event_id: VARCHAR2(20)
        并购事件ID   
    s_info_windcode: VARCHAR2(200)
        参与方名称或代码   
    underlying: VARCHAR2(200)
        交易标的   
    trade_value: NUMBER(20, 4)
        交易总价值(万元)   
    cash_payment: NUMBER(20, 4)
        买方支付现金(万元)   
    crncy_code: VARCHAR2(10)
        货币代码   注1
    ann_date: VARCHAR2(8)
        首次披露日期   
    update_date: VARCHAR2(8)
        最新披露日期   
    completion_date: VARCHAR2(8)
        交易完成日期   
    stockright_proportion: NUMBER(20, 4)
        交易股权占比(%)   
    chronicle: VARCHAR2(4000)
        并购大事记   
    event_title: VARCHAR2(200)
        并购事件标题   
    underlying_type_code: NUMBER(9, 0)
        标的类型代码   注2
    progress_code: NUMBER(9, 0)
        交易方案进度代码   注3
    transfer_numbers: NUMBER(20, 4)
        转让股数(万股)   
    transfer_price: NUMBER(20, 4)
        转让单价   
    pricing_basis_code: NUMBER(9, 0)
        定价依据代码   注4
    evalue_method_code: NUMBER(9, 0)
        评估方法代码   注5
    payment_way_code: NUMBER(9, 0)
        支付方式代码   注6
    is_related_party_transac: NUMBER(1, 0)
        是否为关联交易   注7
    is_control_change: NUMBER(1, 0)
        控制权是否变更   注8
    evalue_basis_date_: VARCHAR2(8)
        资产评估基准日   
    evalue_value: NUMBER(20, 4)
        评估价值   
    appreciation_rate: NUMBER(20, 4)
        增值率   
    is_majorassetrestructure: NUMBER(1, 0)
        是否重大资产重组   注9
    is_merger: NUMBER(1, 0)
        是否并购   注10
    merger_aim_code: NUMBER(9, 0)
        并购目的类型代码   注11
    location_type_code: NUMBER(9, 0)
        并购地区类型代码   注12
    ecd: VARCHAR2(8)
        交易预计完成日期   
    merger_way_code: NUMBER(9, 0)
        并购方式代码   注13
    relevantintelligence_id: VARCHAR2(20)
        关联情报ID   
    merger_type_code: NUMBER(9, 0)
        并购类型代码   注14
    restructure_way_code: NUMBER(9, 0)
        重组形式代码   注15
    restructure_type_code: NUMBER(9, 0)
        重组类型代码   注16
    evalue_way_code: NUMBER(9, 0)
        选用评估方法代码   注17
    is_be_approval: NUMBER(1, 0)
        是否已完成审批   注18

    """
    __tablename__ = "MergerEvent"
    object_id = Column(VARCHAR2(100), primary_key=True)
    event_id = Column(VARCHAR2(20))
    s_info_windcode = Column(VARCHAR2(200))
    underlying = Column(VARCHAR2(200))
    trade_value = Column(NUMBER(20, 4))
    cash_payment = Column(NUMBER(20, 4))
    crncy_code = Column(VARCHAR2(10))
    ann_date = Column(VARCHAR2(8))
    update_date = Column(VARCHAR2(8))
    completion_date = Column(VARCHAR2(8))
    stockright_proportion = Column(NUMBER(20, 4))
    chronicle = Column(VARCHAR2(4000))
    event_title = Column(VARCHAR2(200))
    underlying_type_code = Column(NUMBER(9, 0))
    progress_code = Column(NUMBER(9, 0))
    transfer_numbers = Column(NUMBER(20, 4))
    transfer_price = Column(NUMBER(20, 4))
    pricing_basis_code = Column(NUMBER(9, 0))
    evalue_method_code = Column(NUMBER(9, 0))
    payment_way_code = Column(NUMBER(9, 0))
    is_related_party_transac = Column(NUMBER(1, 0))
    is_control_change = Column(NUMBER(1, 0))
    evalue_basis_date_ = Column(VARCHAR2(8))
    evalue_value = Column(NUMBER(20, 4))
    appreciation_rate = Column(NUMBER(20, 4))
    is_majorassetrestructure = Column(NUMBER(1, 0))
    is_merger = Column(NUMBER(1, 0))
    merger_aim_code = Column(NUMBER(9, 0))
    location_type_code = Column(NUMBER(9, 0))
    ecd = Column(VARCHAR2(8))
    merger_way_code = Column(NUMBER(9, 0))
    relevantintelligence_id = Column(VARCHAR2(20))
    merger_type_code = Column(NUMBER(9, 0))
    restructure_way_code = Column(NUMBER(9, 0))
    restructure_type_code = Column(NUMBER(9, 0))
    evalue_way_code = Column(NUMBER(9, 0))
    is_be_approval = Column(NUMBER(1, 0))
    
