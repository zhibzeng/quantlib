from ..common.mods import AbstractMod
from ..common.events import EventType
from ...common.logging import Logger


@AbstractMod.register
class ShowBasicResults(AbstractMod):
    """简单显示年化平均收益、年化波动和夏普率"""
    def __init__(self):
        self.strategy = None

    def __plug_in__(self, caller):
        self.strategy = caller
        self.strategy.event_manager.register(EventType.BACKTEST_FINISH, self.on_backtest_finish)

    def on_backtest_finish(self, fund):
        profits = fund.sheet["net_value"].pct_change()
        info = dict()
        info["mean"] = profits.mean() * 252
        info["std"] = profits.std() * 252 ** 0.5
        info["sharpe"] = info["mean"] / info["std"]
        msg = (
            "Finished backtest\n"
            "Mean: %(mean).3f\n"
            "Std: %(std).3f\n"
            "Sharpe: %(sharpe).3f\n"
        ) % info
        Logger.info(msg)

