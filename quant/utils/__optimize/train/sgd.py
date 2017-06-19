from .trainer import Trainer
from ..tensor import Tensor


class SGD(Trainer):
    def __init__(self, target: Tensor, learning_rate: float=0.001, trainable_variables: set=None):
        self.target = target
        self.graph = target.graph
        self.trainable_variables = trainable_variables or self.graph.trainable
        self.learning_rate = learning_rate
        with self.graph.compute_gradients():
            self.gradients = self.target.auto_derivate(self.trainable_variables)

    def train(self, feed_dict: dict=None):
        gradients = {}
        with self.graph.enable_cache():
            for variable, gradient in self.gradients.items():
                gradient_value = gradient.eval(feed_dict)
                gradients[variable] = gradient_value
        for variable, gradient_value in gradients.items():
            variable.assign_add(-gradient_value * self.learning_rate)

