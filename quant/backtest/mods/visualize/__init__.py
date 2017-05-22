import os
import json
import webbrowser
from datetime import datetime
import jinja2
from IPython.display import display, HTML
from ...common.events import EventType
from ...common.mods import AbstractMod
from ....data import wind

TEMPLATE_FILE = os.path.join(os.path.split(os.path.realpath(__file__))[0], "statics/template.html")


def in_ipynb():
    try:
        cfg = get_ipython().config
        return cfg['IPKernelApp']['parent_appname'] == 'ipython-notebook'
    except NameError:
        return False


@AbstractMod.register
class WebVisualizer(AbstractMod):
    """回测结束后在网页中显示回测的详细信息"""
    def __init__(self):
        self.strategy = None

    def __plug_in__(self, caller):
        self.strategy = caller
        self.strategy.event_manager.register(EventType.BACKTEST_FINISH, self.on_backtest_finish)

    @staticmethod
    def series2json(series):
        s = series.copy()
        s.index = s.index.astype(int) / 1e6
        return json.dumps(sorted([[int(key), value] for key, value in s.to_dict().items()]))

    def on_backtest_finish(self, fund):
        stocks = {}
        position = fund.position.copy()
        position.index = position.index.astype(int) / 1e6
        for date, pos in position.iterrows():
            stocks[str(date)] = list(pos[pos>0].to_dict().items())
            # stocks[date.value] = list(position[position>0].to_dict().items())
        benchmark = wind.get_wind_data("AIndexEODPrices", "s_dq_close")["000905.SH"] \
            .dropna().truncate(self.strategy.start_date, self.strategy.end_date)
        benchmark /= benchmark.iloc[0]
        info = {}
        info["strategy_name"] = self.strategy.name
        info["start_date"] = self.strategy.start_date
        info["end_date"] = self.strategy.end_date
        info["fee_rate"] = self.strategy.fee_rate
        info["net_value"] = self.series2json(fund.sheet["net_value"])
        info["benchmark"] = self.series2json(benchmark)
        info["relative"] = self.series2json((fund.sheet["net_value"] / benchmark).dropna())
        info["stocks"] = json.dumps(stocks)
        info["fee"] = fund.sheet["fee"].sum()
        with open(TEMPLATE_FILE, encoding="utf8") as template_file:
            template = jinja2.Template(template_file.read())
        html = template.render(**info)
        if in_ipynb():
            display(HTML(html))
        else:
            filename = "%s_%s.html" % \
                (info["strategy_name"], datetime.now().strftime("%Y%m%d%H%M%S"))
            filename = os.path.abspath(filename)
            with open(filename, "w", encoding="utf8") as output_file:
                output_file.write(html)
            print("HTML results output to: %s" % filename)
            webbrowser.open_new_tab(filename)

