"""
把回测的结构输出到HDF5文件中
"""
from ..common import AbstractMod, EventType
from ...common.settings import CONFIG
from ...common.logging import Logger


@AbstractMod.register
class Output(AbstractMod):
    """在回测结束后将每期的持仓、净值等信息输出为hdf5文件"""
    def __init__(self):
        if "OUTPUT" not in CONFIG.keys():
            CONFIG.add_argument("--output", "-o", action="append", help="output format",
                                choices=["sheet", "position"], default=[], required=False)
        super(Output, self).__init__()

    def on_backtest_finish(self, fund):
        filename = "%s_output.h5" % self.strategy.name
        formats = CONFIG.OUTPUT
        if "sheet" in formats:
            fund.sheet.to_hdf(filename, "sheet")
            Logger.info("Output sheet to %s" % filename)
        if "position" in formats:
            fund.position.to_hdf(filename, "position")
            Logger.info("Output position to %s" % filename)
