import numpy as np
from .graph import get_graph
from .tensor import Variable
from .train import SGD
from .operations import reduce_sum


class Optimizer:
    def __init__(self):
        self.graph = get_graph()
        self.vars = {}
        self.eqs = []
        self.ineqs = []
        self.loss = None

    def add_variable(self, name, initial_value, dtype=np.float32):
        variable = Variable(initial_value, name=name, dtype=dtype)
        self.vars[name] = variable
        return variable

    def set_target(self, loss):
        if len(loss.shape) != 0:
            loss = reduce_sum(loss)
        self.loss = loss

    def add_constraint(self, variable, eq=True):
        if eq:
            self.eqs.append(variable)
        else:
            self.ineqs.append(variable)

    def optimize(self):
        loss = self.get_loss()
        trainer = SGD(loss)
        for i in range(1000):
            trainer.train()

    def get_loss(self):
        loss = self.loss
        for constraint in self.eqs:
            constraint = constraint ** 2 * 20
            if len(constraint.shape) != 0:
                constraint = reduce_sum(constraint)
            loss += constraint
        for constraint in self.ineqs:
            constraint = (abs(constraint) - constraint) * 20
            if len(constraint.shape) != 0:
                constraint = reduce_sum(constraint)
            loss += constraint
        return loss

    def __getitem__(self, name):
        if name in self.vars:
            return self.vars[name]
        raise KeyError("No variable named `%s`" % name)

