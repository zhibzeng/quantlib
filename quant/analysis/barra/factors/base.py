import numpy as np
import pandas as pd
import xarray as xr
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from ..entities.portfolio import get_estimation_universe
from ....common.localize import LOCALIZER
from ....common.logging import Logger
from ....data import wind
from ....transform import compute_zscore


def size_weighted_standardize(data):
    """
    [x - weighted-mean(x)] / std(x)
    """
    weight = get_estimation_universe().weight
    index = sorted(set(weight.index) & set(data.index))
    z = pd.DataFrame({idx: (data.loc[idx] - (data.loc[idx] * weight.loc[idx]).sum()) / data.loc[idx].std() for idx in index}).T.clip(-3, 3)
    return z


class Descriptor:
    def get_raw_value(self) -> pd.DataFrame:
        raise NotImplementedError

    def get_zscore(self) -> pd.DataFrame:
        wrapper = LOCALIZER.wrap(self.name + "_z")
        return wrapper(self._get_zscore)()

    def _get_zscore(self) -> pd.DataFrame:
        stocks = wind.get_stock_basics()
        stocks = stocks.index[stocks.s_info_listdate.notnull()]
        raw = (
            self.get_raw_value()
            .loc["2005-01-01":, stocks]
            .dropna(0, how="all")
            .dropna(1, how="all")
        )
        # Use capital-weighted mean instead of equal-weighted mean
        z = size_weighted_standardize(raw)
        return z

    @classmethod
    def register(cls, name):
        """
        Register a descriptor so that you can access it using `Descriptor.xxx`
        """
        def wrapper(subcls):
            setattr(cls, name, subcls)
            setattr(subcls, 'name', name)
            return subcls
        return wrapper


class Factor:
    def __init__(self, name, descriptors, weights, disentangle=None):
        if hasattr(Factor, name):
            raise AttributeError("Factor {} already exists".format(name))
        setattr(Factor, name, self)
        self.name = name
        self.descriptors = descriptors
        self.weights = weights
        self.disentangle = disentangle
        self.__data = None

    def get_exposures(self, fillna=True) -> pd.DataFrame:
        """
        Returns the each stock's exposure to the factor each day
        """
        if self.__data is None:
            wrapper = LOCALIZER.wrap(filename="factors", const_key=self.name)
            # Since self.name can't be used at method level, we have to do
            # the wrapping inside the method.
            self.__data = wrapper(self._build_data)()
        if fillna:
            wrapper = LOCALIZER.wrap(filename="factors", const_key=self.name + "_fillna")
            return wrapper(self._fillna)(self.__data)
        return self.__data

    @classmethod
    def get_factors(cls) -> dict:
        return {
            key: getattr(cls, key)
            for key in dir(cls)
            if key[0].isupper()
        }

    def _build_data(self):
        """
        1. get descriptors data
        2. get weight
        3. do a tensor-dot-product
        4. fillna with regression of size and industry

        According to Barra handbook, if some of the descriptors of a factor is missing, use
        the non-missing data. And if all the descriptors are missing, use the fillna strategy.
        """
        Logger.info("Generating factor data for {}".format(self.name))
        descriptors = []
        for descriptor in self.descriptors:
            df = descriptor.get_zscore()
            descriptors.append(xr.DataArray(
                np.expand_dims(df.values, 0),
                dims=['descriptor', 'date', 'stock'],
                coords={
                    'descriptor': [descriptor.name],
                    'stock': df.columns.rename('stock'),
                    'date': df.index.rename('date')
                }
            ))
        descriptors = xr.concat(descriptors, 'descriptor')
        weights = xr.DataArray(
            np.array(self.weights),
            dims=['descriptor'],
            coords={
                'descriptor': [descriptor.name for descriptor in self.descriptors],
            }
        )
        values = (
            (descriptors * weights)
            .dropna('stock', how='all')
            .sum('descriptor')
            .transpose("date", "stock")
            .to_pandas()
        )
        if self.disentangle:
            disentangled = {}
            exog = [getattr(Factor, f).get_exposures() for f in self.disentangle]
            for idx, row in values.iterrows():
                x = [df.loc[idx] for df in exog]
                x.append(row.rename('target'))
                df = pd.concat(x, 1).dropna(subset=['target']).fillna(0)
                if not len(df):
                    continue
                series = LinearRegression().fit(df.values[:, :-1], df.values[:, -1]).predict(df.values[:, :-1])
                disentangled[idx] = df.loc[:, 'target'] - pd.Series(series, index=df.index)
            values = pd.DataFrame(disentangled).T
        values = size_weighted_standardize(values)
        return values

    def _fillna(self, values):
        cap = wind.get_wind_data("AShareEODDerivativeIndicator", "s_val_mv")
        size = Descriptor.LnCap().get_zscore()
        industry = wind.get_stock_industries("AShareIndustriesClassCITICS")
        common_columns = sorted(set(industry.columns) & set(values.columns) & set(size.columns))
        industry = industry[common_columns]
        values = values[common_columns]
        data = {}
        for idx in sorted(set(size.index) & set(industry.index) & set(values.index)):
            s = size.loc[idx, common_columns]
            industry_dummies = pd.get_dummies(industry.loc[idx])
            try:
                y = values.loc[idx]
            except KeyError:
                raise KeyError("{}@{}".format(self.name, idx))
            x = pd.concat([s.rename('size'), industry_dummies, y], 1).dropna(subset=['size']+list(industry_dummies.columns))
            y = x.iloc[:, -1]
            x = x.iloc[:, :-1]
            yhat = sm.WLS(y, x, weights=cap.loc[idx, x.index]**0.5).fit().fittedvalues
            data[idx] = yhat
        data = pd.DataFrame(data).T
        values.update(data, overwrite=False)
        values.index.name = "date"
        values.columns.name = "stock"
        return values
