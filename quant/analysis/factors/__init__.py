import os
import base64
from io import BytesIO
from abc import abstractstaticmethod
import jinja2
import matplotlib.pyplot as plt
from docutils.core import publish_parts
from ...analysis import get_ic
from ...backtest import SimpleStrategy
from ...common.settings import CONFIG
from ...common.html import HTML
from ...data.wind import get_wind_data


class AbstractFactor:
    """Abstract class for stock factors"""
    factor_name = None
    factor_type = None
    factor_freq = None
    h = None

    @abstractstaticmethod
    def get_factor_value():
        """
        This method should return a pd.DataFrame
        that contains factor values.
        """
        raise NotImplementedError

    @classmethod
    def generate_doc(cls):
        """Generate factor document"""
        factor_name = cls.factor_name or cls.__name__
        factor_values = cls.get_factor_value()
        # strategy = SimpleStrategy(factor_values, mods=[])
        # strategy.run()
        cls.h = HTML()
        with cls.h.html():
            cls._generate_head(factor_name)
            with cls.h.body():
                cls._generate_basics(factor_name)
                # cls._generate_backtest(strategy)
                cls._generate_ic(factor_values)
                cls._generate_footer()
        docstring = cls.h.render()
        with open("%s.html" % factor_name, "w", encoding="utf8") as output_file:
            output_file.write(docstring)

    @classmethod
    def _generate_head(cls, factor_name):
        css_files = (
            "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
            "https://pingendo.com/assets/bootstrap/bootstrap-4.0.0-alpha.6.css",
        )
        with cls.h.head():
            cls.h.inline("meta", charset="utf-8")
            cls.h.inline("meta", name="viewport", content="width=device-width, initial-scale=1")
            for url in css_files:
                cls.h.inline("link", rel="stylesheet", href=url, type="text/css")
            cls.h.inline("title", _text=factor_name)

    @classmethod
    def _get_userdoc(cls):
        doc = cls.__doc__.split("\n")
        for line_no, line in enumerate(doc):
            if line.startswith("    "):
                doc[line_no] = line[4:]
        rst = "\n".join(doc)
        parts = publish_parts(rst, writer_name='html')
        return parts["stylesheet"], parts["html_body"]

    @classmethod
    def _generate_basics(cls, factor_name):
        style_sheet, user_doc = cls._get_userdoc()
        h = cls.h
        h.print(style_sheet)
        with h.div(_class="py-5"):
            with h.div(_class="container"):
                with h.div(_class="row"):
                    with h.div(_class="col-md-12"):
                        h.inline("h1", _class="display-1", _text=factor_name.upper())
        h.inline("hr")
        with h.div(_class="py-5"):
            with h.div(_class="container"):
                with h.div(_class="row"):
                    with h.div(_class="col-md-12"):
                        h.print(user_doc)

    @classmethod
    def _generate_backtest(cls, strategy):
        fund = strategy.fund
        net_value = fund.sheet.net_value.copy()
        benchmark = get_wind_data("AIndexEODPrices", "s_dq_close")[CONFIG.BENCHMARK].dropna()
        benchmark /= benchmark.iloc[0]
        net_value = (net_value / benchmark).dropna()
        rtns = net_value.pct_change()

        mean = rtns.mean() * 100 * 252
        std = rtns.std() * 100 * 252 ** .5
        sharpe = mean / std
        net_value.plot()
        with BytesIO() as tmp:
            plt.savefig(tmp, format="png")
            tmp.seek(0)
            raw_img = tmp.read()
            img_netvalue = base64.b64encode(raw_img).decode('utf8').replace('\n', '')
        h = cls.h
        with h.div(_class="py-5"):
            with h.div(_class="container"):
                with h.div(_class="row"):
                    h.inline("h1", _text="Backtest")
                    h.inline("hr")
                with h.div(_class="row"):
                    with h.div(_class="col-md-3"):
                        with h.ul(_class="list-group py-5 my-5"):
                            h.inline("li", _class="list-group-item", _text="Mean: %.2f%%" % mean)
                            h.inline("li", _class="list-group-item", _text="Std: %.2f%%" % std)
                            h.inline("li", _class="list-group-item", _text="Sharpe: %.2f" % sharpe)
                    with h.div(_class="col-md-9"):
                        h.inline('img', src='data:image/png;base64,{0}'.format(img_netvalue))

    @classmethod
    def _generate_ic(cls, data):
        data = data.truncate("2005-01-01")
        real_price = get_wind_data("AShareEODPrices", "s_dq_adjclose")
        # real_price = real_price.resample("1d").ffill()
        real_price = real_price.loc[data.index]
        real_rtn = real_price.pct_change()
        ic_score = get_ic(data.shift(1), real_rtn)
        ic_score = ic_score.resample("1m").mean()
        with BytesIO() as tmp:
            plt.figure(figsize=(10, 5))
            ax = ic_score.plot(kind='bar', color='red')
            xticks = ax.get_xticks()
            ax.plot(xticks, ic_score.rolling(6).mean())
            num_labels = 10
            xlabels = [ic_score.index[i].strftime("%b %Y")
                       if i % (len(xticks) // num_labels) == 0 else ""
                       for i in range(len(xticks))]
            ax.set_xticks(xticks)
            ax.set_xticklabels(xlabels)
            plt.xticks(rotation=10)
            plt.savefig(tmp, format="png")
            plt.cla()
            tmp.seek(0)
            raw_img = tmp.read()
            img_ic = base64.b64encode(raw_img).decode('utf8').replace('\n', '')
        h = cls.h
        with h.div(_class="py-5"):
            with h.div(_class="container"):
                with h.div(_class="row"):
                    h.inline("h1", _text="IC")
                    h.inline("hr")
                with h.div(_class="row"):
                    with h.div(_class="col-md-12"):
                        h.inline('img', src='data:image/png;base64,{0}'.format(img_ic))

    @classmethod
    def _generate_footer(cls):
        js_files = (
            "https://code.jquery.com/jquery-3.1.1.slim.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js",
            "https://pingendo.com/assets/bootstrap/bootstrap-4.0.0-alpha.6.min.js",
        )
        for url in js_files:
            cls.h.inline("script", src=url)
