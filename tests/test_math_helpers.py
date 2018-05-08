import unittest
import numpy as np
import pandas as pd
from quant.common.math_helpers import cal_mdd, exponential_decay_weight


class MathTestCase(unittest.TestCase):
    def test_cal_mdd(self):
        series = pd.Series([1.0, 1.1, 1.11, 1.04, 1.02, 1.08])
        mdd = cal_mdd(series)
        true_mdd = 1 - 1.02 / 1.11
        self.assertAlmostEqual(mdd, true_mdd)

    def test_exponential_decay(self):
        weights = exponential_decay_weight(halflife=1, truncate_length=4, reverse=False)
        true_weights = np.array([1, 0.5, 0.25, 0.125])
        true_weights /= true_weights.sum()
        np.testing.assert_array_almost_equal(weights, true_weights)
