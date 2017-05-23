"""quant.analysis"""
import numpy as np
import pandas as pd
import pandas.tseries.offsets
from ..data import wind


def get_ic(table1, table2):
    """
    求两组数据之间的IC score

    Parameters
    ----------
    table1, table2: pd.DataFrame
        要计算IC的两个数据框

    Returns
    -------
    float
        IC值
    """
    common_index = sorted(set(table1.index) & set(table2.index))
    ic = []
    for date_idx in common_index:
        rk1 = table1.loc[date_idx]
        rk2 = table2.loc[date_idx]
        corr = rk1.corr(rk2, method="spearman")
        ic.append(corr)
    return np.mean(ic)


def get_factor_exposure(position, factor_value, benchmark=None):
    """计算持仓的因子暴露

    Parameters
    ----------
    position: pd.DataFrame
        每期的持仓
    factor_value: pd.DataFrame
        每期的因子值
    benchmark: str
        要减去的指数的暴露，为None则不减
    """
    data = pd.Series(np.empty(position.shape[0]), index=position.index)
    if benchmark:
        weights = wind.get_index_weight("AIndexHS300FreeWeight", benchmark)
    for date in position.index:
        if benchmark:
            offset_days = -date.day              # 计算当前的基准因子暴露
            while 1:
                try:
                    offset = pd.tseries.offsets.DateOffset(months=1, days=offset_days)
                    weight = weights.loc[date + offset] / 100
                    break
                except KeyError:
                    offset_days -= 1
        absolute_exposure = ((position.loc[date] * factor_value.loc[date]).sum()
                             / position.loc[date].sum())
        if benchmark:
            benchmark_exposure = (weight * factor_value.loc[date]).sum()
            relative_exposure = absolute_exposure - benchmark_exposure
            data.loc[date] = relative_exposure
        else:
            data.loc[date] = absolute_exposure
