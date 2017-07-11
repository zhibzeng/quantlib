# Quantlib

[![Documentation Status](https://readthedocs.org/projects/quantlib/badge/?version=latest)](http://quantlib.readthedocs.io/?badge=latest)
[![Build Status](https://travis-ci.org/SnowWalkerJ/quantlib.svg?branch=master)](https://travis-ci.org/SnowWalkerJ/quantlib)

Quantlib是一个个人维护、使用的量化模块，主要用于金融数据的获取、清洗、变换和分析等功能。

------------------

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
wind.get_wind_data("AShareEODPrices", "s_dq_pctchange") / 100   # 获取涨跌幅
wind.get_wind_table("AShareST")                               # 获取ST信息
```

## Backtest

![Backtest Web Visualizer](http://quantlib.readthedocs.io/_static/backtest_web.jpg)

参考相应[文档](http://quantlib.readthedocs.io/backtest.html)

## Documents

文档部署在[Readthedocs](http://quantlib.readthedocs.io/)上。