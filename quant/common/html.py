import json
from contextlib import contextmanager
from itertools import starmap
import pandas as pd
import jinja2


class HTML:
    """用上下文管理器生成HTML文档

    Example
    -------
    ..  code-block:: python

        doc = HTML()
        with doc.html():
            with doc.head():
                doc.inline("titile", _text="Generated HTML")
            with doc.body():
                with doc.div(_class="container"):
                    with doc.div(_class="row"):
                        doc.inline("p", _text="paragraph")
        html = doc.render()
    """
    def __init__(self):
        self.docstring = []
        self.level = 0
    
    @staticmethod
    def series2json(series):
        """把pd.Series时间序列转换为json格式"""
        series = series.copy()
        series.index = series.index.astype(int) / 1e6
        return json.dumps(sorted([[int(key), value] for key, value in series.to_dict().items()]))

    def text(self, txt):
        self.print(txt)

    def inline(self, tag, **kwargs):
        if "_class" in kwargs:
            kwargs["class"] = kwargs["_class"]
            del kwargs["_class"]
        try:
            text = kwargs["_text"]
            del kwargs["_text"]
        except KeyError:
            text = ""
        attributes = ' '.join(map("%s=%s".__mod__, kwargs.items()))
        if attributes:
            self.print('<%s %s>%s</%s>' % (tag, attributes, text, tag))
        else:
            self.print('<%s>%s</%s>' % (tag, text, tag))

    def __getattr__(self, item):
        @contextmanager
        def wrapped(**kwargs):
            if "_class" in kwargs:
                kwargs["class"] = kwargs["_class"]
                del kwargs["_class"]
            for key, value in kwargs.items():
                if isinstance(value, str):
                    kwargs[key] = '"%s"' % value
                else:
                    kwargs[key] = str(value)
            tag_name = item
            attributes = ' '.join(starmap(lambda key, value: "%s=%s" % (key, value), kwargs.items()))
            if attributes:
                self.print('<%s %s>' % (tag_name, attributes))
            else:
                self.print('<%s>' % tag_name)
            self.level += 1
            yield
            self.level -= 1
            self.print('</%s>' % tag_name)
        return wrapped

    def print(self, source):
        prefix = ' ' * (2 * self.level)                            # Two-space indent
        self.docstring.append(prefix + source)

    def render(self):
        return "\n".join(self.docstring)

    def highcharts(self, name, data, plot_type=None):
        """
        Insert highcharts.

        Parameters
        ----------
        name: str
            Name of the chart.
        data: pd.DataFrame
            data to be converted to chart
        plot_type: dict
            type to be plotted. NOT IMPLEMENTED YET!
        """
        plot_type = plot_type or {}
        if isinstance(plot_type, str):
            if isinstance(data, pd.DataFrame):
                plot_type = {col_name: plot_type for col_name in data.columns}
            else:
                plot_type = {data.name: plot_type}
        self.inline('div',
                    id="highcharts-%s" % name,
                    style="height: 400px; width: 100%; min-width: 310px")
        embedded_data = []
        if isinstance(data, pd.DataFrame):
            for col in data.columns:
                series = data[col]
                embedded_data.append((series.name, self.series2json(series)))
        elif isinstance(data, pd.Series):
            embedded_data.append((data.name, self.series2json(data)))
        else:
            raise TypeError("Data must be either DataFrame or Series")

        template = jinja2.Template("""
        Highcharts.stockChart('highcharts-{{name}}', {
            rangeSelector: {
                selected: 5
            },
            title: {
                text: '{{name}}'
            },
            series: [
                # for s_name, s_value in data
                {
                    name: '{{ s_name }}',
                    data: {{ s_value }},
                    type: '{{ plot_type.get(s_name, "line") }}',
                    tooltip: {
                        valueDecimals: 3
                    }
                }
                # endfor
            ]
        });
        """)

        self.inline("script",
                    _text=template.render(name=name, data=embedded_data, plot_type=plot_type))

    def generate_table(self, data,
                       show_headers=True,
                       show_index=True,
                       hover=True,
                       bordered=True,
                       striped=False,
                       **kwargs):
        """Generate a table

        Parameters
        ----------
        data: pd.DataFrame
            data to be converted to a table
        show_headers: bool
            whether to show the column names as first row
        show_index: bool
            whether to show the index as first column
        hover: bool
            table-hover class
        bordered: bool
            table-bordered class
        striped:
            table-striped class
        kwargs
            other attributes to be added to table
        """
        if "_class" in kwargs:
            kwargs["class"] = kwargs["_class"] + " table"
            del kwargs["_class"]
        else:
            kwargs["class"] = "table"
        if hover:
            kwargs["class"] += " table-hover"
        if bordered:
            kwargs["class"] += " table-bordered"
        if striped:
            kwargs["class"] += " table-striped"
        with self.table(**kwargs):
            if show_headers:
                with self.thead():
                    with self.tr():
                        if show_index:
                            self.inline('th', _text=data.index.name or "#")
                        for col in data.columns:
                            self.inline("th", _text=col)
            with self.tbody():
                for idx, data in data.iterrows():
                    with self.tr():
                        if show_index:
                            self.inline("td", _text=str(idx))
                        for val in data:
                            self.inline('td', _text=str(val))
