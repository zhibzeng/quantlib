"""
Quantlib
"""
import os
import pkgutil
from . import data, transform, utils, analysis, abigale
from .abigale import Abigale, RestAPI
from .analysis import *
# from .backtest import *
from .data import wind
from .transform import *

__version__ = pkgutil.get_data('quant', 'VERSION')
if not isinstance(__version__, str):
    __version__ = __version__.decode('utf8')
__all__ = ['data', 'transform', 'utils', 'analysis', '__version__',
           'cal_mdd', 'get_ic', 'get_factor_exposure', 'AbstractFactor',
           'abigale', 'Abigale', 'RestAPI',
           'wind', 'find_extreme_values', 'compute_zscore',
           'get_residual', 'get_rtn', 'get_st_filter']
