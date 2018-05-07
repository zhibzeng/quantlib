import os
from inspect import signature
from functools import wraps
import pandas as pd
from tables.exceptions import HDF5ExtError
from ..common.settings import DATA_PATH
from ..common.logging import Logger


class Localizer:
    """
    把DataFrame缓存到本地hdf5文件中。通过设置key和const_key参数，可以设定需要跟踪哪些参数。

    Examples
    ========

    无参数

    ..  code-block::
        python

        localilzer = Localizer('./.cache')
        @localizer.wrap('foo', const_key="foo")
        def foo():
            return pd.DataFrame([[1,2,3], [3,4,5]])

    由于hdf5文件需要key来定位数据，因此，对于没有参数的函数，需要给装饰器提供const_key参数方便保存

    跟踪参数

    ..  code-block::
        python

        localilzer = Localizer('./.cache')
        @localizer.wrap('zeros', keys=["length"])
        def zeros(length):
            return pd.DataFrame(np.random.zeros(length, length))

    通过设置keys=["length"]，缓存器可以根据传入的参数不同区分缓存内容。
    
    """
    def __init__(self, path):
        """
        Parameters
        ==========
        path: str
            要缓存到的路径（文件夹）
        """
        self.path = path

    def wrap(self, filename, keys=None, const_key=None, format="fixed"):
        """
        装饰器，用来装饰要缓存结果的函数

        Parameters
        ==========
        filename: str
            缓存到的文件名（无需后缀名）
        keys: List[str]
            需要跟踪的参数名
        const_key: str
            基础键名
        format: {'fixed', 'table'}
            详见pd.DataFrame.to_hdf

        ::

            See :func:`pd.DataFrame.to_hdf`
        """
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
                path = "/".join(str(bounded.arguments[key]) for key in keys) if keys is not None else ""
                if const_key:
                    path = os.path.join(path, const_key)
                if not path:
                    path = "data"
                try:
                    data = pd.read_hdf(filename, path)
                except (KeyError, FileNotFoundError):
                    data = wrapped(*args, **kwargs)
                    try:
                        data.to_hdf(filename, path, format=format)
                    except HDF5ExtError as e:
                        Logger.error("Can't write to HDF5. {}".format(e))
                return data
            return func
        return true_wrapper

LOCALIZER = Localizer(DATA_PATH)
