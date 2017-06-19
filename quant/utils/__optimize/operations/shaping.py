from faketf.tensor import Op, Tensor, cached, Unit, Constant
import numpy as np


def handle_axis(income: Tensor, axis):
    if axis is None:
        return tuple(range(len(income.shape)))
    if isinstance(axis, int):
        axis = [axis]
    ndim = len(income.shape)
    for i in range(len(axis)):
        if axis[i] < 0:
            axis[i] += ndim
    return tuple(axis)


class ReverseReduceOp(Op):
    def __init__(self, income: Tensor, origin):
        # if t1.shape != t2.shape:
        #     raise TypeError("shape of %s and %s incompatible: `%s` and `%s`" % (t1.name, t2.name, t1.shape, t2.shape))
        self.income = income
        self.origin = origin
        axis = origin.axis
        original_shape = origin.income.shape
        if isinstance(axis, int):
            axis = [axis]
        elif not isinstance(axis, list):
            axis = list(axis)
        self.axis = axis
        self.expand_dims = {ax: original_shape[ax] for ax in axis}
        self.direct_dependencies = [income]
        super(ReverseReduceOp, self).__init__(shape=original_shape, dtype=income.dtype, name="ReverseReduce")

    def get_gradients(self, uplevel=None):
        raise NotImplementedError

    @cached
    def eval(self, feed_dict=None):
        down_level = self.income.eval(feed_dict)
        up_level = self.origin.income.eval(feed_dict)
        expand_dims = {ax: up_level.shape[ax] for ax in self.axis}
        for ax, rep in expand_dims.items():
            down_level = np.expand_dims(down_level, axis=ax)
            down_level = np.repeat(down_level, rep, axis=ax)
        if isinstance(self.origin, ReduceMeanOp):
            down_level /= np.array([rep for rep in expand_dims.values()]).prod()
        return down_level


class ReduceSumOp(Op):
    def __init__(self, income: Tensor, axis=None):
        self.income = income
        self.axis = handle_axis(income, axis)
        shape = tuple(self.income.shape[i] for i in range(len(income.shape)) if i not in self.axis)
        self.direct_dependencies = [income]
        super(ReduceSumOp, self).__init__(shape=shape, dtype=income.dtype, name="ReduceSum")

    def get_gradients(self, uplevel=None):
        if uplevel is None:
            uplevel = Constant(np.ones(self.shape))
        return {self.income: ReverseReduceOp(uplevel, self)}

    @cached
    def eval(self, feed_dict=None):
        return self.income.eval(feed_dict).sum(axis=self.axis)


class ReduceMeanOp(Op):
    def __init__(self, income: Tensor, axis=None):
        # if t1.shape != t2.shape:
        #     raise TypeError("shape of %s and %s incompatible: `%s` and `%s`" % (t1.name, t2.name, t1.shape, t2.shape))
        self.income = income
        self.axis = handle_axis(income, axis)
        shape = tuple(self.income.shape[i] for i in range(len(income.shape)) if i not in self.axis)
        self.direct_dependencies = [income]
        super(ReduceMeanOp, self).__init__(shape=shape, dtype=income.dtype, name="ReduceMean")

    def get_gradients(self, uplevel=None):
        if uplevel is None:
            uplevel = Constant(np.ones(self.shape))
        return {self.income: ReverseReduceOp(uplevel, self)}

    @cached
    def eval(self, feed_dict=None):
        return self.income.eval(feed_dict).mean(axis=self.axis)

