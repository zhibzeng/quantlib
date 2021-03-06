"""股票类回测策略"""
from abc import abstractmethod
import os
import json
from datetime import date
from scipy.optimize import linprog
import numpy as np
import pandas as pd
from tqdm import tqdm
from .common.events import EventManager, EventType
from .common.mods import ModManager
from .common.fund import Fund
from .common.market import AShareMarket
from ..common.settings import CONFIG, MAIN_PATH
from ..common.logging import Logger
from ..data import wind
from ..barra import Factor
from ..barra.factors.industry import INDUSTRY_FACTORS
from ..utils.calendar import TradingCalendar, TDay


class AbstractStrategy:
    """股票回测策略基类"""
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
        self.mods = self.mods or ModManager()
        self.mods.plug_in(self)

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
        self._load_mods()
        self._initialize_market_data()
        self._initialize_fund()
        self.event_manager.trigger(EventType.BACKTEST_START)
        for day in tqdm(self.market.trading_days):
            self.today = day
            self.market.on_newday(day)
            self.fund.on_newday(day)
            self.today_position = self.fund.position.loc[day].copy()
            self.event_manager.trigger(EventType.BACKTEST_NEWDAY, self.today)
            universe = set(self.market.today_market.dropna().index)
            self.event_manager.trigger(EventType.GET_UNIVERSE, universe)
            self.handle(day, list(universe))
            self.event_manager.trigger(EventType.BACKTEST_AFTER_HANDLE)
        self.event_manager.trigger(EventType.BACKTEST_FINISH, self.fund)
        return self

    @property
    def net_value(self):
        """净值序列， pd.Series"""
        return self.fund.net_value

    def change_position(self, tobuy_pct: dict):
        """更新持仓比例

        Parameters
        ----------
        tobuy_pct: dict
            以股票代码为键，持仓比例为值
        """
        self.event_manager.trigger(EventType.CHANGE_POSITION, tobuy_pct.copy())
        return self.fund.change_position(tobuy_pct)

    @abstractmethod
    def handle(self, today, universe):
        """每日调仓函数，用户逻辑，需重载"""
        raise NotImplementedError


class SimpleStrategy(AbstractStrategy):
    """简单的回测，只需要输入一个预测收益率的DataFrame，
    每期自动等权做多预测最高的`buy_count`只股票"""
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
        mods: ModManager
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
        share_per_stock = 1 / (len(buy) + 1e-6)
        self.change_position({stock: share_per_stock for stock in buy})


class ConstraintStrategy(SimpleStrategy):
    """
    中性策略，在SimpleStrategy的基础上控制行业和因子暴露
    # TODO: cost in objective
    """
    def __init__(self, *args, constraint_config=None, **kwargs):
        """
        """
        if constraint_config is None:
            config_path = os.path.join(MAIN_PATH, "constraint.json")
            constraint_config = json.load(open(config_path))
        self.constraint_config = constraint_config
        self.factor_data = {
            factor_name: getattr(Factor, factor_name).get_exposures(True)
            for factor_name in constraint_config['factors'].keys()
        }
        self.industry_data = {
            industry_name: industry_factor.get_exposures()
            for industry_name, industry_factor in INDUSTRY_FACTORS.items()
        }
        self.index_weights = wind.get_index_weight("AIndexHS300FreeWeight", CONFIG.BENCHMARK) \
                            .resample("1d").ffill()
        rest_index = pd.date_range(self.index_weights.index[-1], pd.to_datetime(date.today()), freq=TDay)
        rest_df = pd.DataFrame(np.full((len(rest_index)-1, len(self.index_weights.columns)), None), index=rest_index[1:], columns=self.index_weights.columns)
        self.index_weights = pd.concat([self.index_weights, rest_df], 0).ffill()

        try:
            import mosek
        except ImportError:
            Logger.debug("Mosek not installed, use scipy to construct portfolio, which may be much slower")
            self.optimize = self.optimize_with_scipy
        else:
            Logger.debug("Use Mosek to construct portfolio")
            self.optimize = self.optimize_with_mosek

        super(ConstraintStrategy, self).__init__(*args, **kwargs)

    def handle(self, today, universe):
        try:
            self.predicted.loc[today]
        except KeyError:
            return
        predicted = self.predicted.loc[today, universe].dropna()
        weights = self.optimize(predicted, today)
        weights = weights[weights > 0].sort_values(ascending=False)
        weights /= weights.sum()
        self.change_position(dict(weights.iteritems()))

    def optimize_with_scipy(self, predicted, today):
        """
        Solve the optimization problem to maximize profits and minimize risks.
        Note this method does not support short selling (negative weight).

        Parameters
        ----------
        predicted: pd.Series
            每只股票当期的预期收益率
        today: str
            日期, %Y-%m-%d

        Returns
        -------
        weights: pd.Series
            每只股票要买入的百分比
        """
        index_weight = self.index_weights.loc[today].fillna(0)
        index_weight = index_weight / index_weight.sum()
        stocks = list(predicted.index)

        kwargs = {}
        kwargs['method'] = 'interior-point'   # 内点法比单纯形法快
        kwargs['c'] = - predicted.values
        kwargs["A_eq"] = np.ones_like(predicted.values).reshape(1, -1)       # \Sum{x} == 1
        kwargs["b_eq"] = np.ones((1, 1), dtype="float32")
        A_ub = []
        b_ub = []

        for factor_name, epsilon in self.constraint_config['factors'].items():
            factor_data = self.factor_data[factor_name].loc[today]
            factor_data.fillna(np.nanmean(factor_data.values), inplace=True)
            index_exposure = (index_weight * factor_data).sum()
            stocks_exposure = factor_data.loc[stocks].values
            
            A_ub.append(stocks_exposure)
            b_ub.append(index_exposure + epsilon)

            A_ub.append(-stocks_exposure)
            b_ub.append(epsilon - index_exposure)

        for industry_name, epsilon in self.constraint_config['industries'].items():
            industry_data = self.industry_data[industry_name].loc[today].fillna(0)
            index_exposure = (index_weight * industry_data).sum()
            stocks_exposure = industry_data.loc[stocks].values
            
            A_ub.append(stocks_exposure)
            b_ub.append(index_exposure + epsilon)

            A_ub.append(-stocks_exposure)
            b_ub.append(epsilon - index_exposure)

        kwargs["A_ub"] = np.stack(A_ub)
        kwargs["b_ub"] = np.stack(b_ub)

        kwargs["bounds"] = [(0, self.constraint_config['stocks'])] * len(stocks)

        result = linprog(**kwargs)

        if not result.success:
            Logger.warn("Optimization Problem: %s" % result.message)

        x = result.x
        weights = pd.Series(x, index=stocks)
        # assert (weights >= 0).all()
        return weights[weights > 0]

    def optimize_with_mosek(self, predicted, today):
        """
        使用Mosek来优化构建组合。在测试中Mosek比scipy的单纯形法快约18倍，如果可能请尽量使用Mosek。
        但是Mosek是一个商业软件，因此你需要一份授权。如果没有授权的话请使用scipy或optlang。
        """
        from mosek.fusion import Expr, Model, ObjectiveSense, Domain, SolutionError
        index_weight = self.index_weights.loc[today].fillna(0)
        index_weight = index_weight / index_weight.sum()
        stocks = list(predicted.index)

        with Model("portfolio") as M:
            x = M.variable("x", len(stocks), Domain.inRange(0, self.constraint_config['stocks']))

            # 权重总和等于一
            M.constraint("sum", Expr.sum(x), Domain.equalsTo(1.0))

            # 控制风格暴露
            for factor_name, limit in self.constraint_config['factors'].items():
                factor_data = self.factor_data[factor_name].loc[today]
                factor_data = factor_data.fillna(factor_data.mean())
                index_exposure = (index_weight * factor_data).sum()
                stocks_exposure = factor_data.loc[stocks].values
                M.constraint(factor_name, Expr.dot(stocks_exposure.tolist(), x), Domain.inRange(index_exposure-limit, index_exposure+limit))

            # 控制行业暴露
            for industry_name, limit in self.constraint_config['industries'].items():
                industry_data = self.industry_data[industry_name].loc[today].fillna(0)
                index_exposure = (index_weight * industry_data).sum()
                stocks_exposure = industry_data.loc[stocks].values
                M.constraint(industry_name, Expr.dot(stocks_exposure.tolist(), x), Domain.inRange(index_exposure-limit, index_exposure+limit))

            # 最大化期望收益率
            M.objective("MaxRtn", ObjectiveSense.Maximize, Expr.dot(predicted.tolist(), x))
            M.solve()
            weights = pd.Series(list(x.level()), index=stocks)
            # try:
            #     weights = pd.Series(list(x.level()), index=stocks)
            # except SolutionError:
            #     raise RuntimeError("Mosek fail to find a feasible solution @ {}".format(str(today)))
        return weights[weights > 0]

    def optimize_with_optlang(self, predicted, today):
        """
        Optlang是一个支持很多后端优化器的接口，包括scipy。
        
        Warnings
        ========
        这个方法的性能和正确性没有测试！
        """
        # TODO: implement this algorithm and test for performance.
        import optlang as opt
        from operator import mul
        from itertools import starmap
        def dot(a, b):
            "Dot product"
            return sum(starmap(mul, zip(a, b)))
        index_weight = self.index_weights.loc[today].fillna(0)
        index_weight = index_weight / index_weight.sum()
        stocks = list(predicted.index)
        model = opt.Model(name="portfolio")
        x = [opt.Variable(stock, lb=0, ub=self.constraint_config['stocks']) for stock in stocks]
        constraints = [opt.Constraint(sum(x), lb=1.0, ub=1.0)]
        for factor_name, limit in self.constraint_config['factors'].items():
            factor_data = self.factor_data[factor_name].loc[today]
            factor_data.fillna(np.nanmean(factor_data.values), inplace=True)
            index_exposure = (index_weight * factor_data).sum()
            stocks_exposure = factor_data.loc[stocks].values
            constraints.append(opt.Constraint(dot(x, stocks_exposure), lb=index_exposure-limit, ub=index_exposure+limit))
        for industry_name, limit in self.constraint_config['industries'].items():
            industry_data = self.industry_data[industry_name].loc[today].fillna(0)
            index_exposure = (index_weight * industry_data).sum()
            stocks_exposure = industry_data.loc[stocks].values
            constraints.append(opt.Constraint(dot(x, stocks_exposure), lb=index_exposure-limit, ub=index_exposure+limit))
        model.objective = opt.Objective(dot(x, predicted), direction='max')
        model.add(constraints)
        model.optimize()
        index, x = zip(model.variables.items())
        weights = pd.Series(x, index=index)
        return weights[weights > 0]

