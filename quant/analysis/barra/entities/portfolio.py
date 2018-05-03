import pandas as pd
from ....data import wind


class Portfolio:
    def __init__(self, weight):
        self.weight = weight
        self._rtn = None

    def get_returns(self):
        if self._rtn is None:
            stocks_rtn = wind.get_wind_data("AShareEODPrices", "s_dq_pctchange").loc["2003-01-01":] / 100
            self._rtn = (stocks_rtn * self.weight).dropna(how="all").sum(1)
        return self._rtn


__estimation_universe = None
def get_estimation_universe():
    global __estimation_universe
    if __estimation_universe is None:
        size = wind.get_wind_data("AShareEODDerivativeIndicator", "s_val_mv")
        weight = pd.DataFrame({idx: row / row.sum() for idx, row in size.iterrows()}).T.dropna(how='all')
        __estimation_universe = Portfolio(weight)
    return __estimation_universe

