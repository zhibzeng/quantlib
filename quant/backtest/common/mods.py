"""回测系统的扩展模块"""
from abc import abstractmethod, ABCMeta
from ...common.logging import Logger
from .events import EventType

MODS = {}


class AbstractMod(metaclass=ABCMeta):
    """抽象的模块类"""
    def __init__(self):
        self.strategy = None

    def __plug_in__(self, caller):
        """当系统载入模块时会调用该函数，允许它注册事件"""
        self.strategy = caller
        for event_name in EventType.__members__.keys():
            event = getattr(EventType, event_name)
            func_name = "on_%s" % event_name.lower()
            if hasattr(self, func_name):
                func = getattr(self, func_name)
                caller.event_manager.register(event, func)
                Logger.debug("[Mod] Registered {} => {}".format(self.__class__.__name__, event_name))

    @classmethod
    def register(cls, subclass):
        global MODS
        key = subclass.__name__
        if key in MODS:
            Logger.error("Mod `%s` has already been registered." % key)
        else:
            MODS[key] = subclass
        return subclass

    def __call__(self):
        return self

    def unregister(self, subclass):
        global MODS
        if isinstance(subclass, AbstractMod) or isinstance(subclass, type):
            key = subclass.__name__
        elif isinstance(subclass, str):
            key = subclass
        else:
            raise TypeError("Can't identify mod as `%s` type" % str(type(subclass)))
        try:
            del MODS[key]
        except KeyError:
            Logger.error("Found No Mod Named `%s`." % key)

