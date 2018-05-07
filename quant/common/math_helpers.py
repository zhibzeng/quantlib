import numpy as np
import pandas as pd
import pandas.tseries.offsets
from ..data import wind

__all__ = ['cal_mdd', 'get_ic', 'get_factor_exposure']


def cal_mdd(netvalue, compound=True):
    r"""
    计算最大回撤

    Parameters
    ----------
    netvalue: pd.Series
        净值序列
    compound: bool, optional
        是否为复利制，如果为真，回撤计算方法为 :math:`\frac{N_j}{N_i}-1` (j > i);
        如果为假，回撤计算方法为 :math:`N_j-N_i` (j > i)

    Returns
    -------
    最大回撤值(正值)
    """
    cm = netvalue.cummax()
    if compound:
        dd = netvalue / cm - 1
    else:
        dd = netvalue - cm
    mdd = (-dd).max()
    return mdd


def get_ic(table1, table2, method="spearman"):
    """
    求两组数据之间的IC score

    Parameters
    ----------
    table1, table2: pd.DataFrame
        要计算IC的两个数据框
    method: {'spearman', 'pearson', 'kendall'}
        * pearson : standard correlation coefficient
        * kendall : Kendall Tau correlation coefficient
        * spearman : Spearman rank correlation

    Returns
    -------
    pd.Series
        每期的相关系数，求平均可得IC分数。

    See Also
    --------
    pd.Series.corr
    """
    common_index = sorted(set(table1.index) & set(table2.index))
    ic = pd.Series(np.empty(len(common_index)), index=common_index)
    for date_idx in common_index:
        rk1 = table1.loc[date_idx]
        rk2 = table2.loc[date_idx]
        corr = rk1.corr(rk2, method=method)
        ic[date_idx] = corr
    return ic.dropna()


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
    common_index = set(position.index) & set(factor_value.index)
    for date in sorted(common_index):
        absolute_exposure = ((position.loc[date] * factor_value.loc[date]).sum() / (position.loc[date].sum() + 1e-5))
        if benchmark:
            # 计算当前的基准因子暴露          
            benchmark_exposure = (weights.loc[date] * factor_value.loc[date]).sum() / (weights.loc[date].sum() + 1e-5)
            # 相对暴露等于组合暴露减基准暴露
            relative_exposure = absolute_exposure - benchmark_exposure
            data.loc[date] = relative_exposure
        else:
            data.loc[date] = absolute_exposure
    return data


def exponential_decay_weight(halflife, truncate_length, reverse=True):
    lamb = 0.5 ** (1 / halflife)
    weights = lamb ** np.arange(truncate_length)
    weights /= weights.sum()
    if reverse:
        weights = np.array(list(reversed(weights)))
    return weights



class Rolling:
    def __init__(self, data, period, min_periods=None):
        self.data = data
        self.period = period
        self.min_periods = period if min_periods is None else min_periods
    
    def mean(self):
        return self.data.rolling(self.period, min_periods=self.min_periods).mean()

    def std(self):
        return self.data.rolling(self.period, min_periods=self.min_periods).std()

    def sum(self):
        return self.data.rolling(self.period, min_periods=self.min_periods).sum()

    def max(self):
        return self.data.rolling(self.period, min_periods=self.min_periods).max()

    def min(self):
        return self.data.rolling(self.period, min_periods=self.min_periods).min()

    def apply(self, func):
        result = {}
        for i in range(self.period, len(self.data)):
            idx = self.data.index[i]
            sub_data = self.data.iloc[i-self.period:i].dropna(1, thresh=self.min_periods)
            result[idx] = sub_data.apply(func, raw=False, reduce=True)
        return pd.DataFrame(result).T


