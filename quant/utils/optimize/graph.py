from .constant import TYPE_VARIABLE, TYPE_OPERATION, TYPE_CONSTANT, TYPE_PLACEHOLDER
from contextlib import contextmanager
__graph = None


def get_graph():
    global __graph
    if not __graph:
        __graph = Graph()
    return __graph


class Graph:
    def __init__(self):
        self.tensors = {}
        self.ops = {}
        self.variables = {}
        self.constants = {}
        self.trainable = set()
        self.mute = 0
        self.__cache = 0

    def as_default(self):
        global __graph
        tmp = __graph
        __graph = self
        yield
        __graph = tmp

    @property
    def cache(self):
        return self.__cache

    @cache.setter
    def cache(self, value):
        if self.__cache > 0 and value == 0:
            for tensor in self.tensors.values():
                tensor.cache = False
        elif value > 0 and self.__cache == 0:
            for tensor in self.tensors.values():
                tensor.cache = True
        self.__cache = max(value, 0)

    @contextmanager
    def compute_gradients(self):
        self.mute += 1
        yield
        self.mute -= 1

    @contextmanager
    def enable_cache(self):
        self.cache += 1
        yield
        self.cache -= 1

    def add_tensor(self, tensor):
        if tensor.name in self.tensors:
            raise KeyError("Tensor %s already exists in graph" % tensor.name)
        self.tensors[tensor.name] = tensor
        if tensor.tensor_type == TYPE_OPERATION:
            self.ops[tensor.name] = tensor
        elif tensor.tensor_type == TYPE_VARIABLE:
            self.variables[tensor.name] = tensor
            if tensor.trainable:
                self.trainable.add(tensor)
        elif tensor.tensor_type == TYPE_CONSTANT:
            self.constants[tensor.name] = tensor

    def check_name(self, tensor, name):
        if tensor.tensor_type == TYPE_VARIABLE:
            prefix = "V"
        elif tensor.tensor_type == TYPE_OPERATION:
            prefix = "Op"
        elif tensor.tensor_type == TYPE_CONSTANT:
            prefix = "C"
        elif tensor.tensor_type == TYPE_PLACEHOLDER:
            prefix = "P"
        else:
            prefix = "T"
        if self.mute:
            prefix = "G_" + prefix
        i = 0
        while 1:
            postfix = str(i)
            valid_name = "_".join([prefix, name, postfix])
            if valid_name not in self.tensors:
                return valid_name
            i += 1

    def __eq__(self, other):
        return self is other
