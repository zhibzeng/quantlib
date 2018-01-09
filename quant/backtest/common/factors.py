"""
Search and import default factors automatically
The `get_factor` function finds modules under `~/.quantlib/factors`
and subclasses of the AbstractFactor and load them to
the namespace.
"""
import importlib
import os
import sys
from ...analysis.factors import AbstractFactor
from ...common.settings import MAIN_PATH
from ...common.logging import Logger


def load_factors(path, module_name):
    sys.path.insert(0, path)
    factors = []
    try:
        module = importlib.import_module(module_name)
    except:
        return factors
    for member_name in dir(module):
        member = getattr(module, member_name)
        if isinstance(member, type) and issubclass(member, AbstractFactor):
            Logger.debug("[Factor] Loaded factor {}".format(member_name))
            factors.append(member)
    del sys.path[0]
    return factors


__factors = None

def get_factors():
    """
    Finds modules under `~/.quantlib/factors`
    and subclasses of the AbstractFactor and
    load them to the namespace.
    """
    global __factors
    if __factors is None:
        __factors = []
        PATH = os.path.join(MAIN_PATH, "factors")
        if os.path.exists(PATH):
            for filename in os.listdir(PATH):
                if filename.endswith(".py") and filename != "__init__.py":
                    factors = load_factors(PATH, filename[:-3])
                    __factors.extend(factors)
    return __factors
