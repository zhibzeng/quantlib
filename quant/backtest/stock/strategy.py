from abc import abstractmethod, ABCMeta
from ..common.events import EventManager, EventType
from ..common.mods import MODS
from ..common.fund import Fund
from ..common.market import AShareMarket
from ..mods import *
from ...utils.calendar import TradingCalendar


class AbstractStrategy(metaclass=ABCMeta):
    """股票回测策略基类"""
    name = "strategy"
    start_date = None
    end_date = None
    mods = None
    fee_rate = 5e-4
    def __init__(self):
        self.event_manager = EventManager(EventType)
        self.calendar = TradingCalendar()
        self.load_mods()
        self.market = None
        self.fund = None
        self.today = None
        self.today_position = None

    def load_mods(self):
        """加载外部模块"""
        available_mods = type(self).mods
        mods = [MODS[m] for m in available_mods] if available_mods else list(MODS.values())
        self.mods = []
        for mod_cls in mods:
            mod = mod_cls()
            mod.__plug_in__(self)
            self.mods.append(mod)

    def initialize_market_data(self):
        """初始化行情（收益率）数据"""
        self.market = AShareMarket(self)
        self.market.initalize_market(self.start_date, self.end_date)
        self.event_manager.trigger(EventType.INIT_AFTER_LOAD_DATA, self.market)

    def initialize_fund(self):
        """初始化资金帐户"""
        self.fund = Fund(self)
        self.fund.initialize()
        self.event_manager.trigger(EventType.INIT_AFTER_SET_FUND, self.fund)

    def run(self):
        """运行回测过程"""
        self.initialize_market_data()
        self.initialize_fund()
        self.event_manager.trigger(EventType.BACKTEST_START)
        for day in self.market.trading_days:
            self.today = day
            self.market.on_newday(day)
            self.fund.on_newday(day)
            self.today_position = self.fund.position.loc[day].copy()
            self.event_manager.trigger(EventType.BACKTEST_NEWDAY, self.today)
            universe = list(self.market.today_market.dropna().index)
            self.event_manager.trigger(EventType.GET_UNIVERSE, universe)
            self.handle(day, universe)
            self.event_manager.trigger(EventType.BACKTEST_AFTER_HANDLE)
        self.event_manager.trigger(EventType.BACKTEST_FINISH, self.fund)

    @property
    def net_value(self):
        return self.fund.net_value

    def change_position(self, tobuy_pct):
        """更新持仓比例

        Parameters
        ----------
        tobuy_pct: dict
            以股票代码为键，持仓比例为值
        """
        return self.fund.change_position(tobuy_pct)

    @abstractmethod
    def handle(self, today, universe):
        raise NotImplementedError


class SimpleStrategy(AbstractStrategy):
    def __init__(self, predicted, name=None, buy_count=50):
        self.predicted = predicted
        self.name = name
        self.buy_count = buy_count
        self.start_date = predicted.index[0].strftime("%Y-%m-%d")
        self.end_date = predicted.index[-1].strftime("%Y-%m-%d")
        super(SimpleStrategy, self).__init__()

    def handle(self, today, universe):
        try:
            self.predicted.loc[today]
        except KeyError:
            return
        predicted = self.predicted.loc[today, universe].dropna().sort_values(ascending=False)
        buy = predicted.index[:self.buy_count]
        share_per_stock = 1 / len(buy)
        self.change_position({stock: share_per_stock for stock in buy})



