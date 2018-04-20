import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from ....common.localize import LOCALIZER
from .base import Descriptor, Factor
from .size import Size


@Descriptor.register("NLSize")
class NLSize(Descriptor):
    """
    Cube of Size

    First, the standardized Size exposure (i.e., log of market cap) is cubed. 
    The resulting factor is then orthogonalized with respect to the Size factor 
    on a regression-weighted basis. Finally, the factor is winsorized and standardized.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="nlsize")
    def get_raw_value(self):
        size = Size.get_exposures()
        cube = size ** 3
        nlsize = {}
        for idx in size.index:
            x = size.loc[idx].dropna()
            if len(x) == 0:
                continue
            stocks = x.index
            x = x.values.reshape(-1, 1)
            y = cube.loc[idx, stocks].values
            yhat = LinearRegression().fit(x, y).predict(x)
            nlsize[idx] = pd.Series(np.clip(y-yhat, -3, 3), index=stocks)
        nlsize = pd.DataFrame(nlsize).T
        return nlsize


NonLinearSize = Factor("NonLinearSize", [NLSize()], [1.0])
