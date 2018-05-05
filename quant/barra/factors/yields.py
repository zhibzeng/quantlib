import numpy as np
import pandas as pd
import xarray as xr
from tqdm import tqdm
import statsmodels.api as sm
from ...data import wind
from ...common.localize import LOCALIZER
from ...common.logging import Logger
from ...transform import get_rtn
from .base import Factor, Descriptor
from .industry import INDUSTRY_FACTORS


def get_industry_weights(size, industries):
    common_index = sorted(set(size.index) & set(industries.stock.data))
    size = size[common_index]
    industries = industries.sel(stock=common_index)
    weight = {}
    for industry in industries.factor.data:
        weight[industry] = size[industries.sel(factor=industry).fillna(0).to_pandas().astype(bool)].sum()
    weight = pd.Series(weight) / sum(weight.values())
    return weight


@LOCALIZER.wrap("factor_yields.h5", const_key="yields")
def get_factor_yields():
    Logger.info("Generating factor yields")
    size = wind.get_wind_data("AShareEODDerivativeIndicator", "s_val_mv")

    yields = wind.get_wind_data("AShareEODPrices", "s_dq_adjclose").pct_change()
    yields = yields.clip(yields.mean(1)-yields.std(1)*3, yields.mean(1)+yields.std(1)*3, axis=0)
    yields = xr.DataArray(
        np.expand_dims(yields.values, 2),
        dims=['date', 'stock', 'factor'],
        coords={
            'date': list(yields.index),
            'stock': list(yields.columns),
            'factor': ['yields']
        }
    )

    factors = []
    for name, factor in Factor.get_factors().items():
        factor = factor.get_exposures(fillna=False).shift(1)
        factor = xr.DataArray(
            np.expand_dims(factor.values, 2),
            dims=['date', 'stock', 'factor'],
            coords={
                'date': list(factor.index),
                'stock': list(factor.columns),
                'factor': [name]
            }
        )
        factors.append(factor)
    factors = xr.concat(factors, 'factor')

    industry_factors = [f for f in factors.factor.data if f.startswith("Industry")]

    data = xr.concat([factors, yields], 'factor').sel(date=slice("2005-01-01", None))
    yields_data = {}
    for date in tqdm(data.date.data):
        row = data.sel(date=date).dropna('factor', how='all').dropna('stock').transpose("stock", "factor")
        try:
            x = row.sel(factor=sorted(f for f in row.factor.data if f != "yields"))
            w = size.loc[date, row.stock.data] ** 0.5
            y = row.sel(factor="yields")
            valid = (x.isnull().sum('factor') < len(x.factor.data) / 2) & (~y.isnull())
            x = x.fillna(0.0).values[valid, :]
            y = y.values[valid]
            w = w.values[valid]
        except KeyError:
            continue
        model = sm.WLS(y, x, weights=w, missing='drop').fit()
        beta = pd.Series(model.params, index=sorted(f for f in row.factor.data if f != "yields"))
        
        # Extract yield of country factor from industry factors
        industry_weights = get_industry_weights(size.loc[date], factors.sel(factor=industry_factors, date=date))
        cne_yield = (industry_weights * beta[industry_factors]).sum()
        beta[industry_factors] -= cne_yield

        yields_data[date] = beta
    yields_data = pd.DataFrame(yields_data).T
    return yields_data



