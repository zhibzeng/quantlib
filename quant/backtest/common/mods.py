"""回测系统的扩展模块"""
from abc import abstractmethod, ABCMeta
from ...common.logging import Logger

MODS = {}


class AbstractMod(metaclass=ABCMeta):
    """抽象的模块类"""
    @abstractmethod
    def __plug_in__(self, caller):
        """当系统载入模块时会调用该函数，允许它注册事件"""
        pass

    @classmethod
    def register(cls, subclass):
        global MODS
        key = subclass.__name__
        if key in MODS:
            Logger.error("Mod `%s` has already been registered." % key)
        else:
            MODS[key] = subclass
        return subclass
