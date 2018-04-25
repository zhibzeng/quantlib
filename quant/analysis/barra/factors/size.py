import numpy as np
from ....data import wind
from ....common.localize import LOCALIZER
from .base import Descriptor, Factor


@Descriptor.register("LnCap")
class LnCap(Descriptor):
    @LOCALIZER.wrap(filename="descriptors", const_key="LnCap")
    def get_raw_value(self):
        return np.log(wind.get_wind_data("AShareEODDerivativeIndicator", "s_dq_mv"))


Size = Factor("Size", [LnCap()], [1.0])