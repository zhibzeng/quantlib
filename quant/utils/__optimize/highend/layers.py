from ..tensor import Variable, Tensor
from ..initialization import Initializer, XavierInitializer, ZeroInitializer
import numpy as np


def fully_connected(income: Tensor,
                    out_depth: int,
                    activation=None,
                    weight_initializer: Initializer=None,
                    bias_initialzier: Initializer=None):
    if len(income.shape) != 2:
        raise TypeError("FullyConnection input must be 2-dimensional, but instead %s is %d-dimensional" % (income.name, len(income.shape)))
    in_depth = income.shape[1]
    shape = (in_depth, out_depth)
    weight_initializer = weight_initializer or XavierInitializer()
    bias_initialzier = bias_initialzier or ZeroInitializer()
    weight = Variable(weight_initializer.generate(*shape), name="weight")
    bias = Variable(bias_initialzier.generate(out_depth), name="bias")
    output = income @ weight + bias
    if activation:
        output = activation(output)
    output.W = weight
    output.b = bias
    return output
