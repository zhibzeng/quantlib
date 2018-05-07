quant.barra
###########

基类
====

..  currentmodule:: quant.barra.factors

..  autoclass:: Descriptor
    :members: get_raw_value, get_zscore, register

..  autoclass:: Factor
    :members: get_exposures, get_factors

Descriptor
==========

Beta
----

..  class:: quant.barra.factors.beta.BetaDescriptor

    Beta

    Computed as the slope coefficient in a time-series regression of excess stock return, 
    :math:`r_t - r_{ft}`, against the cap-weighted excess return of the estimation universe :math:`R_t`,

    ..  math:: r_t-r_{ft} = \alpha + \beta R_t + e_t

    The regression coefficients are estimated over the trailing 252 trading days of returns 
    with a half-life of 63 trading days.

RSTR
----

..  class:: quant.barra.factors.momentum.RSTR

    Relative strength

    Computed as the sum of excess log returns over the trailing T = 504 trading days with a lag of L=21 tradingdays,
    
    ..  math:: RSTR = \Sigma_{t=L}^{T+L}w_t[ln(1+r_t)-ln(1+r_{ft})]
    
    where :math:`r_t` is the stock return on day t, :math:`r_{ft}` is the risk-free return, and :math:`w_t` is an
    exponential weight with a half-life of 126 trading days.

LnCap
-----

..  class:: quant.barra.factors.size.LnCap

    Natural log of market cap

    Given by the logarithm of the total market capitalization of the firm.

BToP
----

..  class:: quant.barra.factors.book_to_price.B2P

    Book-to-price ratio

    Last reported book value of common equity divided by current market capitalization.

EPFWD
-----

..  class:: quant.barra.factors.earnings_yield.EPFWD

    Predicted earnings-to-price ratio

    Given by the 12-month forward-looking earnings divided by the current 
    market capitalization. Forward-looking earnings are defined as a 
    weighted average between the average analyst-predicted earnings for 
    the current and next fiscal years.

CEToP
-----

..  class:: quant.barra.factors.earnings_yield.CEToP

    Cash earnings-to-price ratio

    Given by the trailing 12-month cash earnings divided by current price.

EToP
----

..  class:: quant.barra.factors.earnings_yield.EToP

    Trailing earnings-to-price ratio

    Given by the trailing 12-month earnings divided by the current market capitalization. 
    Trailing earnings are defined as the last reported fiscal-year earnings plus the 
    difference between current interim figure and the comparative interim figure from the 
    previous year.


EGRLF
-----

..  class:: quant.barra.factors.growth.EGRLF

    Long-term predicted earnings growth

    Long-term (3-5 years) earnings growth forecasted by analysts.

EGRSF
-----

..  class:: quant.barra.factors.growth.EGSRLF

    Short-term predicted earnings growth

    Short-term (1 year) earnings growth forecasted by analysts.

EGRO
----

..  class:: quant.barra.factors.growth.EGSRO

    Earnings growth (trailing five years)

    Annual reported earnings per share are regressed against time over the past 
    five fiscal years. The slope coefficient is then divided by the average 
    annual earnings per share to obtain the earnings growth.

MLEV
----

..  class:: quant.barra.factors.leverage.MLEV

    Market leverage

    Computed as
    MLEV = (ME + PE + LD) / ME
    where ME is the market value of common equity on the last trading day, 
    PE is the most recent book value of preferred equity, and LD is the 
    most recent book value of long-term debt.

BLEV
----

..  class:: quant.barra.factors.leverage.BLEV

    Book leverage

    Computed as
    BLEV = (BE + PE + LD) / ME
    where BE is the book value of common equity on the last trading day, 
    PE is the most recent book value of preferred equity, and LD is the 
    most recent book value of long-term debt.

DToA
----

..  class:: quant.barra.factors.leverage.DToA

    Debt-to-assets

    Computed as

    .. math:: DTOA = TD / TA

    where TD is the book value of total debt (long-term debt and current liabilities), 
    and TA is most recent book value of total assets.

STOM
----

..  class:: quant.barra.factors.liquidity.STOM

    Share turnover, one month

    Computed as the log of the sum of daily turnover during the previous 21 trading days,

    ..  math:: STOM = ln[\Sigma_{t=1}^{21}\frac{V_t}{S_t}]

    where Vt is the trading volume on day t , and St is the number of shares outstanding.

STOQ
----

..  class:: quant.barra.factors.liquidity.STOQ

    Share turnover, trailing 3 months

    Let STOM_t be the share turnover for month t , with each month consisting of 21 trading days. 
    The quarterly share turnover is defined by
    
    ..  math:: STOQ = ln[\frac{1}{T}\Sigma_{t=1}{T}exp\{STOM_t\}]
    
    where T = 3 months.

STOA
----

..  class:: quant.barra.factors.liquidity.STOA

    Share turnover, trailing 12 months

    Let STOM_t be the share turnover for month t , with each month consisting of 21 trading days. 
    The quarterly share turnover is defined by
    
    ..  math:: STOQ = ln[\frac{1}{T}\Sigma_{t=1}{T}exp\{STOM_t\}]

    where T = 12 months.

NLSize
------

..  class: quant.barra.factors.non_linear_size.NLSize

    Cube of Size

    First, the standardized Size exposure (i.e., log of market cap) is cubed. 
    The resulting factor is then orthogonalized with respect to the Size factor 
    on a regression-weighted basis. Finally, the factor is winsorized and standardized.

DASTD
-----

..  class: quant.barra.factors.residual_volatility.DASTD

    Daily standard deviation

    Computed as the volatility of daily excess returns over the past 252 trading days with a half-life of 42 trading days.

CMRA
----

..  class: quant.barra.factors.residual_volatility.CMRA

    Cumulative range

    This descriptor differentiates stocks that have experienced wide swings over the last 12 months 
    from those that have traded within a narrow range. Let Z(T) be the cumulative
    excess log return over the past T months, with each month defined as the previous 21 trading days.

HSigma
------

..  class: quant.barra.factors.residual_volatility.HSigma

    Historical sigma

    Computed as the volatility of residual returns in Equation A1,
    The volatility is estimated over the trailing 252 trading days of returns with a half-life of
    63 trading days.
    The Residual Volatility factor is orthogonalized with respect to Beta and Size to reduce collinearity.

Factors
=======

Beta
----

..  math:: Beta = 1.0 * BetaDescriptor

BookToPrice
-----------

..  math:: BookToPrice = 1.0 * BToP

EarningsYield
-------------

..  math:: EarningsYield = 0.68 * EPFWD + 0.21 * CEToP +  0.11 * EToP

Growth
------

..  math:: Growth = 0.18 * EGRLF + 0.11 * EGRSF + 0.24 * EGRO + 0.47 * SGRO

Leverage
--------

..  math:: Leverage = 0.38 * MLEV + 0.35 * DToA + 0.27 * BLEV

Liquidity
---------

..  math:: Liquidity = 0.35 * STOM + 0.35 * STOQ + 0.30 * STOA

Momentum
--------

..  math:: Momentum = 1.0 * RSTR

NonLinearSize
-------------

..  math:: NonLinearSize = 1.0 * NLSize

ResidualVolatility
------------------

..  math:: ResidualVolatility = 0.74 * DASTD + 0.16 * CMRA + 0.10 * HSigma

Size
----

..  math:: Size = 1.0 * LnCap
