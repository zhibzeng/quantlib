import os
import importlib.util
import glob
import fire
import pandas as pd
from .backtest import SimpleStrategy
from .common.settings import CONFIG


def load_class_from_file(path):
    module_name = os.path.split(path)[-1][:-3]
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    obj_name = "".join(x.capitalize() for x in module_name.split("_"))
    obj = getattr(module, obj_name)
    return obj_name, obj


class QuantMain:
    """Main entry for quantlib"""
    @staticmethod
    def gen_docs(path="."):
        """
        Generate documents for factors defined under a specific path.
        """
        from .analysis.factors import AbstractFactor
        from .common.logging import Logger
        filenames = [path] if path.endswith(".py") else glob.glob(os.path.join(path, "*.py"))
        num = 0
        for filename in filenames:
            if os.path.split(filename)[-1].startswith("__"):
                continue
            obj_name, obj = load_class_from_file(filename)
            if hasattr(obj, "generate_doc"):
                Logger.info("Generating documents for %s ..." % obj_name)
                obj.generate_doc()
                num += 1
        Logger.info("Gen-doc finished. %d documents generated." % num)

    @staticmethod
    def reset_config():
        """Rewrite config file with default settings"""
        from .common.settings import create_default_config
        create_default_config()

    @staticmethod
    def clear_cache(all=False):
        """Delete all cache data"""
        from .common.settings import DATA_PATH
        y_for_all = all
        for filename in glob.glob(os.path.join(DATA_PATH, "*.h5")):
            confirm = (y_for_all
                       or input("Confirm deleting %s? [y/N/a]" % os.path.split(filename)[-1]))
            if confirm == "a":
                y_for_all = True
            if confirm in ("a", "y", True):
                os.remove(filename)

    @staticmethod
    def backtest(strategy_filename, key=None):
        if strategy_filename.endswith(".h5"):
            QuantMain._backtest_simple(strategy_filename, key)
        else:
            if not strategy_filename.endswith(".py"):
                strategy_filename += ".py"
            QuantMain._backtest_strategy(strategy_filename)

    @staticmethod
    def _backtest_strategy(py_file):
        strategy_class = load_class_from_file(py_file)[1]
        strategy_class.run()

    @staticmethod
    def _backtest_simple(h5_file, key):
        predicted = pd.read_hdf(h5_file, key)
        strategy = SimpleStrategy(predicted)
        strategy.run()


if __name__ == "__main__":
    fire.Fire(QuantMain)
