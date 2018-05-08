import base64
import io
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ..barra.entities import get_estimation_universe, Portfolio
from ..common.logging import Logger
from ..common.html import HTMLBase
from ..data import wind


class AlphaReport:
    def __init__(self, data, name):
        data.index = pd.to_datetime(data.index)
        self.data = data        
        self.name = name
        self.weight = self.data.div(self.data.abs().sum(0), 1)

    def generate_report(self):
        h = HTMLBase()
        with h.use(h.head):
            h.inline("title", _text=self.name)
        with h.use(h.body):
            h.inline("style", _text="body{text-align: center;}")
            with h.div():
                h.inline("h1", _text=self.name)

            with h.div():
                h.inline("h2", "Coverage")
                h.inline("hr")
                h.inline("img", src="data:image/gif;base64,{}".format(self.coverage()))

            with h.div():
                h.inline("h2", "Distribution")
                h.inline("hr")
                plot, skewness, kurtosis = self.distribution()
                h.inline("img", src="data:image/gif;base64,{}".format(plot))
                with h.table():
                    with h.tr():
                        h.inline("td", _text="skewness")
                        h.inline("td", _text="{:0.4f}".format(skewness))
                    with h.tr():
                        h.inline("td", _text="kurtosis")
                        h.inline("td", _text="{:0.4f}".format(kurtosis))
            
            with h.div():
                h.inline("h2", "Single Sort")
                h.inline("hr")
                cumulated_plot, bar_plot = self.single_sort()
                h.inline("img", src="data:image/gif;base64,{}".format(cumulated_plot))
                h.inline("img", src="data:image/gif;base64,{}".format(bar_plot))

            with h.div():
                h.inline("h2", "Intraday")
                h.inline("hr")
                h.inline("img", src="data:image/gif;base64,{}".format(self.intraday()))

            with h.div():
                h.inline("h2", "Alpha Decay")
                h.inline("hr")
                h.inline("img", src="data:image/gif;base64,{}".format(self.decay()))
            
        return h

    def coverage(self):
        """
        因子每期的覆盖率（有效值比例）
        """
        Logger.info("因子每期的覆盖率（有效值比例）")
        cap = wind.get_wind_data("AShareEODDerivativeIndicator", "s_val_mv")
        available = cap.dropna(how='all').notnull().sum(1)
        covered = self.data.dropna(how='all').notnull().sum(1)
        pct_coverage = (covered / available).dropna()
        sns.tsplot(pct_coverage)
        return self.get_plot()

    def distribution(self):
        """
        因子的横截面分布
        """
        Logger.info("因子的横截面分布")
        sns.distplot(pd.melt(self.data)['value'].dropna(), kde=False, norm_hist=True)
        skewness = self.data.skew(1).mean()
        kurtosis = self.data.kurt(1).mean()
        return self.get_plot(), skewness, kurtosis

    @staticmethod
    def get_plot():
        f = io.BytesIO()
        plt.savefig(f)
        f.seek(0)
        data = f.read()
        plt.cla()
        return base64.b64encode(data).decode()

    def single_sort(self):
        """
        单因子排序分组收益率
        """
        Logger.info("单因子排序分组收益率")
        rtns = wind.get_wind_data("AShareEODPrices", "s_dq_pctchange").replace(0, np.nan) / 100
        common_dates = sorted(set(self.data.index) & set(rtns.index))
        group_rtns = {}
        for date in common_dates:
            rtn = rtns.loc[date].dropna()
            score = self.data.loc[date].dropna()
            common_stocks = list(set(score.index) & set(rtn.index))
            rank = score[common_stocks].rank(ascending=False, pct=True)
            group = np.floor(rank * 10).astype(int)
            group_rtns[date] = rtn.groupby(group).mean().iloc[:-1]
        group_rtns = pd.DataFrame(group_rtns).T
        group_rtns.columns = group_rtns.columns.rename("group")
        group_rtns.index = group_rtns.index.rename("time")
        # data = group_rtns.cumsum().unstack().reset_index()
        # data['data'] = data[0]
        # sns.tsplot(data=data, condition="group", time="time", value="data").set_title("Group Returns")
        # plt.show()
        group_rtns.cumsum().plot()
        cumulated_plot = self.get_plot()
        sns.barplot(group_rtns.columns, group_rtns.mean() * 252).set_title("Avg Group Returns")
        bar_plot = self.get_plot()
        return cumulated_plot, bar_plot

    def intraday(self):
        """
        日内alpha分布
        """
        Logger.info("日内alpha分布")
        last_c = wind.get_wind_data("AShareEODPrices", "s_dq_adjclose")
        this_o = wind.get_wind_data("AShareEODPrices", "s_dq_adjopen").shift(-1)
        this_v = (wind.get_wind_data("AShareEODPrices", "s_dq_avgprice") * wind.get_wind_data("AShareEODPrices", "s_dq_adjfactor")).shift(-1)
        this_c = last_c.shift(-1)
        
        next_o = this_o.shift(-1)
        next_v = this_v.shift(-1)
        next_c = this_c.shift(-1)
        labels = [
            "last_c",
            "this_o",
            "this_v",
            "this_c",
            "next_o",
            "next_v",
            "next_c",
        ]
        alphas = [
            0,
            self._profit(self.weight, np.log(this_o / last_c)).mean(),
            self._profit(self.weight, np.log(this_v / last_c)).mean(),
            self._profit(self.weight, np.log(this_c / last_c)).mean(),
            self._profit(self.weight, np.log(next_o / last_c)).mean(),
            self._profit(self.weight, np.log(next_v / last_c)).mean(),
            self._profit(self.weight, np.log(next_c / last_c)).mean(),
        ]
        sns.barplot(labels, alphas).set_title("Intraday Alpha")
        return self.get_plot()

    @staticmethod
    def _profit(weight, rtn):
        rtn = (rtn * weight).dropna(how='all')
        normalizer = (rtn.notnull() * weight.abs()).sum(1)
        return rtn.sum(1) / normalizer

    def decay(self):
        """
        Alpha随天数变化
        """
        decay = []
        rtns = wind.get_wind_data("AShareEODPrices", "s_dq_pctchange") / 100
        for _ in range(20):
            rtns = rtns.shift(-1)
            alpha = self._profit(self.weight, rtns).mean()
            decay.append(alpha)
        sns.barplot(list(range(1, 21)), decay).set_title('Alpha Decay')
        return self.get_plot()

