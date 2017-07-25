"""回测结束后在网页中显示回测的详细信息"""
import os
import sys
import json
import webbrowser
import base64
from io import BytesIO
from datetime import datetime
import jinja2
import matplotlib.pyplot as plt
from IPython.display import display, IFrame
from ...common.events import EventType
from ...common.mods import AbstractMod
from ....analysis import get_factor_exposure
from ....data import wind
from ....common.settings import CONFIG
from ....common.logging import Logger

TEMPLATE_FILE = os.path.join(os.path.split(os.path.realpath(__file__))[0], "statics/template.html")


def in_ipynb():
    """判断当前是否为jupyter notebook环境"""
    try:
        from IPython import get_ipython, terminal
        this = get_ipython()
        return not isinstance(this, terminal.interactiveshell.TerminalInteractiveShell)
    except:
        return False


@AbstractMod.register
class WebVisualizer(AbstractMod):
    """回测结束后在网页中显示回测的详细信息"""

    risk_factors = set()

    def __init__(self):
        self.strategy = None

    def __plug_in__(self, caller):
        self.strategy = caller
        CONFIG.add_argument("--no_browser", action="store_false", dest="open_browser")
        self.strategy.event_manager.register(EventType.BACKTEST_FINISH, self.on_backtest_finish)
        Logger.debug("[Mod WebVisualizer] initialized.")

    @classmethod
    def register_factor(cls, factor):
        cls.risk_factors.add(factor)

    @staticmethod
    def series2json(series):
        """把pd.Series时间序列转换为json格式"""
        series = series.copy()
        series.index = series.index.astype(int) / 1e6
        return json.dumps(sorted([[int(key), value] for key, value in series.to_dict().items()]))

    def get_benchmark(self):
        """获取基准标的的净值"""
        benchmark = wind.get_wind_data("AIndexEODPrices", "s_dq_close")[CONFIG.BENCHMARK] \
            .dropna().truncate(self.strategy.start_date, self.strategy.end_date)
        benchmark /= benchmark.iloc[0]
        return benchmark

    def get_exposure(self, position, factor):
        """计算持仓的因子暴露"""
        factor_name = factor.factor_name
        factor_value = factor.get_factor_value()
        exposure = get_factor_exposure(position, factor_value, benchmark=CONFIG.BENCHMARK).resample("1m").mean()
        return self.series2json(exposure)

    def on_backtest_finish(self, fund):
        stocks = {}
        position = fund.position.copy()
        position.index = position.index.astype(int) // 1000000
        for date, pos in position.iterrows():
            stocks[str(date)] = list(pos[pos > 0].to_dict().items())
        benchmark = self.get_benchmark()
        info = {}
        info["strategy_name"] = self.strategy.name
        info["start_date"] = self.strategy.start_date
        info["end_date"] = self.strategy.end_date
        info["fee_rate"] = CONFIG.FEE_RATE
        info["net_value"] = self.series2json(fund.sheet["net_value"])
        info["benchmark"] = self.series2json(benchmark)
        info["relative"] = self.series2json((fund.sheet["net_value"] / benchmark).dropna())
        info["stocks"] = json.dumps(stocks)
        info["fee"] = fund.sheet["fee"].sum()
        info["exposure"] = sorted([(factor.factor_name.replace(" ", ""), self.get_exposure(fund.position, factor)) for factor in self.risk_factors])
        with open(TEMPLATE_FILE, encoding="utf8") as template_file:
            template = jinja2.Template(template_file.read())
        html = template.render(**info)
        filename = "%s.html" % info["strategy_name"]
        filename = os.path.realpath(filename)
        with open(filename, "w", encoding="utf8") as output_file:
            output_file.write(html)
        Logger.info("HTML results output to: %s" % filename)
        if in_ipynb():
            return IFrame(src=filename, width="100%", height="800")
        elif CONFIG.OPEN_BROWSER:
            webbrowser.open_new_tab(filename)

