import numpy as np
import pandas as pd
from ...common.localize import LOCALIZER
from ...data import wind
from .base import Descriptor, Factor


@Descriptor.register("STOM")
class STOM(Descriptor):
    r"""
    Share turnover, one month

    Computed as the log of the sum of daily turnover during the previous 21 trading days,

    STOM = ln[\Sigma_{t=1}^{21}\frac{V_t}{S_t}]

    where Vt is the trading volume on day t , and St is the number of shares outstanding.
    """
    def __init__(self):
        self.T = 21

    @LOCALIZER.wrap(filename="descriptors", const_key="stom")
    def get_raw_value(self):
        amount = wind.get_wind_data("AShareEODPrices", "s_dq_amount")
        size = wind.get_wind_data("AShareEODDerivativeIndicator", "s_val_mv")
        stom = np.log((amount / size).dropna(how='all').rolling(self.T).sum() + 1e-6)
        return stom


@Descriptor.register("STOQ")
class STOQ(Descriptor):
    r"""
    Share turnover, trailing 3 months

    Let STOM_t be the share turnover for month t , with each month consisting of 21 trading days. 
    The quarterly share turnover is defined by
    
    STOQ = ln[\frac{1}{T}\Sigma_{t=1}{T}exp\{STOM_t\}]
    where T = 3 months.
    """
    def __init__(self):
        self.T = 3

    @LOCALIZER.wrap(filename="descriptors", const_key="stoq")
    def get_raw_value(self):
        stom = STOM().get_raw_value()
        stoq = np.log(np.exp(stom).rolling(self.T*21).mean())
        return stoq


@Descriptor.register("STOA")
class STOA(Descriptor):
    r"""
    Share turnover, trailing 12 months

    Let STOM_t be the share turnover for month t , with each month consisting of 21 trading days. 
    The quarterly share turnover is defined by
    
    STOQ = ln[\frac{1}{T}\Sigma_{t=1}{T}exp\{STOM_t\}]
    where T = 12 months.
    """
    def __init__(self):
        self.T = 12

    @LOCALIZER.wrap(filename="descriptors", const_key="stoa")
    def get_raw_value(self):
        stom = STOM().get_raw_value()
        stoa = np.log(np.exp(stom).rolling(self.T*21).mean())
        return stoa


Liquidity = Factor("Liquidity", [STOM(), STOQ(), STOA()], [0.35, 0.35, 0.30], disentangle=['Size'])
