import numpy as np


class Initializer:
    def generate(self, *shape):
        raise NotImplementedError


class NormalInitializer(Initializer):
    def __init__(self, mu=0, sigma=1.0):
        self.mu = mu
        self.sigma = sigma

    def generate(self, *shape):
        return np.random.randn(*shape) * self.sigma + self.mu


class XavierInitializer(NormalInitializer):
    def generate(self, *shape):
        node_in = np.array(shape[:-1]).prod()
        node_out = shape[-1]
        return np.random.rand(*shape) * np.sqrt(2 / (node_in + node_out))


class HeInitializer(NormalInitializer):
    def generate(self, *shape):
        node_in = np.array(shape[:-1]).prod()
        return np.random.rand(*shape) * np.sqrt(2 / node_in)


class ZeroInitializer(Initializer):
    def generate(self, *shape):
        return np.zeros(shape, dtype=np.float32)


class UniformInitializer(Initializer):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def generate(self, *shape):
        return np.random.uniform(self.low, self.high, shape)

