import numpy as np
import pandas as pd
import xarray as xr
from ....data import wind
from .base import Descriptor, Factor


def _build_industry_factors():
    industry_codes = {
        "汽车": "Automobile",
        "轻工制造": "LightIndustry",
        "医药": "Medical",
        "基础化工": "FundamentalChemistry",
        "传媒": "Media",
        "建材": "BuildingMaterials",
        "电力设备": "ElectricDevice",
        "建筑": "Construction",
        "电子元器件": "ElectronicComponents",
        "房地产": "RealEstate",
        "食品饮料": "Food",
        "商贸零售": "Retail",
        "石油石化": "Petroleum",
        "综合": "Composite",
        "计算机": "Computer",
        "通信": "Communication",
        "机械": "Mechanism",
        "钢铁": "Iron",
        "非银行金融": "NonbankFinance",
        "交通运输": "Transportation",
        "电力及公用事业": "Public",
        "农林牧渔": "Agriculture",
        "国防军工": "Military",
        "家电": "ElectricalAppliance",
        "纺织服装": "Clothing",
        "有色金属": "NonferrousMetal",
        "银行": "Bank",
        "餐饮旅游": "Tourism",
        "煤炭": "Coal",
    }
    industries = wind.get_stock_industries("AShareIndustriesClassCITICS", 1)
    factors = {}
    for ind_name, ind_key in industry_codes.items():
        key = "Industry" + ind_key
        data = (industries == ind_name).astype("float64")
        factors[ind_key] = IndustryFactor(key, data)
    return factors


class IndustryFactor(Factor):
    def __init__(self, name, data):
        setattr(Factor, name, self)
        self.name = name
        self.data = data
    
    def get_exposures(self, fillna=None) -> pd.DataFrame:
        return self.data


INDUSTRY_FACTORS = _build_industry_factors()
