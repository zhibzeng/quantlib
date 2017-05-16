"""用来本地化数据的模块"""
import os
import pickle
import functools
from inspect import signature, isclass, isfunction
import pandas as pd
from .settings import DATA_PATH, MAIN_PATH


class Register:
    """
    用来记录有哪些数据被本地化以及本地化时调用的函数、使用的参数，以便于日后的跟踪维护
    """
    def __init__(self, path="register.pkl"):
        self.log_path = os.path.join(MAIN_PATH, path)
        try:
            with open(self.log_path, "rb") as file_handler:
                self.data = pickle.load(file_handler)
        except FileNotFoundError:
            self.data = dict()

    def keys(self):
        """List the keys of the register"""
        return self.data.keys()

    def __getitem__(self, item):
        return self.data[item]

    def register(self, func, path, args, kwargs, time=None, exclude=None):
        """
        记录本地化数据的来源（函数、参数）以及目标（文件名、键名），便于日后更新

        Parameters
        ----------
        func
            注册的函数
        path: str
        本地化的文件路径
        args: tuple
            调用函数的无关键字参数
        kwargs: dict
            调用函数的关键字参数
        time: str, optional
            无用
        exclude: list, optional
            指定哪些参数名不会被加入到本地化键名中
        """
        exclude = exclude or []
        sig = signature(func)
        bounded = sig.bind(*args, **kwargs)
        bounded.apply_defaults()
        keys = [""]
        for pname, value in bounded.arguments.items():
            if pname in exclude:
                pass
            elif isinstance(value, str):
                keys.append(value)
            elif isclass(value) or isfunction(value):
                keys.append(value.__name__)
        key = "_".join(keys)  # 将函数的所有字符串参数连接起来作为hdf的key
        module = func.__module__
        func_name = func.__name__
        meta_key = "%s/%s/%s" % (module, func_name, key)
        if meta_key not in self.data:
            self.data[meta_key] = {
                "module": module,
                "name": func_name,
                "key": key,
                "params": bounded,
                "path": path,
                "time": time,
                "exclude": exclude,
            }
            self.save()
        return key

    def save(self):
        """Save the register data to pickle file"""
        with open(self.log_path, "wb") as file_handler:
            pickle.dump(self.data, file_handler)


class LocalizeWrapper:
    """
    这是一个装饰器，使用@localizer.wrap(filename)来装饰一个函数，该函数应该返回pandas对象。
    则每次调用函数时会优先调用pd.read_hdf(filename, key)，key是函数的字符串参数的拼接，从本地读取缓存，
    如果读取失败才调用原函数，并将返回值储存在对应的文件内。
    """

    def __init__(self, path):
        self.path = path

    def wrap(self, filename=None, time=None, exclude=None):
        """
        装饰器，被装饰过的函数都会自动本地化

        Parameters
        ----------
        filename: str, optional
            数据要保存的h5文件名
        time: str, optional
            对应于数据时间的参数名，便于日后更新数据
        exclude: list, optional
                哪些参数不需要记录到键名中

        Examples
        --------
        ..  code-block:: python

            @LOCALIZER.wrap("data")
            def get_data(code):
                    ...
        会自动把函数的返回值以`code`为键本地化到`data.h5`中
        """
        def true_wrapper(wrapped):
            nonlocal filename
            filename = filename or wrapped.__name__
            if not filename.endswith("h5"):
                filename = filename + ".h5"
            path = os.path.join(self.path, filename)  # 将指定的文件名或函数名作为文件名

            @functools.wraps(wrapped)
            def func(*args, **kwargs):
                """装饰后的函数"""
                key = REGISTER.register(wrapped, path, args, kwargs, time=time, exclude=exclude)
                # 从注册器注册该函数及参数，并获得对应的键名
                try:
                    data = pd.read_hdf(path, key)
                except (FileNotFoundError, KeyError):
                    data = wrapped(*args, **kwargs)
                    data.to_hdf(path, key)
                return data

            return func

        return true_wrapper



LOCALIZER = LocalizeWrapper(DATA_PATH)
REGISTER = Register()
