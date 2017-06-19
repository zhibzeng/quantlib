"""Position optimization"""
import numpy as np
from ..common.settings import CONFIG
import tensorflow as tf


CONFIG.add_argument("--optim_single_limit", type=float, default=0.03)
CONFIG.add_argument("--optim_factor_limit", type=float, default=0.1)


class LimitedOptimizer:
    r"""
        Simple optimizer to optimize position.

    It is to solve the question:

    ..  math::

        max E(R)

        s.t. \qquad & 0 \le x \le optim_single_limit \\
                    & \sum{x} = 1 \\
                    & \lambda F_j \le optim_factor_limit

    in which:

    ..  math::

        E(R) = \sum_i{E(r_i)x_i}

        F_j = \abs{\sum_i{exposure_{ij} x_i} - y_j}

    :math:`y_j` is the expected exposure, which is usually set
    as the exposure of the hedging asset.
    """
    def __init__(self, expected_return):
        """
        Parameters
        ----------
        expected_return: np.ndarray
            :math:`E(r_i)`
        """
        self.expected_return = np.asarray(expected_return)
        self.risks = []

    def add_risk(self, w, y, lamb=1.0):
        r"""
        Add a risk, whose exposure to be minimized.

        Parameters
        ----------
        w: np.ndarray
            the exposure of the stocks
        y: np.ndarray
            target total exposure
        lamb: float, optional
            :math:`\lambda` in the formula
        """
        self.risks.append((w, y, lamb))

    def optimize(self, x0, learning_rate=1e-3):
        """
        Run the optimization and return the result.

        Parameters
        ----------
        x0: np.ndarray
            Initial value of the weights
        learning_rate: float, optional
            learning rate

        Returns
        -------
        np.ndarray, the optimized weights of the stocks
        """
        graph = tf.Graph()
        sess = tf.Session(graph=graph)
        with graph.as_default():
            x = tf.Variable(np.ones_like(self.expected_return) / len(self.expected_return), dtype=tf.float32)
            loss = - tf.reduce_sum(tf.constant(self.expected_return, dtype=tf.float32) * x)
            # for w, y, lamb in self.risks:
            #     risk = tf.reduce_sum(tf.constant(w, dtype=tf.float32) * x) - tf.constant(y, dtype=tf.float32)
            #     loss += tf.cond(risk > 0.1, lambda: risk-0.1, lambda: tf.constant(0, dtype=tf.float32))
            regular = tf.abs(x) + (tf.reduce_sum(x) - 1) ** 2 + tf.abs(x-1)
            loss += regular
            trainer = tf.train.GradientDescentOptimizer(1e-6)
            train_op = trainer.minimize(loss)
            sess.run(tf.global_variables_initializer())
            for i in range(1000):
                sess.run(train_op)
            x = sess.run(x)
            print(x)
            return x


class SimpleOptimizer:
    r"""
    Simple optimizer to optimize position.

    It is to solve the question:

    ..  math::

        max E(R)-\sum_j{\lambda F_j}

        s.t. \qquad & 0 \le x \le 1 \\
                    & \sum{x} = 1

    in which:

    ..  math::

        E(R) = \sum_i{E(r_i)x_i}

        F_j = (\sum_i{exposure_{ij} x_i} - y_j)^2

    :math:`y_j` is the expected exposure, which is usually set
    as the exposure of the hedging asset.
    """
    def __init__(self, expected_return):
        """
        Parameters
        ----------
        expected_return: np.ndarray
            :math:`E(r_i)`
        """
        self.expected_return = np.asarray(expected_return)
        self.risks = []

    def add_risk(self, w, y, lamb=1.0):
        r"""
        Add a risk, whose exposure to be minimized.

        Parameters
        ----------
        w: np.ndarray
            the exposure of the stocks
        y: np.ndarray
            target total exposure
        lamb: float, optional
            :math:`\lambda` in the formula
        """
        self.risks.append((w, y, lamb))

    def _objective_function(self, x):
        objective = - self.expected_return @ x
        jaccobi = - self.expected_return
        for w, y, lamb in self.risks:
            objective += (w @ x - y) ** 2 * lamb
            jaccobi += 2 * lamb * (w @ x - y) * w
        jaccobi += 2 * (x.sum() - 1) * np.ones_like(x)      # To force x.sum() to 1.0
        return objective, jaccobi

    def optimize(self, x0, learning_rate=1e-4):
        """
        Run the optimization and return the result.

        Parameters
        ----------
        x0: np.ndarray
            Initial value of the weights
        learning_rate: float, optional
            learning rate

        Returns
        -------
        np.ndarray, the optimized weights of the stocks
        """
        direction = np.ones_like(x0) / len(x0)

        best_objective = np.inf
        x = np.array(x0) / sum(x0)
        steps_no_better = 0
        while 1:
            objective, gradient = self._objective_function(x)
            if objective < best_objective - 1e-6:
                best_objective = objective
                steps_no_better = 0
            else:
                steps_no_better += 1
                if steps_no_better > 5:
                    break
            x -= gradient * learning_rate
            x[x < 0] = 0
            x[x > 0.2] = 0.2
            valid_grad = np.array((x < 0.2) & (x > 0), dtype=np.float)
            d = (x.sum() - 1) / valid_grad.sum()
            x -= d * valid_grad
            # assert abs(x.sum() - 1)<1e-5, x.sum()
            # if x.sum() != 0:
            #     x /= x.sum()
        # print(max(x))
        return x

