import numpy as np
import pandas as pd
from ...common.localize import LOCALIZER
from ...data import wind
from .base import Descriptor, Factor


@Descriptor.register("B2P")
class B2P(Descriptor):
    """
    Book-to-price ratio

    Last reported book value of common equity divided by current market capitalization.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="b2p")
    def get_raw_value(self):
        return 1 / wind.get_wind_data("AShareEODDerivativeIndicator", "s_val_pb_new")


BookToPrice = Factor("BookToPrice", [B2P()], [1.0])
