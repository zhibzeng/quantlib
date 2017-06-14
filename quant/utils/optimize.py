"""Position optimization"""
import numpy as np

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

