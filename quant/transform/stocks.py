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


@LOCALIZER.wrap("filter_st", const_key="filter_st")
def get_st_filter():
    st = wind.get_wind_table("AShareST")
    st["entry_dt"] = pd.to_datetime(st.entry_dt)
    st["remove_dt"] = pd.to_datetime(st.remove_dt)
    return st


def remove_st(data):
    """把ST的股票去除
    Parameters
    ----------
    data: pd.DataFrame / pd.Panel
        要处理的数据框，至少是二维的，第一维为事件，第二维为股票
    Returns
    -------
    pandas结构，和输入的data同一形状、类型，将ST股票的记录置为NaN
    """
    # TODO
    pass

