"""
Global settings about where to store data and configurations.
"""
import os
from argparse import ArgumentParser

MAIN_PATH = os.path.abspath(os.path.expanduser("~/.quantlib"))
CONFIG_PATH = os.path.join(MAIN_PATH, "config.cfg")
DATA_PATH = os.path.join(MAIN_PATH, "data")


class ConfigManager:
    """配置项管理，解析配置文件，并允许配置项被命令行参数重写"""
    def __init__(self, path="config.cfg"):
        self.path = path
        self.parser = ArgumentParser()
        self.ready = False
        with open(self.path, "r") as config_file:
            self.data = self.__parse_config_file(config_file)

    def __parse_config_file(self, file):
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
            if "#" in value:
                i = value.index("#")
                help_text = value[i+1:].strip()
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
            self.parser.add_argument("--%s" % key, default=true_value,
                                     type=type(true_value), help=help_text)
        return cfg

    @staticmethod
    def __strparser(unparsed_value):
        if unparsed_value[0] == unparsed_value[-1] == "'" \
            or unparsed_value[0] == unparsed_value[-1] == "\"":
            return unparsed_value[1: -1]
        return unparsed_value

    @staticmethod
    def __boolparser(unparsed_value):
        if unparsed_value == "False":
            return False
        elif unparsed_value == "True":
            return True
        else:
            raise ValueError

    def __getattr__(self, item):
        if not self.ready:
            try:
                self.update()
            except:
                pass
        item = item.upper()
        try:
            return self.data[item]['value']
        except KeyError:
            return self.data[item]['default']

    def add_argument(self, *args, **kwargs):
        """除了配置文件已有的参数外，新增命令行参数，与`argparse.ArgumentParser.add_argument`相同"""
        # TODO: 如果新增的参数和配置文件中的重复，可能有冲突
        self.parser.add_argument(*args, **kwargs)

    def keys(self):
        """列出所有可用的参数名"""
        return self.data.keys()

    def items(self):
        """遍历键值对"""
        for key, item in self.data.items():
            try:
                value = item["value"]
            except KeyError:
                value = item["default"]
            yield key, value

    def update(self):
        """从命令行参数中更新所有配置"""
        args = self.parser.parse_args()
        for key, value in args._get_kwargs():
            key = key.upper()
            try:
                self.data[key]['value'] = value
            except KeyError:
                self.data[key] = {'value': value, 'type': type(value)}
        self.ready = True



def create_default_config():
    """Create default config file"""
    with open(CONFIG_PATH, "w") as config_file:
        config_file.writelines([
            "wind_db_driver = 'pymysql'\n",
            "wind_db_type = 'mysql'\n",
            "wind_host = 'localhost'\n",
            "wind_port = 3306\n",
            "wind_username = 'wind'\n",
            "wind_password = 'password'\n",
            "wind_db_name = 'quant'\n",
        ])


def make_default_settings():
    """Create directories for data and configurations"""
    os.mkdir(MAIN_PATH)
    os.mkdir(DATA_PATH)
    create_default_config()


if not os.path.exists(MAIN_PATH):
    make_default_settings()
CONFIG = ConfigManager(os.path.join(MAIN_PATH, "config.cfg"))
