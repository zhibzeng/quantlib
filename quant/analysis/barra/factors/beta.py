import numpy as np
import pandas as pd
import statsmodels.api as sm
from ....common.localize import LOCALIZER
from ....common.math_helpers import exponential_decay_weight
from ....data import wind
from ..entities import get_estimation_universe
from .base import Descriptor, Factor


@Descriptor.register("Beta")
class BetaDescriptor(Descriptor):
    r"""
    Beta

    Computed as the slope coefficient in a time-series regression of excess stock return, 
    r_t - r_{ft} , against the cap-weighted excess return of the estimation universe R_t ,

    r_t-r_{ft} = \alpha + \beta R_t + e_t

    The regression coefficients are estimated over the trailing 252 trading days of returns 
    with a half-life of 63 trading days.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="beta")
    def get_raw_value(self):
        R = get_estimation_universe().get_returns()
        T = 252
        halflife = 63
        weights = exponential_decay_weight(halflife, T, reverse=True)
        stock_rtns = wind.get_wind_data("AShareEODPrices", "s_dq_pctchange") / 100
        df = pd.concat([R, stock_rtns.loc[R.index]], 1).truncate("2000-01-01")
        df[df==0] = np.nan
        result = []
        for i in range(T, len(df)):
            sub_df = df.iloc[i-T:i].dropna(axis=1, thresh=T//2)
            X, Y = sub_df.iloc[:, 0:1], sub_df.iloc[:, 1:]
            model = sm.WLS(Y.values, X.values, weights, missing='none').fit()
            result.append(pd.Series(model.params[0], index=Y.columns).rename(df.index[i]))
        result = pd.concat(result, 1).T
        return result

Beta = Factor("Beta", [BetaDescriptor()], [1.0])
