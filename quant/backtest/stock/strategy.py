"""股票类回测策略"""
from abc import abstractmethod
import numpy as np
import pandas as pd
from ..common.events import EventManager, EventType
from ..common.mods import MODS
from ..common.fund import Fund
from ..common.market import AShareMarket
from ...data.wind import get_index_weight
from ...utils.calendar import TradingCalendar


class AbstractStrategy:
    """股票回测策略基类"""
    # TODO: 个股收益明细
    # TODO: 风险敞口
    name = "strategy"
    start_date = None
    end_date = None
    mods = None
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
        available_mods = self.mods if self.mods is not None else list(MODS.values())
        self.mods = []
        for mod_cls in available_mods:
            if isinstance(mod_cls, str):
                try:
                    mod_cls = MODS[mod_cls]
                except KeyError:
                    raise KeyError("Mod `%s` not found!" % mod_cls)
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
        """净值序列， pd.Series"""
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
    """简单的回测，只需要输入一个预测收益率的DataFrame，
    每期自动等全做多预测最高的`buy_count`只股票"""
    def __init__(self, predicted, name=None, buy_count=50, mods=None):
        """
        Parameters
        ----------
        predicted: pd.DataFrame
            预测收益率
        name: str
            策略名称，用于显示
        buy_count: int
            每期做多股票数量
        mods: list
            使用的模块列表，None则为全部已注册模块
        """
        self.predicted = predicted
        self.name = name
        self.buy_count = buy_count
        if mods is not None:
            self.mods = mods
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
        share_per_stock = 0.999 / (len(buy) + 1e-6)          # keep 0.001 for transaction fee
        self.change_position({stock: share_per_stock for stock in buy})


class NeutralStrategy(SimpleStrategy):
    """
    中性策略，在SimpleStrategy的基础上对冲一些风险
    """
    def __init__(self, *args, neutral_factors={}, **kwargs):
        self.neutral_factors = neutral_factors
        self.factor_data = {factor.factor_name: factor.get_factor_value()
                            for factor in neutral_factors.keys()}
        self.index_weights = get_index_weight("AIndexHS300FreeWeight", "000905.SH")
        super(NeutralStrategy, self).__init__(*args, **kwargs)

    def handle(self, today, universe):
        import scipy.optimize
        try:
            self.predicted.loc[today]
        except KeyError:
            return
        predicted = self.predicted.loc[today, universe].dropna()
        stocks = predicted.index

        def objective_function(weights):
            index_weight = self.index_weights.loc[today, stocks].fillna(0)
            weights = np.asarray(weights) - index_weight.values
            profits = predicted.values @ weights
            exposion_regularizer = 0
            for factor, regularizer_weight in self.neutral_factors.items():
                factor_data = self.factor_data[factor.factor_name].loc[today, stocks]
                factor_data.fillna(np.nanmean(factor_data.values))
                exposion = factor_data.values @ weights
                exposion_regularizer += regularizer_weight * exposion ** 2
            return -profits + exposion_regularizer

        result = scipy.optimize.minimize(objective_function,
                                         np.zeros(len(stocks), dtype=np.float32),
                                         bounds=[(0, None) for _ in stocks])
        weights = pd.Series(result.x, index=stocks).sort_values(ascending=False)
        buy = weight.index[:self.buy_count]
        share_per_stock = 0.999 / (len(buy) + 1e-6)          # keep 0.001 for transaction fee
        self.change_position({stock: share_per_stock for stock in buy})
        



