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
    for member in dir(module):
        if member.lower() == module_name:
            Logger.debug("[Factor] Loaded factor {}".format(member))
            return getattr(module, member)


def get_factors():
    PATH = os.path.join(MAIN_PATH, "factors")
    factors = []
    if os.path.exists(PATH):
        for filename in os.listdir(PATH):
            if filename.endswith(".py") and filename != "__init__.py":
                try:
                    factors.append(load_factor(PATH, filename[:-3]))
                except:
                    pass
    return factors
