import os
import base64
from io import BytesIO
from abc import ABCMeta, abstractstaticmethod
import jinja2
import matplotlib.pyplot as plt
from docutils.core import publish_parts
from ...backtest import SimpleStrategy
from ...common.settings import CONFIG
from ...common.html import HTML
from ...data.wind import get_wind_data


class AbstractFactor(metaclass=ABCMeta):
    """Abstract class for stock factors"""
    factor_name = None
    factor_type = None
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
        strategy = SimpleStrategy(factor_values, mods=[])
        strategy.run()
        cls.h = HTML()
        with cls.h.html():
            cls.generate_head(factor_name)
            with cls.h.body():
                cls.generate_basics(factor_name)
                cls.generate_backtest(strategy)
                cls.generate_footer()
        docstring = cls.h.render()
        with open("%s.html" % factor_name, "w", encoding="utf8") as output_file:
            output_file.write(docstring)

    @classmethod
    def generate_head(cls, factor_name):
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
    def get_userdoc(cls):
        doc = cls.__doc__.split("\n")
        for line_no, line in enumerate(doc):
            if line.startswith("    "):
                doc[line_no] = line[4:]
        rst = "\n".join(doc)
        parts = publish_parts(rst, writer_name='html')
        return parts["stylesheet"], parts["html_body"]

    @classmethod
    def generate_basics(cls, factor_name):
        style_sheet, user_doc = cls.get_userdoc()
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
    def generate_backtest(cls, strategy):
        fund = strategy.fund
        net_value = fund.sheet.net_value.copy()
        benchmark = get_wind_data("AIndexEODPrices", "s_dq_close")["000905.SH"].dropna()
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
    def generate_ic(cls):
        real_rtn

    @classmethod
    def generate_footer(cls):
        js_files = (
            "https://code.jquery.com/jquery-3.1.1.slim.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js",
            "https://pingendo.com/assets/bootstrap/bootstrap-4.0.0-alpha.6.min.js",
        )
        for url in js_files:
            cls.h.inline("script", src=url)


class FactorDocGenerator:
    """A class to generate document for factors"""
    def __init__(self):
        pass

    def generate(self):
        pass
