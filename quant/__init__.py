"""
Quantlib
"""
import os
from . import data, transform, utils, analysis
with open(os.path.join(os.path.dirname(__file__), 'quant/VERSION')) as f:
    __version__ = f.read().strip()
__all__ = ['data', 'transform', 'utils', 'analysis', '__version__']
