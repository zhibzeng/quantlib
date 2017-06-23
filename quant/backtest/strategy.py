"""股票类回测策略"""
from abc import abstractmethod
from scipy.optimize import linprog
import numpy as np
import pandas as pd
from progressbar import Bar, ProgressBar, ETA, Percentage
from .common.events import EventManager, EventType
from .common.mods import MODS
from .common.fund import Fund
from .common.market import AShareMarket
from ..common.settings import CONFIG
from ..common.logging import Logger
from ..data.wind import get_index_weight
from ..utils.calendar import TradingCalendar, TDay
# from ..utils.optimize import Variable, Constant, reduce_sum
# from ..utils.optimize.tensor import Unit
# from ..utils.optimize.optimizer import Optimizer
# from ..utils.optimize.graph import Graph
# from ..utils.optimize.train import SGD


class AbstractStrategy:
    """股票回测策略基类"""
    # TODO: 个股收益明细
    name = "strategy"
    """策略名称，用于结果输出"""
    start_date = None
    """起始日期 %Y-%m-%d"""
    end_date = None
    """结束日期 %Y-%m-%d"""
    mods = None
    """可用Mod列表"""
    def __init__(self):
        self.event_manager = EventManager(EventType)
        self.calendar = TradingCalendar()
        self.market = None
        self.fund = None
        self.today = None
        self.today_position = None

    def _load_mods(self):
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

    def _initialize_market_data(self):
        """初始化行情（收益率）数据"""
        self.market = AShareMarket(self)
        self.market.initalize_market(self.start_date, self.end_date)
        self.event_manager.trigger(EventType.INIT_AFTER_LOAD_DATA, self.market)

    def _initialize_fund(self):
        """初始化资金帐户"""
        self.fund = Fund(self)
        self.fund.initialize()
        self.event_manager.trigger(EventType.INIT_AFTER_SET_FUND, self.fund)

    def run(self):
        """运行回测过程"""
        self._initialize_market_data()
        self._initialize_fund()
        self._load_mods()
        self.event_manager.trigger(EventType.BACKTEST_START)
        bar = ProgressBar(widgets=[Percentage(), Bar(), ETA()])
        for day in bar(self.market.trading_days):
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
        """每日调仓函数，用户逻辑，需重载"""
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
        self.index_weights = get_index_weight("AIndexHS300FreeWeight", CONFIG.BENCHMARK) \
                            .resample("1d").ffill() / 100
        super(NeutralStrategy, self).__init__(*args, **kwargs)

    def handle(self, today, universe):
        try:
            self.predicted.loc[today]
        except KeyError:
            return
        predicted = self.predicted.loc[today, universe].dropna()
        stocks = predicted.index
        weights = self.optimize(predicted, today).sort_values(ascending=False)
        weights = weights[weights > 0]
        if self.buy_count:
            weights = weights.iloc[:self.buy_count]
            weights /= weights.sum()
        self.change_position(dict(weights.iteritems()))

    def optimize(self, predicted, today):
        """
        Solve the optimization problem to maximize profits and minimize risks.
        Note this method does not support short selling (negative weight).

        Parameters
        ----------
        predicted: pd.Series
            Predicted returns of the stocks at `today`
        today: str
            The date, %Y-%m-%d

        Returns
        -------
        weights: pd.Series
            The percentage of each stock to buy.
        """
        index_weight = self.index_weights.loc[today].fillna(0)
        stocks = list(predicted.index)

        kwargs = {}
        kwargs['c'] = - predicted.values
        kwargs["A_eq"] = np.ones_like(predicted.values).reshape(1, -1)       # \Sum{x} == 1
        kwargs["b_eq"] = np.ones((1, 1), dtype=np.float32)
        A_ub = []
        b_ub = []

        for factor, regularizer_weight in self.neutral_factors.items():
            factor_data = self.factor_data[factor.factor_name].loc[today]
            factor_data.fillna(np.nanmean(factor_data.values), inplace=True)
            index_exposure = (index_weight * factor_data).sum()
            stocks_exposure = factor_data.loc[stocks].values
            import ipdb
            # ipdb.set_trace()
            A_ub.append(stocks_exposure)
            b_ub.append(index_exposure + 0.1)

            A_ub.append(-stocks_exposure)
            b_ub.append(0.1 - index_exposure)

        kwargs["A_ub"] = np.stack(A_ub)
        kwargs["b_ub"] = np.stack(b_ub)

        kwargs["bounds"] = [(0, 0.02)] * len(stocks)

        result = linprog(**kwargs)

        if not result.success:
            Logger.warn("Optimization: %s" % result.message)

        x = result.x
        weights = pd.Series(x, index=stocks)
        return weights[weights > 0]


