import numpy as np
from ..tensor import Op, Tensor, cached, Constant


class DropoutOp(Op):
    def __init__(self, income: Tensor, keep_prob: float):
        self.income = income
        self.keep_prob = keep_prob
        self.direct_dependencies = [income]
        self.mask = None
        super(DropoutOp, self).__init__(shape=self.income.shape, dtype=self.income.dtype, name="Dropout")

    @cached
    def eval(self, feed_dict=None):
        down_level = self.income.eval(feed_dict)
        self.mask = np.random.binomial(1, self.keep_prob, self.shape)
        self.gradients = {self.income: Constant(self.mask)}
        return down_level * self.mask
