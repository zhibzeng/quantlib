import numpy as np
import pandas as pd
import xarray as xr
from ....common.localize import LOCALIZER
from ....data import wind
from ....transform import compute_zscore


class Descriptor:
    def get_raw_value(self) -> pd.DataFrame:
        raise NotImplementedError

    def get_zscore(self) -> pd.DataFrame:
        stocks = wind.get_stock_basics()
        stocks = stocks.index[stocks.s_info_listdate.notnull()]
        raw = (
            self.get_raw_value()
            .loc["2005-01-01":, stocks]
            .dropna(0, how="all")
            .dropna(1, how="all")
        )
        z = compute_zscore(raw, 0, clip=4.0, inplace=True)
        return z

    @classmethod
    def register(cls, name):
        def wrapper(subcls):
            setattr(cls, name, subcls)
            setattr(subcls, 'name', name)
            return subcls
        return wrapper


class Factor:
    def __init__(self, name, descriptors, weights):
        setattr(Factor, name, self)
        self.name = name
        self.descriptors = descriptors
        self.weights = weights
        self.__data = None

    def get_exposures(self) -> pd.DataFrame:
        if self.__data is None:
            wrapper = LOCALIZER.wrap(filename="factors", const_key=self.name)
            # Since self.name can't be used at method level, we have to do
            # the wrapping inside the method.
            self.__data = wrapper(self._build_data)()
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
        4. fillna with zero
        5. compute z-score
        TODO: fillna with industrial mean

        According to Barra handbook, if some of the descriptors of a factor is missing, use
        the non-missing data. And if all the descriptors are missing, use the fillna strategy.
        """
        if len(self.descriptors) > 1:
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
                .fillna(0)
                .transpose("date", "stock")
                .to_pandas()
            )
            compute_zscore(values, 0, 4.0, True)
        else:
            values = self.descriptors[0].get_zscore()
        return values
    
