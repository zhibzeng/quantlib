"""回测系统的扩展模块"""
from abc import abstractmethod, ABCMeta
from typing import Union
from ...common.logging import Logger
from .events import EventType


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


class ModManager:
    __mods = {}

    def __init__(self):
        self.mods = self.__class__.__mods.copy()

    @classmethod
    def register(cls, enabled: Union[type, bool]=True):
        """
        注册一个mod，并指定其默认是否启用

        Examples
        ========

        # 默认启用
        @ModManager.register
        class CustomMod(AbstraceMod):
            pass

        # 指定是否启用
        @ModManager.register(enable=False)
        class CustomMod(AbstraceMod):
            pass
        """
        def _register(enabled):
            def wrapper(mod):
                if not isinstance(mod, type):
                    raise TypeError("Mod must be a class. not a `{}`".format(type(mod)))
                elif not issubclass(mod, AbstractMod):
                    raise TypeError("Mod must be inherited from `quant.backtest.common.mods.AbstractMod`, not `{}`".format(mod.__base__))
                else:
                    cls.__mods[mod] = enable
                return mod
            return wrapper

        if isinstance(enabled, bool):
            return _register(enabled)
        else:
            mod = enabled
            return _register(True)(mod)

    def enable(self, mod):
        """
        启用一个Mod

        Parameters
        ==========
        mod: Union[str, type]
            需要启动的Mod类或其名称
        """
        self.set_ability(mod, True)

    def disable(self, mod):
        """
        禁用一个Mod

        Parameters
        ==========
        mod: Union[str, type]
            需要启动的Mod类或其名称
        """
        self.set_ability(mod, False)

    def set_ability(self, mod, ability):
        if isinstance(mod, str):
            for m in list(self.mods.keys()):
                if m.__name__ == mod:
                    self.mods[m] = ability
        else:
            self.mods[mod] = ability

    def plug_in(self, strategy):
        """
        把所有以启用的Mod绑定到策略上
        """
        for mod in self.available_mods:
            mod = mod()
            mod.__plug_in__(strategy)

    @property
    def available_mods(self):
        return (mod for mod, enabled in self.mods.items() if enabled)
