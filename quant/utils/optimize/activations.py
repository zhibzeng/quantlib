from .tensor import Op, Tensor, cached, Constant
import numpy as np


def relu(income: Tensor)->Tensor:
    return Relu(income)


def sigmoid(income: Tensor)->Tensor:
    return Sigmoid(income)


class Sigmoid(Op):
    def __init__(self, income: Tensor):
        self.income = income
        self.direct_dependencies = [income]
        self.gradients = {income: self * (1 - self)}
        super(Sigmoid, self).__init__(shape=income.shape, dtype=income.dtype, name="Sigmoid")

    @cached
    def eval(self, feed_dict=None):
        income_value = self.income.eval(feed_dict)
        return 1 / 1 + np.exp(-income_value)


class Relu(Op):
    def __init__(self, income: Tensor):
        self.income = income
        self.direct_dependencies = [income]
        super(Relu, self).__init__(shape=income.shape, dtype=income.dtype, name="Relu")

    @cached
    def eval(self, feed_dict=None):
        down_level = self.income.eval(feed_dict).copy()
        return np.maximum(down_level, 0)

    def get_gradients(self, uplevel=None):
        if uplevel is None:
            uplevel = Constant(np.ones(self.shape, self.dtype))
        return ReluDerivation(uplevel)


class ReluDerivation(Op):
    def __init__(self, income: Tensor):
        self.income = income
        self.direct_dependencies = [income]
        super(ReluDerivation, self).__init__(shape=income.shape, dtype=income.dtype, name="ReluDerivation")

    @cached
    def eval(self, feed_dict=None):
        down_level = self.income.eval(feed_dict)
        return np.asarray(down_level > 0, dtype=np.float32)

    def get_gradients(self, uplevel=None):
        raise NotImplementedError
