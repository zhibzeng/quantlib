from ..tensor import Tensor, Op
from .shaping import ReduceSumOp, ReduceMeanOp


def reduce_sum(income: Tensor, axis=None):
    return ReduceSumOp(income, axis)


def reduce_mean(income: Tensor, axis=None):
    return ReduceMeanOp(income, axis)


