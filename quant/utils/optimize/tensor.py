from collections import defaultdict
from typing import Set
import numpy as np
from .graph import get_graph
from .constant import *


class Tensor:
    tensor_type = None
    direct_dependencies = None

    def __init__(self, shape, dtype, dependency=None, graph=None, name=None):
        self.dependency = dependency or set()
        self.direct_dependencies = self.direct_dependencies or set()
        self.shape = tuple(shape)
        self.dtype = dtype
        self.graph = graph or get_graph()
        self.name = self.graph.check_name(self, name)
        self.graph.add_tensor(self)
        self.__cache = False
        self.cached_value = None

    def eval(self, feed_dict=None):
        raise NotImplementedError

    def auto_derivate(self, trainable_variables: set, uplevel=None):
        raise NotImplementedError

    @property
    def cache(self):
        return self.__cache

    @cache.setter
    def cache(self, value: bool):
        self.__cache = value
        self.cached_value = None

    def transpose(self):
        return TransposeOp(self)

    def is_scalar(self) -> bool:
        return len(self.shape) == 0

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return "%s: <%s>" % (self.tensor_type, self.name)

    def __eq__(self, other):
        return type(self) == type(other) \
               and (not isinstance(self, Op) or self.direct_dependencies == other.direct_dependencies)

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if other is Zero:
            return self
        if not isinstance(other, Tensor):
            other = Constant(other)
        return AddOp(self, other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Tensor):
            other = Constant(other)
        return SubOp(self, other)

    def __rsub__(self, other):
        if not isinstance(other, Tensor):
            other = Constant(other)
        return SubOp(other, self)

    def __mul__(self, other):
        if other is Zero:
            return Constant(np.zeros(self.shape, self.dtype))
        elif other is Unit:
            return self
        elif not isinstance(other, Tensor):
            other = Constant(other)
        return MulOp(self, other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __matmul__(self, other):
        if not isinstance(other, Tensor):
            other = Constant(other)
        if len(other.shape) == len(self.shape) == 2 and other.shape[0] == self.shape[1]:
            return MatMulOp(self, other)
        elif len(other.shape) == len(self.shape) == 1 and other.shape[0] == self.shape[0]:
            from .operations import ReduceSumOp
            return ReduceSumOp(MulOp(self, other))

    def __rmatmul__(self, other):
        if not isinstance(other, Tensor):
            other = Constant(other)
        if len(other.shape) == len(self.shape) == 2 and other.shape[1] == self.shape[0]:
            return MatMulOp(other, self)
        elif len(other.shape) == len(self.shape) == 1 and other.shape[0] == self.shape[0]:
            from .operations import ReduceSumOp
            return ReduceSumOp(MulOp(self, other))

    def __pow__(self, power: float, modulo=None):
        return PowerOp(self, power)

    def __abs__(self):
        return AbsOp(self)


class Variable(Tensor):
    def __init__(self, values, dtype=None, trainable: bool=True, name: str=None, **kwargs):
        self.trainable = trainable
        self.values = np.array(values, dtype=dtype)
        self.tensor_type = TYPE_VARIABLE
        name = name or "Variable"
        super(Variable, self).__init__(shape=self.values.shape, dtype=self.values.dtype, dependency=None, name=name, **kwargs)

    def eval(self, feed_dict: dict=None)->np.ndarray:
        if feed_dict and self in feed_dict:
            return feed_dict[self]
        return self.values.copy()

    def auto_derivate(self, trainable_variables: set, uplevel=None)->dict:
        if self in trainable_variables:
            return {self: uplevel}
        return {}

    def assign(self, value):
        value = np.array(value, dtype=self.dtype)
        if not value.shape == self.shape:
            raise TypeError("AssignOp require shape match: `%s` and `%s`" % (self.shape, value.shape))
        self.values = value

    def assign_add(self, delta):
        delta = np.asarray(delta)
        ndim1, ndim2 = len(self.shape), len(delta.shape)
        compatible, need_broadcast = broadcastable(self.shape, delta.shape)
        if not compatible:
            raise TypeError("AssignAdd shape not compatible: `%s` and `%s`" % (self.shape, delta.shape))
        if need_broadcast == 0:
            reduce_dims = tuple(range(ndim2-ndim1))
            delta = delta.sum(axis=reduce_dims)
        self.values += delta


class Constant(Tensor):
    def __init__(self, values, dtype=None, name: str=None, **kwargs):
        self.values = np.array(values, dtype=dtype)
        self.tensor_type = TYPE_CONSTANT
        name = name or "Constant"
        super(Constant, self).__init__(shape=self.values.shape, dtype=self.values.dtype, dependency=None, name=name, **kwargs)

    def eval(self, feed_dict: dict=None)->np.ndarray:
        if feed_dict and self in feed_dict:
            return feed_dict[self]
        return self.values.copy()

    def auto_derivate(self, trainable_variables: set, uplevel=None)->dict:
        return {}

Unit = Constant(1.0)
Zero = Constant(0.0)


class Placeholder(Tensor):
    def __init__(self, shape, dtype=np.float32, name: str=None, **kwargs):
        self.tensor_type = TYPE_PLACEHOLDER
        name = name or "Placeholder"
        super(Placeholder, self).__init__(shape=shape, dtype=dtype, name=name, **kwargs)

    def eval(self, feed_dict: dict=None)->np.ndarray:
        if not feed_dict or self not in feed_dict:
            raise RuntimeError("This operation requires values fed to placeholder %s" % self.name)
        fed_value = np.asarray(feed_dict[self], dtype=self.dtype)
        if not self.compatible_shape(fed_value.shape, self.shape):
            raise TypeError("Placeholder %s is of shape `%s`, but fed value is of shape `%s`" % (self.name, self.shape, fed_value.shape))
        return fed_value

    def auto_derivate(self, trainable_variables: set, uplevel=None):
        return {}

    @staticmethod
    def compatible_shape(shape1, shape2):
        if len(shape1) != len(shape2):
            return False
        zipped = zip(shape1, shape2)
        ok = map(lambda x: (not x[0]) or (not x[1]) or x[0] == x[1], zipped)
        return np.array(list(ok)).all()


def cached(func):
    def eval(self, feed_dict: dict=None):
        if self.cache and self.cached_value is not None:
            return self.cached_value
        value = func(self, feed_dict)
        if self.cache:
            self.cached_value = value
        return value
    return eval


def broadcastable(shape1: tuple, shape2: tuple):
    shape1, shape2 = np.array(shape1), np.array(shape2)
    ndim1, ndim2 = shape1.size, shape2.size
    if ndim1 > ndim2:
        padded_shape2 = np.pad(shape2, ((ndim1 - ndim2, 0),), mode="constant", constant_values=1)
        if (padded_shape2 <= shape1).all():
            return True, 1
        else:
            return False, None
    elif ndim2 > ndim1:
        padded_shape1 = np.pad(shape1, ((ndim2 - ndim1, 0),), mode="constant", constant_values=1)
        if (padded_shape1 <= shape2).all():
            return True, 0
        else:
            return False, None
    elif (shape1 == shape2).all():
        return True, None
    elif (shape1 >= shape2).all():
        return True, 1
    elif (shape2 >= shape1).all():
        return True, 0
    else:
        return False, None


class Op(Tensor):
    gradients = None

    def __init__(self, *args, **kwargs):
        self.tensor_type = TYPE_OPERATION
        super(Op, self).__init__(dependency=Op.get_dependency(set(self.direct_dependencies)), *args, **kwargs)

    def auto_derivate(self, trainable_variables: set, uplevel=None):
        to_be_trained = self.dependency & trainable_variables
        final_gradients = defaultdict(list)
        gradients = self.get_gradients(uplevel)
        with self.graph.compute_gradients():
            for tensor in gradients:
                this_grad = gradients[tensor]
                grads = tensor.auto_derivate(to_be_trained, uplevel=this_grad)
                for target, grad in grads.items():
                    final_gradients[target].append(grad)
            for k in final_gradients:
                final_gradients[k] = sum(final_gradients[k], Zero)
        return final_gradients

    @staticmethod
    def get_dependency(list_of_tensors: Set[Tensor]) -> set:
        dependency = set()
        for tensor in list_of_tensors:
            if tensor.tensor_type == TYPE_VARIABLE:
                dependency.add(tensor)
            else:
                dependency |= Op.get_dependency(tensor.dependency)
        return dependency

    def get_gradients(self, uplevel=None):
        if uplevel is None:
            uplevel = Constant(np.ones(self.shape, dtype=self.dtype))
        return {k: uplevel*v for k, v in self.gradients.items()}

    def tree(self):
        tree = {}
        for tensor in self.direct_dependencies:
            if isinstance(tensor, (Constant, Variable, Placeholder)):
                tree[tensor] = tensor
            elif isinstance(tensor, Op):
                if tensor.name.startswith("G_"):
                    tree[tensor] = tensor.tree()
                else:
                    tree[tensor] = tensor
        return tree


class AddOp(Op):
    def __init__(self, t1: Tensor, t2: Tensor):
        valid, master = broadcastable(t1.shape, t2.shape)
        if not valid:
            raise TypeError("shape of %s and %s incompatible: `%s` and `%s`" % (t1.name, t2.name, t1.shape, t2.shape))
        self.t1 = t1
        self.t2 = t2
        self.direct_dependencies = [t1, t2]
        self.gradients = {
            t1: Unit,
            t2: Unit,
        }
        shape = t1.shape if master else t2.shape
        super(AddOp, self).__init__(shape=shape, dtype=t1.dtype, name="Add")

    @cached
    def eval(self, feed_dict=None):
        return self.t1.eval(feed_dict) + self.t2.eval(feed_dict)


class SubOp(Op):
    def __init__(self, t1: Tensor, t2: Tensor):
        valid, master = broadcastable(t1.shape, t2.shape)
        if not valid:
            raise TypeError("shape of %s and %s incompatible: `%s` and `%s`" % (t1.name, t2.name, t1.shape, t2.shape))
        self.t1 = t1
        self.t2 = t2
        self.direct_dependencies = [t1, t2]
        self.gradients = {
            t1: Unit,
            t2: Constant(-1.0),
        }
        shape = t1.shape if master else t2.shape
        super(SubOp, self).__init__(shape=shape, dtype=t1.dtype, name="Sub")

    @cached
    def eval(self, feed_dict=None):
        return self.t1.eval(feed_dict) - self.t2.eval(feed_dict)


class MulOp(Op):
    def __init__(self, t1: Tensor, t2: Tensor):
        valid, master = broadcastable(t1.shape, t2.shape)
        if not valid:
            raise TypeError("shape of %s and %s incompatible: `%s` and `%s`" % (t1.name, t2.name, t1.shape, t2.shape))
        self.t1 = t1
        self.t2 = t2
        self.direct_dependencies = [t1, t2]
        self.gradients = {
            t1: t2,
            t2: t1,
        }
        shape = t1.shape if master else t2.shape
        super(MulOp, self).__init__(shape=shape, dtype=t1.dtype, name="Mul")

    @cached
    def eval(self, feed_dict=None):
        return self.t1.eval(feed_dict) * self.t2.eval(feed_dict)


class AbsDerivation(Op):
    def __init__(self, income: Tensor):
        self.income = income
        self.direct_dependencies = {income}
        super(AbsDerivation, self).__init__(shape=income.shape, dtype=income.dtype, name="AbsDerivation")

    @cached
    def eval(self, feed_dict=None):
        down_level = self.income.eval(feed_dict)
        return np.sign(down_level)

    def auto_derivate(self, trainable_variables: set, uplevel=None):
        raise NotImplementedError


class AbsOp(Op):
    def __init__(self, income: Tensor):
        self.income = income
        self.direct_dependencies = [income]
        super(AbsOp, self).__init__(shape=income.shape, dtype=income.dtype, name="Abs")

    @cached
    def eval(self, feed_dict=None):
        down_level = self.income.eval(feed_dict)
        return np.abs(down_level)

    def get_gradients(self, uplevel=None):
        if uplevel is None:
            uplevel = Constant(np.ones(self.shape, dtype=np.float32))
        return {self.income: uplevel * AbsDerivation(self.income)}


class PowerOp(Op):
    def __init__(self, income: Tensor, pow: float):
        self.income = income
        self.power = pow
        self.direct_dependencies = [income]
        super(PowerOp, self).__init__(shape=self.income.shape, dtype=np.float32, name="Power")

    @cached
    def eval(self, feed_dict=None):
        down_level = self.income.eval(feed_dict)
        return down_level ** self.power

    def get_gradients(self, uplevel=None):
        if uplevel is None:
            uplevel = Constant(np.ones(self.shape, dtype=self.dtype))
        return {self.income: uplevel * self.power * self.income ** (self.power - 1)}


class TransposeOp(Op):
    def __init__(self, income: Tensor):
        self.income = income
        if len(income.shape) != 2:
            raise TypeError("Transpose Op only support 2-dimensional tensor, but `%s` is %d-dimensional" % (income.name, len(income.shape)))
        shape = (income.shape[1], income.shape[0])
        self.direct_dependencies = [income]
        super(TransposeOp, self).__init__(shape=shape, dtype=income.dtype, name="Transpose")

    @cached
    def eval(self, feed_dict: dict=None):
        down_level = self.income.eval(feed_dict)
        return down_level.transpose()

    def get_gradients(self, uplevel: Tensor=None):
        if uplevel is None:
            uplevel = Constant(np.ones(self.shape))
        return {self.income: TransposeOp(uplevel)}


class MatMulOp(Op):
    def __init__(self, t1: Tensor, t2: Tensor):
        if len(t2.shape) == len(t1.shape) == 1:
            shape = None
        elif len(t1.shape) == len(t2.shape) == 2 and t2.shape[0] == t1.shape[1]:
            shape = (t1.shape[0], t2.shape[1])
        else:
            raise TypeError("MatMulOp: dimension not compatible. `%s` and `%s`" % (t1.shape, t2.shape))
        self.t1 = t1
        self.t2 = t2
        self.direct_dependencies = [t1, t2]
        super(MatMulOp, self).__init__(shape=shape, dtype=t1.dtype, name="MatMul")

    @cached
    def eval(self, feed_dict=None):
        return self.t1.eval(feed_dict) @ self.t2.eval(feed_dict)

    def get_gradients(self, uplevel=None):
        if uplevel is None:
            uplevel = Constant(np.ones(self.shape, dtype=self.dtype))
        return {
            self.t1: uplevel @ TransposeOp(self.t2),
            self.t2: TransposeOp(self.t1) @ uplevel
        }