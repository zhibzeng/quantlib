import pandas as pd
from ...abigale import Abigale, exceptions
from ...analysis import get_factor_exposure
from ...common.settings import CONFIG
from ...data import wind
from ..common.mods import AbstractMod


class AbigaleMod(AbstractMod):
    risk_factors = set()
    def __init__(self, workspace, table, override=False, metadata=None):
        """
        Parameters
        ==========
        workspace: str
            workspace to store the result data
        table: str
            table name
        override: bool
            Whether to override if the target place is already occupied, defaults False.
            If this is set to False, raises TableExistsException if occupied
        """
        self.workspace = workspace
        self.table = table
        self.override = override
        self.metadata = metadata or {}
        super(AbigaleMod, self).__init__()

    # def __plug_in__(self, caller):
    #     self.strategy = caller
    #     caller.event_manager.register(EventType.BACKTEST_FINISH, self.on_backtest_finish)

    @classmethod
    def register_factor(cls, factor):
        cls.risk_factors.add(factor)

    def get_benchmark(self):
        """获取基准标的的净值"""
        benchmark = wind.get_wind_data("AIndexEODPrices", "s_dq_close")[CONFIG.get("BENCHMARK", "000905.SH")] \
            .dropna().truncate(self.strategy.start_date, self.strategy.end_date)
        benchmark /= benchmark.iloc[0]
        return benchmark
    
    def get_exposure(self, position, factor):
        """计算持仓的因子暴露"""
        factor_name = factor.factor_name
        factor_value = factor.get_factor_value()
        exposure = get_factor_exposure(position, factor_value, benchmark=CONFIG.BENCHMARK).resample("1m").mean()
        return exposure.rename(factor_name)

    def on_backtest_finish(self, fund):
        benchmark = self.get_benchmark()
        data = [
            (fund.sheet["net_value"] / benchmark).dropna().rename("netValue")
        ]
        for factor in self.risk_factors:
            data.append(self.get_exposure(fund.position, factor))
        abigale = Abigale()
        if not abigale.api.auth:
            if not abigale.login():
                raise exceptions.LoginFailed
        if not self.override and self.table in abigale.ls(abigale.username, self.workspace):
            raise exceptions.TableExistsException
        self.metadata["is_backtest"] = True
        data = pd.concat(data, axis=1)
        abigale.upload(self.workspace, self.table, data, self.metadata)
        

