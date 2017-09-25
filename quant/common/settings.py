"""
Global settings about where to store data and configurations.
"""
import os
import re
import warnings
from argparse import ArgumentParser

MAIN_PATH = os.path.abspath(os.path.expanduser("~/.quantlib"))
CONFIG_PATH = os.path.join(MAIN_PATH, "config.cfg")
DATA_PATH = os.path.join(MAIN_PATH, "data")


class ConfigManager:
    """配置项管理，解析配置文件，并允许配置项被命令行参数重写"""
    def __init__(self, path="config.cfg"):
        self.path = path
        self.__keys = set()
        self.parser = ArgumentParser()
        with open(self.path, "r") as config_file:
            self.data = self.__parse_config_file(config_file)
        local_config = os.path.join(os.getcwd(), "config.cfg")
        if path == CONFIG_PATH and os.path.exists(local_config):
            with open(local_config, "r") as config_file:
                self.data = self.__parse_config_file(config_file)

    def __parse_config_file(self, file):
        """
        Read the config file, add the items to argparser so
        that the settings can be overrided by command arguments.
        """
        cfg = {}
        for line in file:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            pair = stripped.split("=")
            if len(pair) != 2:
                raise RuntimeError("Config format error: `%s`" % line)
            key = pair[0].strip()
            value = pair[1].strip()
            help_text = ""
            choices = None
            if "#" in value:
                # Take whatever after `#` as comment. This may cause
                # problems if value string includes `#`
                i = value.index("#")
                help_text = value[i+1:].strip()
                help_text, choices = self.__parse_choices(help_text)
                value = value[:i].strip()
            true_value = None
            for parser in (int, float, self.__boolparser, self.__strparser):
                try:
                    true_value = parser(value)
                except ValueError:
                    pass
                else:
                    break
            if true_value is None:
                raise ValueError("unexpected error in config: `%s`" % line)
            cfg[key.upper()] = {'default': true_value, 'type': type(true_value)}
            self.__keys.add(key.upper())
            self.parser.add_argument("--%s" % key, default=true_value,
                                     type=type(true_value), help=help_text,
                                     choices=choices)
        return cfg

    @classmethod
    def __parse_choices(cls, help_text):
        pattern = r", ?{((?:[^,}]+, ?)+[^,}]+)}$"
        # Warning: this pattern may miss the occasion where
        # `}` appears in the string value
        match = re.search(pattern, help_text)
        if not match:
            choices = None
        else:
            help_text = help_text[:match.start()]
            choices = [cls.__strparser(item.strip()) for item in match.groups()[0].split(",")]
        return help_text, choices

    @staticmethod
    def __strparser(unparsed_value):
        """
        Try to parse the value as str and remove the
        quatation marks beside, if there are any.
        """
        if unparsed_value[0] == unparsed_value[-1] == "'" \
            or unparsed_value[0] == unparsed_value[-1] == "\"":
            return unparsed_value[1: -1]
        return unparsed_value

    @staticmethod
    def __boolparser(unparsed_value):
        """Parse the value as bool"""
        if unparsed_value == "False":
            return False
        elif unparsed_value == "True":
            return True
        else:
            raise ValueError

    def __getattr__(self, item):
        # try:
        #     return object.__getattribute__(self, item)
        # except AttributeError:
        #     pass
        item = item.upper()
        if item not in self.data and item in self.__keys:
            self.update()
        if item not in self.data:
            raise KeyError("Key `%s` not found in config" % item)
        try:
            return self.data[item]['value']
        except KeyError:
            return self.data[item]['default']

    def __setattr__(self, key, value):
        """Allows the value of an item be overrided by program"""
        if key.isupper():
            self.set_value(key, value)
        else:
            object.__setattr__(self, key, value)

    def __contains__(self, item):
        return item in self.__keys

    def get(self, key, default):
        try:
            return getattr(self, key.upper())
        except KeyError:
            return default

    def add_argument(self, *args, **kwargs):
        """除了配置文件已有的参数外，新增命令行参数，与`argparse.ArgumentParser.add_argument`相同"""
        temp_parser = ArgumentParser()
        store_action = temp_parser.add_argument(*args, **kwargs)
        key = store_action.dest.upper()
        if key in self.__keys:
            warnings.warn("Key `%s` already in Config" % key)
            return
        store_action = self.parser.add_argument(*args, **kwargs)
        key = store_action.dest.upper()
        self.__keys.add(key)

    def keys(self):
        """列出所有可用的参数名"""
        return self.__keys

    def items(self):
        """遍历键值对"""
        for key, item in self.data.items():
            try:
                value = item["value"]
            except KeyError:
                value = item["default"]
            yield key, value

    def __set(self, key, value, field):
        try:
            self.data[key][field] = value
        except KeyError:
            self.data[key] = {field: value}
        self.__keys.add(key)

    def set_value(self, key, value):
        """Set the value of a setting item.
        This will overwrite the config file
        and commandline arguments.
        """
        self.__set(key.upper(), value, 'value')

    def set_default(self, key, value):
        """Set the default of a setting item.
        This will overwrite the config file,
        but not the commandline arguments.
        """
        self.__set(key.upper(), value, 'default')

    def get(self, item, default=None):
        # try:
        #     return object.__getattribute__(self, item)
        # except AttributeError:
        #     pass
        item = item.upper()
        if item not in self.data and item in self.__keys:
            self.update()
        if item not in self.data:
            return default
        try:
            return self.data[item]['value']
        except KeyError:
            return self.data[item]['default']

    def update(self):
        """从命令行参数中更新所有配置"""
        args, _ = self.parser.parse_known_args()
        for key, value in args._get_kwargs():
            key = key.upper()
            if key in self.data and "value" in self.data[key]:
                continue
            try:
                self.data[key]['value'] = value
            except KeyError:
                self.data[key] = {'value': value, 'type': type(value)}



def create_default_config():
    """Create default config file"""
    with open(CONFIG_PATH, "w") as config_file:
        default_config = [
            "# Wind",
            "wind_db_driver = 'pymysql'",
            "wind_db_type = 'mysql'",
            "wind_host = 'localhost'",
            "wind_port = 3306",
            "wind_username = 'wind'",
            "wind_password = 'password'",
            "wind_db_name = 'quant'",
            "wind_charset = 'cp936'       # This is for mssql. If you are using mysql, you may want to change it to utf-8 or latin-1",
            "",
            "# logging",
            "log_level = 'INFO'    # Loggin level, {'DEBUG', 'INFO', 'WARNING', 'ERROR', 'FATAL'}",
            "",
            "# backtest",
            "benchmark = '000905.SH'   # Backtest benchmark, default is ZZ500 index",
            "fee_rate = 0.0005",
            "",
        ]
        config_file.write("\n".join(default_config))


def make_default_settings():
    """Create directories for data and configurations"""
    os.mkdir(MAIN_PATH)
    os.mkdir(DATA_PATH)
    create_default_config()


if not os.path.exists(MAIN_PATH):
    make_default_settings()
CONFIG = ConfigManager(os.path.join(MAIN_PATH, "config.cfg"))
