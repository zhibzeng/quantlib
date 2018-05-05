import numpy as np
import pandas as pd
from ...common.localize import LOCALIZER
from ...data import wind, to_trade_data
from .base import Descriptor, Factor


@Descriptor.register("EPFWD")
class EPFWD(Descriptor):
    r"""
    Predicted earnings-to-price ratio

    Given by the 12-month forward-looking earnings divided by the current 
    market capitalization. Forward-looking earnings are defined as a 
    weighted average between the average analyst-predicted earnings for 
    the current and next fiscal years.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="epfwd")
    def get_raw_value(self):
        capitalization = wind.get_wind_data("AShareEODPrices", "s_dq_close")
        earnings = wind.get_consensus_data('eps_avg', 1)
        return earnings / capitalization


@Descriptor.register("CETOP")
class CEToP(Descriptor):
    r"""
    Cash earnings-to-price ratio

    Given by the trailing 12-month cash earnings divided by current price.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="cetop")
    def get_raw_value(self):
        capital = wind.get_wind_data("AShareEODDerivativeIndicator", "s_dq_mv")
        cash_earnings = to_trade_data(wind.get_wind_data("AShareCashFlow", "net_cash_flows_oper_act", index="ann_dt")).dropna(how='all')
        return cash_earnings / capital


@Descriptor.register("ETOP")
class EToP(Descriptor):
    r"""
    Trailing earnings-to-price ratio

    Given by the trailing 12-month earnings divided by the current market capitalization. 
    Trailing earnings are defined as the last reported fiscal-year earnings plus the 
    difference between current interim figure and the comparative interim figure from the 
    previous year.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="etop")
    def get_raw_value(self):
        price = wind.get_wind_data("AShareEODPrices", "s_dq_close")
        eps = to_trade_data(wind.get_wind_data("AShareFinancialIndicator", "s_fa_eps_basic", index="ann_dt"))
        return eps / price

EarningsYield = Factor("EarningsYield", [EPFWD(), CEToP(), EToP()], [0.68, 0.21, 0.11])
