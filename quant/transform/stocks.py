import numpy as np
import pandas as pd
from ..data import wind
from ..common.localize import LOCALIZER


def get_rtn(x: pd.Series, rtn_len: int, shift: bool= False):
    """
    对价格序列计算收益率序列

    Parameters
    ----------
    x: pd.Series
        价格序列
    rtn_len: int
        计算收益率的天数
    shift: bool
        如果True，则每天的数据对应当天以后的收益率;
        如果False，则每天的数据对应当天以前的收益率
    """
    # data = (1 + x.pct_change()).rolling(rtn_len).prod() - 1
    data = np.exp(np.log(x).diff().rolling(rtn_len, min_periods=1).sum()) - 1
    if shift:
        data = data.shift(-rtn_len)
    return data
