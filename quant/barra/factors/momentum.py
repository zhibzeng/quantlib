import numpy as np
import pandas as pd
from ...common.localize import LOCALIZER
from ...common.math_helpers import exponential_decay_weight
from ...data import wind
from .base import Descriptor, Factor


@Descriptor.register("RSTR")
class RSTR(Descriptor):
    """
    Relative strength

    Computed as the sum of excess log returns over the trailing T = 504 trading days with a lag of L=21 tradingdays,
    
    ..  math:: RSTR = \Sigma_{t=L}^{T+L}w_t[ln(1+r_t)-ln(1+r_{ft})]
    
    where :math:`r_t` is the stock return on day t, :math:`r_{ft}` is the risk-free return, and :math:`w_t` is an
    exponential weight with a half-life of 126 trading days.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="rstr")
    def get_raw_value(self):
        T = 504
        L = 21
        halflife = 126
        weights = exponential_decay_weight(halflife, T)
        data = np.log(1 + wind.get_wind_data("AShareEODPrices", "s_dq_pctchange") / 100)
        # Truncated exponential moving average
        return data.rolling(T).apply(lambda y: np.nansum(y*weights) / (~np.isnan(y) @ weights)).shift(L)


Momentum = Factor("Momentum", [RSTR()], [1.0])
