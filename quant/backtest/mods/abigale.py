import json
import pandas as pd
from ...abigale import Abigale, exceptions
from ...common.math_helpers import get_factor_exposure
from ...barra.factors import get_factor_yields
from ...common.settings import CONFIG
from ...common.logging import Logger
from ...data import wind
from ..common.mods import AbstractMod
from ...barra import Factor


@AbstractMod.register
class AbigaleMod(AbstractMod):
    def __init__(self):
        self.weights = {}
        super(AbigaleMod, self).__init__()

    def get_benchmark(self):
        """获取基准标的的净值"""
        benchmark = wind.get_wind_data("AIndexEODPrices", "s_dq_close")[CONFIG.get("BENCHMARK", "000905.SH")] \
            .dropna().truncate(self.strategy.start_date, self.strategy.end_date)
        benchmark /= benchmark.iloc[0]
        return benchmark
    
    def get_exposure(self, position, factor):
        """计算持仓的因子暴露"""
        factor_name = factor.name
        factor_value = factor.get_exposures()
        exposure = (get_factor_exposure(position, factor_value, benchmark=CONFIG.BENCHMARK)
            .resample("1m")
            .mean()
            .rename(factor_name)
        )
        return exposure

    def on_change_position(self, weight):
        self.weights[self.strategy.today] = pd.Series(weight)

    def on_backtest_finish(self, fund):
        weights = pd.DataFrame(self.weights).T
        weights.index = pd.to_datetime(weights.index)
        benchmark = self.get_benchmark()
        relative_net_value = (fund.sheet["net_value"] / benchmark).dropna().rename("netValue")
        data = {
            "strategyName": self.strategy.name,
            "basic": self.generate_basic_info(relative_net_value, weights),
            "netValues": self.generate_net_values(relative_net_value),
            "styleRisks": self.generate_style_risks(weights),
            "industryRisks": self.generate_industry_risks(weights),
            "factorYields": self.generate_factor_exposure_yields()
        }
        with open(f'{self.strategy.name}.json', 'w') as f:
            json.dump(data, f)
        Logger.info(f"回测结果输出到{self.strategy.name}.json")

    def generate_basic_info(self, net_values, weights):
        """
        生成基本信息，包括：每年的平均收益率、波动率、夏普率、换手率、回撤
        """
        years = sorted(net_values.index.year.unique())
        data = []
        for year in years:
            idx = net_values.index[net_values.index.year == year]
            nv = net_values.loc[idx]
            idx = weights.index[weights.index.year == year]
            w = weights.loc[idx]
            data.append(self._basic_info_item(str(year), nv, w))
        data.append(self._basic_info_item("Total", net_values, weights))
        return data

    def generate_net_values(self, net_values):
        """
        生成净值序列
        """
        return self._series_to_list(net_values)

    def generate_factor_exposure_yields(self):
        """
        因子归因
        """
        position = self.strategy.fund.position.apply(lambda x: x / x.sum(), axis=1)
        factor_yields = get_factor_yields()
        factor_exposure_yields = {}

        # calculate factor yields one by one
        for factor in factor_yields.columns:
            factor_value = getattr(Factor, factor).get_exposures()
            exposure = get_factor_exposure(position, factor_value, benchmark=CONFIG.BENCHMARK)
            yields = exposure * factor_yields[factor]
            factor_exposure_yields[factor] = yields.dropna()
        
        # Sum all industry yields
        industry_exposure_yields = sum(value for key, value in factor_exposure_yields.items() if key.startswith("Industry"))
        for key in list(factor_exposure_yields.keys()):
            if key.startswith("Industry"):
                del factor_exposure_yields[key]
        factor_exposure_yields['Industry'] = industry_exposure_yields
        
        # relative_rtn = self.strategy.fund.sheet["net_value"].pct_change() - self.get_benchmark().pct_change()
        # risk_yields = pd.DataFrame(factor_exposure_yields).sum(1)
        # factor_exposure_yields['Alpha'] = (relative_rtn - risk_yields).dropna()

        return {
            key: self._series_to_list(series.cumsum())
            for key, series in factor_exposure_yields.items()
        }
        

    def generate_style_risks(self, weights):
        """
        风格暴露
        """
        style_risks = {}
        for factor in Factor.get_factors().values():
            if factor.name.startswith("Industry"):
                continue
            series = self.get_exposure(weights, factor)
            style_risks[factor.name] = self._series_to_list(series)
        return style_risks

    def generate_industry_risks(self, weights):
        """
        行业暴露
        """
        industry_risks = {}
        for factor in Factor.get_factors().values():
            if not factor.name.startswith("Industry"):
                continue
            series = self.get_exposure(weights, factor)
            industry_risks[factor.name[8:]] = self._series_to_list(series)
        return industry_risks

    @staticmethod
    def _series_to_list(series):
        """
        把DatetimeIndex的Series转换成Highstocks的序列格式
        """
        return [
            [int(idx.timestamp() * 1000), value]
            for idx, value in series.iteritems()
        ]

    @staticmethod
    def _basic_info_item(name, nv, weights):
        """
        基本统计信息
        """
        rtns = nv.pct_change()
        rtn = rtns.mean() * 252
        std = rtns.std() * 252 ** 0.5
        sharpe = rtn / std
        mdd = (1 - nv / nv.cummax() ).max()
        turnover = weights.fillna(0).diff().abs().sum(1).sum() / (weights.index[-1] - weights.index[0]).days * 252
        return {
            'period': name,
            'rtn': f'{rtn*100:0.2f}%',
            'volatility': f'{std*100:0.2f}%',
            'sharpe': f'{sharpe:0.2f}',
            'mdd': f'{mdd*100:0.1f}%',
            'turnover': f'{turnover*100:0.1f}%'
        }