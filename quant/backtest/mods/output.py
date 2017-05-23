import pandas as pd
from ..common import AbstractMod, EventType


@AbstractMod.register
class Output(AbstractMod):
    """在回测结束后将每期的持仓、净值等信息输出为hdf5文件"""
    def __init__(self):
        self.strategy = None

    def __plug_in__(self, caller):
        self.strategy = caller
        caller.event_manager.register(EventType.BACKTEST_FINISH, self.on_backtest_finish)

    def on_backtest_finish(self, fund):
        fund.sheet.to_hdf("output.h5", "sheet")
        fund.position.to_hdf("output.h5", "position")
