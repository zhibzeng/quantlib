import numpy as np

from ...common.localize import LOCALIZER
from ...data import wind
from ...transform.distribution import compute_zscore
from .base import AbstractFactor


class Size(AbstractFactor):
    """
    A股当日流通市值

    ..  code-block:: python
    
        factor_freq = 20
        size = np.log(wind.get_wind_data("AShareEODDerivativeIndicator", "s_dq_mv"))
        z = compute_zscore(size, axis=0, inplace=True)
        return z
    """
    factor_name = "Size"
    factor_type = "Fundamental"
    factor_freq = 20

    @staticmethod
    @LOCALIZER.wrap(filename="factors", const_key="size")
    def get_factor_value():
        size = np.log(wind.get_wind_data("AShareEODDerivativeIndicator", "s_dq_mv"))
        z = compute_zscore(size, axis=0, inplace=True)
        return z
