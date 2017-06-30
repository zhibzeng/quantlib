"""
Quantlib
"""
import os
import pkgutil
from . import data, transform, utils, analysis
__version__ = pkgutil.get_data('quant', 'VERSION')
if not isinstance(__version__, str):
    __version__ = __version__.decode('utf8')
__all__ = ['data', 'transform', 'utils', 'analysis', '__version__']
