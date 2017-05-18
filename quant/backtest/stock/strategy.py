from abc import abstractmethod, ABCMeta
from ..common.events import EventManager, EventType
from ..common.mods import MODS
from ..common.fund import Fund
from ..common.market import AShareMarket
from ...data import wind
from ...utils.calendar import TradingCalendar


class AbstractStrategy(metaclass=ABCMeta):
    """策略基类"""
    start_date = None
    end_date = None
    mods = None
    fee_rate = 5e-4
    def __init__(self):
        self.event_manager = EventManager(EventType)
        self.calendar = TradingCalendar()
        self.load_mods()
        self.market = None
        self.market_data = None
        self.fund = None
        self.today = None

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
        self.initialize_market_data()
        self.initialize_fund()
        self.event_manager.trigger(EventType.BACKTEST_START)
        for day in self.market.trading_days:
            self.today = day
            self.event_manager.trigger(EventType.BACKTEST_NEWDAY, self.today)
            universe = self.market.today_market.index
            self.event_manager.trigger(EventType.GET_UNIVERSE, universe)
            self.handle(day, universe)
            self.event_manager.trigger(EventType.BACKTEST_AFTER_HANDLE)
        self.event_manager.trigger(EventType.BACKTEST_FINISH, self)

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

