import os
import importlib.util
import glob
import json
from collections import defaultdict
import fire
import numpy as np
import pandas as pd
from .data import wind
from .common.settings import CONFIG, DATA_PATH, MAIN_PATH
from .common.logging import Logger


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
    def reset_config():
        """Rewrite config file with default settings"""
        from .common.settings import create_default_config
        create_default_config()

    @staticmethod
    def data(command, *args):
        """Manage cache data"""
        command = command.lower()
        assert command in ("ls", "rm"), "Command must be one of {`ls`, `rm`}"
        if command == "ls":
            for filename in glob.glob(os.path.join(DATA_PATH, "*.h5")):
                print(filename.replace("\\", "/").split("/")[-1][:-3])
        elif command == "rm":
            try:
                f = args[0]
            except IndexError:
                raise ValueError("must specify the filename to remove.")
            if not f.endswith(".h5"):
                f += ".h5"
            filename = os.path.join(DATA_PATH, f)
            os.remove(filename)

    @staticmethod
    def table(command, *args):
        """Manage cache data
        command must be one of ("ls", "rm", "update")
        """
        command = command.lower()
        assert command in ("ls", "rm", "update"), "Command must be one of {`ls`, `rm`, `update`}"
        tree = defaultdict(list)
        if command == "ls":
            with pd.HDFStore(os.path.join(DATA_PATH, "wind.h5")) as h5:
                for key in h5.keys():
                    table, field = key[1:].split("/")
                    tree[table].append(field)
            for key, value in tree.items():
                last_update = wind._get_last_update(key)
                print(key, str(last_update))
                for field in value:
                    print("\t", field)
            print("\n\rTotal %d tables, %d fields" % (len(tree), sum(map(len, tree.values()))))

        elif command == "rm":
            try:
                key = args[0]
                if not key.startswith("/"):
                    key = "/" + key
            except IndexError:
                raise ValueError("must specify the key to remove.")
            deleted = False
            with pd.HDFStore(os.path.join(DATA_PATH, "wind.h5")) as h5:
                for k in h5.keys():
                    if k.startswith(key):
                        del h5[k]
                        Logger.info("Deleted %s" % k)
                        deleted = True
            if not deleted:
                Logger.warn("There's no key named `{key}`".format(key=key))

        elif command == "update":
            QuantMain.__update_wind_tables(*args)

    @staticmethod
    def __update_wind_tables(table=None):
        """Delete all cache data"""
        filename = os.path.join(DATA_PATH, "wind.h5")
        if table is None:
            with pd.HDFStore(filename, "r") as h5:
                tables = set(key[1:].split("/")[0] for key in h5.keys())
        else:
            tables = [table]
        for table in tables:
            wind._update_wind_table(table)

    @staticmethod
    def backtest(strategy_filename, key, freq=1):
        key = str(key)
        predicted = pd.read_hdf(strategy_filename, key)
        predicted.index = pd.to_datetime(predicted.index)
        from .utils.calendar import TDay
        dates = pd.date_range(start=predicted.index[0], end=predicted.index[-1], freq=freq*TDay)
        predicted = predicted.loc[dates]
        # import ipdb; ipdb.set_trace()
        final_day = pd.DataFrame(np.zeros([1, predicted.shape[1]]), columns=predicted.columns, index=[predicted.index[-1] + freq*TDay])
        predicted = pd.concat([predicted, final_day])

        config_path = os.path.join(MAIN_PATH, "constraint.json")
        config = json.load(open(config_path))
        from .backtest import ConstraintStrategy
        strategy = ConstraintStrategy(config, predicted, name=key.replace("/", "_"))
        strategy.run()


if __name__ == "__main__":
    fire.Fire(QuantMain)
