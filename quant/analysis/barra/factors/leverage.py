import numpy as np
import pandas as pd
from ....common.localize import LOCALIZER
from ....data import wind
from .base import Descriptor, Factor


@Descriptor.register("LD")
class LD(Descriptor):
    r"""
    Long-term debt

    Computed as
    LD = [long-term borrow] + [bonds payable]
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="ld")
    def get_raw_value(self):
        lb = wind.get_wind_data("AShareBalanceSheet", "lt_borrow", index="ann_dt").ffill()
        bp = wind.get_wind_data("AShareBalanceSheet", "bonds_payable", index="ann_dt").ffill()
        return lb + bp


@Descriptor.register("MLEV")
class MLEV(Descriptor):
    r"""
    Market leverage

    Computed as
    MLEV = (ME + PE + LD) / ME
    where ME is the market value of common equity on the last trading day, 
    PE is the most recent book value of preferred equity, and LD is the 
    most recent book value of long-term debt.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="mlev")
    def get_raw_value(self):
        me = wind.get_wind_data("AShareEODDerivativeIndicator", "s_dq_mv")
        pe = wind.get_wind_data("AShareBalanceSheet", "other_equity_tools_p_shr", index="ann_dt").ffill()
        ld = LD().get_raw_value()
        return 1 + (pe + ld) / me


@Descriptor.register("BLEV")
class BLEV(Descriptor):
    r"""
    Market leverage

    Computed as
    BLEV = (BE + PE + LD) / ME
    where BE is the book value of common equity on the last trading day, 
    PE is the most recent book value of preferred equity, and LD is the 
    most recent book value of long-term debt.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="blev")
    def get_raw_value(self):
        book_equity = wind.get_wind_data("AShareBalanceSheet", "tot_shrhldr_eqy_excl_min_int", index="ann_dt").ffill()
        pe = wind.get_wind_data("AShareBalanceSheet", "other_equity_tools_p_shr", index="ann_dt").ffill()
        ld = LD().get_raw_value()
        return 1 + (pe + ld) / book_equity


@Descriptor.register("DTOA")
class DToA(Descriptor):
    r"""
    Debt-to-assets

    Computed as

    DTOA = \frac{TD}{TA}

    where TD is the book value of total debt (long-term debt and current liabilities), 
    and TA is most recent book value of total assets.
    """
    @LOCALIZER.wrap(filename="descriptors", const_key="dtoa")
    def get_raw_value(self):
        return wind.get_wind_data("AShareFinancialIndicator", "s_fa_debttoassets", index="ann_dt").ffill()


Leverage = Factor("Leverage", [MLEV(), DToA(), BLEV()], [0.38, 0.35, 0.27])
