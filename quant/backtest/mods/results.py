"""Output simple backtest results on screen"""

from ..common.mods import AbstractMod, ModManager
from ..common.events import EventType
from ...common.logging import Logger
from ...common.settings import CONFIG
from ...data import wind


@ModManager.register(enable=True)
class ShowBasicResults(AbstractMod):
    """简单显示年化平均收益、年化波动和夏普率"""
    def on_backtest_finish(self, fund):
        net_value = fund.sheet["net_value"].copy()
        if CONFIG.BENCHMARK:
            benchmark = wind.get_wind_data("AIndexEODPrices", "s_dq_close")[CONFIG.BENCHMARK] \
                .dropna().truncate(self.strategy.start_date, self.strategy.end_date)
            benchmark /= benchmark.iloc[0]
            net_value /= benchmark
        profits = net_value.pct_change()
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

