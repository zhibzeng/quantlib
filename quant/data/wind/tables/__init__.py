"""Wind数据库数据表

Tables:
    AIndexEODPrices: A股指数每日收盘行情

    AShareEODDerivativeIndicator: A股股票每日收盘指标

    AShareEODPrices: A股股票每日收盘行情

    AShareIPO: A股股票IPO信息

    AShareST: A股股票ST信息

    AShareTTMHist:
"""

from .a_index_eod_prices import AIndexEODPrices
from .a_share_eod_derivative_indicator import AShareEODDerivativeIndicator
from .a_share_eod_prices import AShareEODPrices
from .a_share_ipo import AShareIPO
from .a_share_st import AShareST
from .a_share_ttm_his import AShareTTMHis


DEFAULT_FIELDS = {
    AIndexEODPrices: {'index': 'trade_dt', 'columns': 's_info_windcode'},
    AShareEODDerivativeIndicator: {'index': 'trade_dt', 'columns': 's_info_windcode'},
    AShareEODPrices: {'index': 'trade_dt', 'columns': 's_info_windcode'},
}
