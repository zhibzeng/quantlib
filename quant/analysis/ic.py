"""IC correlation score"""
import numpy as np


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
