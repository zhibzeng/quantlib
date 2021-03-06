"""
与数据分布有关的变换
"""
import numpy as np
import scipy.stats
import pandas as pd


def find_extreme_values(data, distribution="norm", alpha=0.975):
    """
    在给定的分布和alpha水平下，找出离群值

    Parameters
    ----------
    data: array_like
        要处理离群值的数据
    distribution: str
        假定数据的分布，如:
            - ``norm``：正态分布
            - ``expon``：指数分布
            - ``uniform``：均匀分布
    alpha: float
        判断离群值的alpha水平

    Returns
    -------
        pd.Series
            是否为离散值的布尔值序列

    Examples
    --------

    ..  ipython::

        In [1]: import numpy as np

        In [2]: from quant.transform.distribution import find_extreme_values

        In [2]: data = np.array([0.2, 0.02, 0.1, -0.1, 0.2, 0.15, 100])

        In [3]: find_extreme_values(data)
    
    """
    distribution_family = getattr(scipy.stats, distribution)
    dist_parameters = distribution_family.fit(data[np.isfinite(data)])
    distribution = distribution_family(*dist_parameters)
    low, high = distribution.interval(alpha)
    extreme = (data > high) | (data < low)
    return extreme


def __compute_zscore(data: np.ndarray, axis: int = -1, clip: float = 3.0):
    dims = data.ndim
    data[data == np.inf] = np.nan
    data[data == -np.inf] = np.nan
    if axis is None:
        length = 1
    else:
        if axis < 0:
            axis += dims
        length = data.shape[axis]
    for i in range(length):
        _slice = [i if j == axis else slice(None) for j in range(dims)]
        sliced = data.__getitem__(_slice)
        extremes = find_extreme_values(sliced)
        score = (sliced - np.nanmedian(sliced[~extremes])) / np.nanstd(sliced[~extremes])
        score = np.clip(score, -clip, clip)
        epsilon = 1e-4
        total_err = 1.0
        avg = np.nanmean(score[~extremes])
        sd = np.nanstd(score[~extremes])
        z = (score - avg) / sd
        trial = 0
        while total_err > epsilon and trial < 3:
            if (abs(z) >= clip).any():
                z = np.clip(z, -clip, clip)
            avg = np.nanmean(z)
            std = np.nanstd(z)
            total_err = abs(avg) + abs(std - 1)
            z = (z - avg) / std
            trial += 1
        data.__setitem__(_slice, z)
    return data


def compute_zscore(data, axis=-1, clip=3.0, inplace=False):
    """
    计算Z分数（标准化）

    Parameters
    ----------
    data
        要计算的数据
    axis: int
        以哪一维度作为features区分
    clip: float, optional
        clip
    inplace: bool, optional
        在原数据上修改还是返回新的数据

    Examples
    --------

    ..  ipython::

        In [1]: import numpy as np

        In [2]: from quant.transform.distribution import compute_zscore

        In [3]: data = np.array([[0.1, 0.2, 0.3, 0.25], [0.02, 0.14, 0.28, 0.45]])
        
        In [4]: compute_zscore(data, axis=0)

        In [5]: Out[4].std(1)

    """
    if not inplace:
        data = data.copy()
    if isinstance(data, (pd.Series, pd.DataFrame, pd.Panel)):
        __compute_zscore(data.values, axis=axis, clip=clip)
    else:
        __compute_zscore(data, axis=axis, clip=clip)
    return data


###########


def get_residual(y: pd.Series, x: pd.Series, 
                 estimate_start=None, estimate_end=None, remove_alpha=True):
    """
    将y序列对x序列做回归并求残差

    Parameters
    ----------
    y: pd.Series
        因变量
    x: pd.Series
        自变量
    estimate_start: str (YYYY-MM-DD), optional
        参数估计的起始时间
    estimate_end: str (YYYY-MM-DD), optional
        参数估计的结束时间
    remove_alpha: bool, optinal
        是否去除常数项，默认为True
    """
    estimate_x = x.truncate(estimate_start, estimate_end).dropna()
    estimate_y = y.truncate(estimate_start, estimate_end).dropna()
    common_index = sorted(set(estimate_x.index) & set(estimate_y.index))
    estimate_x = estimate_x[common_index]
    estimate_y = estimate_y[common_index]
    estimate_matrix = np.stack([np.ones(len(estimate_x)), estimate_x.values], axis=1)
    beta = ((np.linalg.pinv(estimate_matrix.T @ estimate_matrix) @ estimate_matrix.T) @ estimate_y.values).reshape(-1)
    if remove_alpha:
        matrix = np.stack([np.ones(len(x)), x.values])
    else:
        matrix = np.stack([np.zeros(len(x)), x.values])
    return y - matrix @ beta




