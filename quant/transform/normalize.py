import numpy as np
import scipy.stats
import pandas as pd


def find_extreme_values(data, distribution="norm", alpha=0.975):
    """
    在给定的分布和alpha水平下，找出离群值

    Parameters:
        data (pd.Series):
            要处理离群值的数据
        distribudtion (str):
            假定数据的分布，如:
                ``norm``：正态分布

                ``expon``：指数分布

                ``uniform``：均匀分布

        alpha (float):
            判断离群值的alpha水平
    Returns:
        pd.Series[bool]，每个值是否是离群值
    """
    distribution_family = getattr(scipy.stats, distribution)
    dist_parameters = distribution_family.fit(data)
    distribution = distribution_family(*dist_parameters)
    low, high = distribution.interval(alpha)
    extreme = (data > high) | (data < low)
    return extreme


def __compute_zscore(x: np.ndarray, axis: int = -1, clip: float = 3.0):
    dims = x.ndim
    x[x == np.inf] = np.nan
    x[x == -np.inf] = np.nan
    if axis is None:
        length = 1
    else:
        if axis < 0:
            axis += dims
        length = x.shape[axis]
    for i in range(length):
        _slice = [i if j == axis else slice(None) for j in range(dims)]
        sliced = x.__getitem__(_slice)
        extremes = find_extreme_values(sliced)
        score = (sliced - np.nanmedian(sliced[~extremes])) / np.nanstd(sliced[~extremes])
        score[score > clip] = clip
        score[score < -clip] = -clip
        epsilon = 1e-4
        total_err = 1.0
        avg = np.nanmean(score[~extremes])
        sd = np.nanstd(score[~extremes])
        z = (score - avg) / sd
        while total_err > epsilon:
            if (abs(z) >= clip).any():
                z[abs(z) >= clip] = clip * np.sign(z[abs(z) >= clip])
            avg = np.nanmean(z)
            err = np.nanstd(z)
            total_err = abs(avg) + abs(err - 1)
            z = (z - avg) / err
        x.__setitem__(_slice, z)
    return x


def compute_zscore(x, axis=-1, clip=3.0, inplace=False):
    """
    计算Z分数

    Parameters:
        x:
            要计算的数据
        axis (int):
            以哪一维度作为features区分
        clip (float):
            clip
        inplace (bool):
            在原数据上修改还是返回新的数据
    """
    if not inplace:
        x = x.copy()
    if isinstance(x, (pd.Series, pd.DataFrame, pd.Panel)):
        __compute_zscore(x.values, axis=axis, clip=clip)
    else:
        __compute_zscore(x, axis=axis, clip=clip)
    return x


###########


def get_residual(y: pd.Series, x: pd.Series, estimate_start=None, estimate_end=None, remove_alpha=True):
    """
    将y序列对x序列做回归并求残差

    Parameters:
        y (pd.Series):
            因变量
        x (pd.Series):
            自变量
        estimate_start (str):
            参数估计的起始时间 YYYY-MM-DD
        estimate_end (str):
            参数估计的结束时间 YYYY-MM-DD
        remove_alpha (bool):
            是否去除常数项
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


#########


def get_rtn(x: pd.Series, rtn_len: int, shift: bool= False):
    """
    对价格序列计算收益率序列

    Parameters:
        x (pd.Series):
            价格序列
        rtn_len (int):
            计算收益率的天数
        shift (bool):
            如果True，则每天的数据对应当天以后的收益率;
            如果False，则每天的数据对应当天以前的收益率
    """
    # data = (1 + x.pct_change()).rolling(rtn_len).prod() - 1
    data = np.exp(np.log(x).diff().rolling(rtn_len).sum()) - 1
    if shift:
        data = data.shift(-rtn_len)
    return data


