import numpy as np

from ...common.localize import LOCALIZER
from ...data import wind
from ...transform.stocks import get_rtn
from ...transform.distribution import compute_zscore
from .base import AbstractFactor


class Momentum(AbstractFactor):
    """
    A股近20日横截面动量
    """
    factor_name = "Momentum"
    factor_type = "Technical"
    factor_freq = 20

    @staticmethod
    @LOCALIZER.wrap(filename="factors", const_key="momentum")
    def get_factor_value():
        rtn = get_rtn(wind.get_wind_data("AShareEODPrices", "s_dq_adjclose"), 10, False)
        z = compute_zscore(rtn, axis=0, inplace=True)
        return z
