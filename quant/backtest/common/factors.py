"""
Search and import default factors automatically
"""
import importlib
import os
import sys
from ...analysis.factors import AbstractFactor
from ...common.settings import MAIN_PATH
from ...common.logging import Logger


def load_factor(path, module_name):
    sys.path.insert(0, path)
    module = importlib.import_module(module_name)
    factor = None
    for member in dir(module):
        if member.lower().replace("_", "") == module_name.replace("_", ""):
            Logger.debug("[Factor] Loaded factor {}".format(member))
            factor = getattr(module, member)
            break
    del sys.path[0]
    return factor


__factors = None

def get_factors():
    global __factors
    if __factors is None:
        __factors = []
        PATH = os.path.join(MAIN_PATH, "factors")
        if os.path.exists(PATH):
            for filename in os.listdir(PATH):
                if filename.endswith(".py") and filename != "__init__.py":
                    try:
                        factor = load_factor(PATH, filename[:-3])
                        if factor is not None:
                            __factors.append(factor)
                    except:
                        pass
    return __factors
