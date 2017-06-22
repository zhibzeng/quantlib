from abc import abstractmethod
import numpy as np


class Tensor:
    def __init__(self, shape, dtype=None):
        self.__shape = tuple(shape)
        self.__dtype = dtype

    @property
    def shape(self):
        return self.__shape

    @property
    def dtype(self):
        return self.__dtype

    @abstractmethod
    def eval(self, feed_dict):
        pass

    @abstractmethod
    def compute_gradients(self, uplevel=None):
        pass

    def __add__(self, other):
        pass

    def __div__(self, other):
        pass

    def __matmul__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __sub__(self, other):
        pass


class Symbol(Tensor):
    def __init__(self, name, shape=None, dtype=None):
        self.name = name
        dtype = dtype or np.float32
        shape = shape or tuple()
        super(Symbol, self).__init__(shape, dtype)

    def __str__(self):
        return 'Symbol<`%s` %s>' % (
            self.name,
            'x'.join(map(str, self.shape))
        )

    def eval(self, feed_dict=None):
        feed_dict = feed_dict or dict()
        if self in feed_dict:
            return feed_dict[self]
        else:
            raise KeyError("Symbol evaluation without feed_dict")


class Variable(Tensor):
    def __init__(self, values, dtype=None, trainable=True):
        self.__values = np.array(values, dtype=dtype)
        self.trainable = trainable
        dtype = dtype or np.float32
        shape = self.values.shape
        super(Variable, self).__init__(shape, dtype)

    def __str__(self):
        return 'Variable<%s>' % str(self.values)

    def eval(self, feed_dict=None):
        feed_dict = feed_dict or dict()
        if self in feed_dict:
            return feed_dict[self]
        else:
            return self.values

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, new_values):
        self.__values = new_values


class Constant(Tensor):
    def __init__(self, values, dtype=None):
        self.__values = np.array(values, dtype=dtype)
        dtype = dtype or np.float32
        shape = self.values.shape
        super(Constant, self).__init__(shape, dtype)

    def __str__(self):
        return 'Constant<%s>' % str(self.values)

    def eval(self, feed_dict=None):
        feed_dict = feed_dict or dict()
        if self in feed_dict:
            return feed_dict[self]
        else:
            return self.values

    @property
    def values(self):
        return self.__values


class Op(Tensor):
    pass


class AddOp(Op):
    def __init__(self, t1, t2):
        pass


def check_compatible(wrapped):
    def func(self, t1, t2):
        valid, main = broadcastable(t1.shape, t2.shape)
        if not valid:
            raise ValueError("AddOp shape not compatible %s and %s" % (t1.shape, t2.shape))


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
    elif (shape1 >=shape2).all():
        return True, 1
    elif (shape2 >=shape1).all():
        return True, 0
    else:
        return False, None
