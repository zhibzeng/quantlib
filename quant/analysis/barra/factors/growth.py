import numpy as np
import pandas as pd
from ....common.localize import LOCALIZER
from ....data import wind
from .base import Descriptor, Factor


@Descriptor.register("EGRLF")
class EGRLF(Descriptor):
    """
    Long-term predicted earnings growth

    Long-term (3-5 years) earnings growth forecasted by analysts.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="egrlf")
    def get_raw_value(self):
        forecast_eps = wind.get_consensus_data('eps_avg', 3)
        current_eps = wind.get_wind_data("AShareFinancialIndicator", "s_fa_eps_basic", index="ann_dt").ffill()
        return forecast_eps / current_eps - 1


@Descriptor.register("EGRSF")
class EGRSF(Descriptor):
    """
    Short-term predicted earnings growth

    Short-term (1 year) earnings growth forecasted by analysts.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="egrsf")
    def get_raw_value(self):
        forecast_eps = wind.get_consensus_data('eps_avg', 1)
        current_eps = wind.get_wind_data("AShareFinancialIndicator", "s_fa_eps_basic", index="ann_dt").ffill()
        return forecast_eps / current_eps - 1


@Descriptor.register("EGRO")
class EGRO(Descriptor):
    """
    Earnings growth (trailing five years)

    Annual reported earnings per share are regressed against time over the past 
    five fiscal years. The slope coefficient is then divided by the average 
    annual earnings per share to obtain the earnings growth.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="egrsf")
    def get_raw_value(self):
        forecast_eps = wind.get_consensus_data('eps_avg', 1)
        current_eps = wind.get_wind_data("AShareFinancialIndicator", "s_fa_eps_basic", index="ann_dt").ffill()
        return forecast_eps / current_eps - 1


Growth = Factor("Growth", [EGRLF(), EGRSF(), EGRO()], [0.18, 0.11, 0.24])
# TODO: SGRO
