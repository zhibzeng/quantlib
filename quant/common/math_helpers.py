import numpy as np


def exponential_decay_weight(halflife, truncate_length, reverse=True):
    lamb = 0.5 ** (1 / halflife)
    weights = lamb ** np.arange(truncate_length)
    weights /= weights.sum()
    if reverse:
        weights = np.array(list(reversed(weights)))
    return weights
