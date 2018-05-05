# Quantlib

[![Documentation Status](https://readthedocs.org/projects/quantlib/badge/?version=latest)](http://quantlib.readthedocs.io/?badge=latest)
[![Build Status](https://travis-ci.org/SnowWalkerJ/quantlib.svg?branch=master)](https://travis-ci.org/SnowWalkerJ/quantlib)

Quantlib is a library that serves quantitative trading. It offers data querying, data cleansing, calculation and backtesting.

------------------

## About language

This project is specialized in China A Share stocks, and highly depends on Wind database. So the users are expected to be Chinese.
Thus all the documents and comments will be Chinese.

## Get started

### Installation

```bash
git clone git@github.com:SnowWalkerJ/quantlib.git
python setup.py install
```

### Configuration

```bash
vim ~/.quantlib/config.cfg
```

And change the settings items such as wind db accounts and other preferences.

## Wind Data

```python
from quant.data import wind
wind.get_wind_data("AShareEODPrices", "s_dq_pctchange") / 100 # get price change
wind.get_wind_table("AShareST")                               # get special treatment list
```

## Backtest

![Backtest Web Visualizer](http://quantlib.readthedocs.io/_static/backtest_web.jpg)

参考相应[文档](http://quantlib.readthedocs.io/tutorial/backtest.html)

## Documents

文档部署在[Readthedocs](http://quantlib.readthedocs.io/)上。