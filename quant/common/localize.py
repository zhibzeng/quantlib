import os
from inspect import signature
from functools import wraps
import pandas as pd
from ..common.settings import DATA_PATH


class Localizer:
    def __init__(self, path):
        self.path = path

    def wrap(self, filename, keys=None, const_key=None, format="fixed"):
        if keys is None and const_key is None:
            raise ValueError("Either `keys` or `const_key` must not be None")
        filename = os.path.join(self.path, filename)
        if not filename.endswith(".h5"):
            filename += ".h5"
        if keys is None:
            keys = []
        if isinstance(keys, str):
            keys = [keys]
        def true_wrapper(wrapped):
            @wraps(wrapped)
            def func(*args, **kwargs):
                sig = signature(wrapped)
                bounded = sig.bind(*args, **kwargs)
                bounded.apply_defaults()
                path = "/".join(bounded.arguments[key] for key in keys) if keys is not None else ""
                if const_key:
                    path = os.path.join(path, const_key)
                if not path:
                    path = "data"
                try:
                    data = pd.read_hdf(filename, path)
                except (KeyError, FileNotFoundError):
                    data = wrapped(*args, **kwargs)
                    data.to_hdf(filename, path, format=format)
                return data
            return func
        return true_wrapper

LOCALIZER = Localizer(DATA_PATH)
