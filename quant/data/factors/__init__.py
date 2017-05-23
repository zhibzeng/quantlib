import os
from abc import ABCMeta, abstractstaticmethod
import jinja2
from docutils.core import publish_string
from ...backtest import SimpleStrategy


"""
data_uri = open('11.png', 'rb').read().encode('base64').replace('\n', '')
img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
"""


_TEMPLATE_FILE = os.path.join(os.path.split(os.path.realpath(__file__))[0], "statics/template.rst")

class AbstractFactor(metaclass=ABCMeta):
    """Abstract class for stock factors"""
    factor_name = None
    factor_type = None
    docstring = None
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
        factor_values = cls.get_factor_value()
        strategy = SimpleStrategy(factor_values, mods=[])
        strategy.run()
        cls.docstring = []
        cls.generate_basics()
        cls.generate_backtest(strategy)

    @classmethod
    def get_userdoc(cls):
        doc = cls.__doc__.split("\n")
        common_space_prefix = min([len(x) - len(x.lstrip()) for x in doc])
        doc = [x[common_space_prefix:] for x in doc]
        return "\n".join(doc)

    @classmethod
    def generate_basics(cls):
        factor_name = cls.factor_name or cls.__name__
        cls.docstring.append(factor_name)
        cls.docstring.append("=" * len(factor_name))
        cls.docstring.append("")
        cls.docstring.append(cls.get_userdoc())
        cls.docstring.append("")

    @classmethod
    def generate_summary(cls):
        cls.docstring.append("Summary")
        cls.docstring.append("-------")
        cls.docstring.append("")
        cls.docstring.append("|Type: %s" % cls.factor_type)
        cls.docstring.append("|Mean: %0.2f%%" % cls.factor_type)
        cls.docstring.append("")

    @classmethod
    def get_bactest(cls, strategy):
        cls.docstring.append("Backtest")
        cls.docstring.append("--------")
        cls.docstring.append()


class FactorDocGenerator:
    """A class to generate document for factors"""
    def __init__(self):
        pass

    def generate(self):
        pass
