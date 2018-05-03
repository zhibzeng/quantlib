import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from ....common.localize import LOCALIZER
from ....common.math_helpers import exponential_decay_weight
from ....data import wind
from .base import Descriptor, Factor
from .size import Size
from .beta import BetaDescriptor, Beta


@Descriptor.register("DASTD")
class DASTD(Descriptor):
    """
    Daily standard deviation

    Computed as the volatility of daily excess returns over the past 252 trading days with a half-life of 42 trading days.
    """
    def __init__(self):
        self.halflife = 42
        self.T = 252

    @LOCALIZER.wrap(filename="descriptors", const_key="dastd")
    def get_raw_value(self):
        weights = exponential_decay_weight(self.halflife, self.T, reverse=True)
        data = wind.get_wind_data("AShareEODPrices", "s_dq_pctchange") / 100
        data[data==0] = np.nan
        ewmstd = lambda series: (np.nansum(np.sqrt(((series-series.mean())**2 * weights)) / (~np.isnan(series) @ weights)))
        return data.rolling(self.T).apply(ewmstd)


@Descriptor.register("CMRA")
class CMRA(Descriptor):
    """
    Cumulative range

    This descriptor differentiates stocks that have experienced wide swings over the last 12 months 
    from those that have traded within a narrow range. Let Z(T) be the cumulative
    excess log return over the past T months, with each month defined as the previous 21 trading days.
    """
    def __init__(self):
        self.months = 12
        self.days_per_month = 21

    @LOCALIZER.wrap(filename="descriptors", const_key="cmra")
    def get_raw_value(self):
        daily_rtn = wind.get_wind_data("AShareEODPrices", "s_dq_pctchange") / 100
        return daily_rtn.rolling(self.months * self.days_per_month).apply(self.cmra)

    def cmra(self, series):
        monthly_rtn = series.reshape(self.months, self.days_per_month).sum(1)
        z = np.log(1 + np.log(monthly_rtn + 1))
        return z.max() - z.min()


@Descriptor.register("HSigma")
class HSigma(Descriptor):
    """
    Historical sigma

    Computed as the volatility of residual returns in Equation A1,
    The volatility is estimated over the trailing 252 trading days of returns with a half-life of
    63 trading days.
    The Residual Volatility factor is orthogonalized with respect to Beta and Size to reduce collinearity.
    """
    def __init__(self):
        self.T = 252
        self.halflife = 63

    @LOCALIZER.wrap(filename="descriptors", const_key="hsigma")
    def get_raw_value(self):
        rtns = wind.get_wind_data("AShareEODPrices", "s_dq_pctchange").loc["2005-01-01":] / 100
        beta = Descriptor.Beta().get_raw_value()
        resid = {}
        common_index = sorted(set(rtns.index) & set(beta.index))
        for idx in common_index:
            row = rtns.loc[idx]
            resid[idx] = row - row.mean() - beta.loc[idx]
        resid = pd.DataFrame(resid).T
        sigma = pd.ewmstd(resid, halflife=self.T)
        return sigma


ResidualVolatility = Factor("ResidualVolatility", [DASTD(), CMRA(), HSigma()], [0.74, 0.16, 0.10], disentangle=["Size", "Beta"])
