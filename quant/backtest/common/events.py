""""事件注册、触发等管理"""
from enum import Enum
import bisect


EventType = Enum("EventType", ("INIT_AFTER_LOAD_DATA",
                               "INIT_AFTER_SET_FUND",
                               "BACKTEST_START",
                               "BACKTEST_NEWDAY",
                               "BACKTEST_AFTER_HANDLE",
                               "GET_UNIVERSE",
                               "BACKTEST_FINISH"))


class EventManager:
    """事件管理器"""
    def __init__(self, event_types):
        self.event_types = event_types
        self.hooks = {key: [] for key in event_types}

    def register(self, event_type, callback, index=99):
        """注册事件

        Parameters
        ----------
        event_type
            事件类型
        callbakc
            回调函数

        Raises
        ------
        KeyError
            如果注册的事件类型不在事件管理器支持的类型中则触发异常
        """
        if event_type in self.event_types:
            if callback not in self.hooks[event_type]:
                position = [x[0] for x in self.hooks[event_type]]
                position = bisect.bisect_right(position, index)
                self.hooks[event_type].insert(position, (index, callback))
        else:
            raise KeyError("Event `%s` not recognized" % event_type.name)

    def register_wrap(self, event_type, index=99):
        """自动注册被装饰的函数

        Parameters
        ----------
        event_type
            注册的事件类型
        """
        def wrapper(wrapped):
            self.register(event_type, wrapped, index)
            return wrapped
        return wrapper

    def trigger(self, event_type, *args, **kwargs):
        """触发指定类型的事件"""
        if event_type not in self.event_types:
            raise KeyError("Event `%s` not recognized" % event_type.name)
        for _, func in self.hooks[event_type]:
            func(*args, **kwargs)

