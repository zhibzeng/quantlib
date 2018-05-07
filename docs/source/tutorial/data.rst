Wind Data
*********

直接从万得SQL数据库查询数据，需要设置数据库连接信息。


配置信息
########

使用万得数据库需要配置数据库对应的连接信息。

配置文件``~/.quantlib/config.cfg``:

| wind_db_driver = 'pymysql'
| wind_db_type = 'mysql'
| wind_host = 'localhost'
| wind_port = 3306
| wind_username = 'wind'
| wind_password = 'password'
| wind_db_name = 'quant'


基本用法
########

股票基本信息
============

..  code-block::
    python

    from quant.data import wind
    wind.get_stock_basics()

量价数据
========

..  code-block::
    python

    wind.get_wind_data("AShareEODPrices", "s_dq_pctchange")


格式为wind.get_wind_data(表名,列名),会以trade_dt为index,s_info_windcode为column重新排列数据。

日衍生数据
==========

..  code-block::
    python

    # 获取A股个股市值
    wind.get_wind_data("AShareEODDerivativeIndicator", "s_val_mv")

万得数据库原始表
================

..  code-block::
    python

    wind.get_wind_table("AShareEODPrices", ["s_info_windcode", "trade_dt", "s_dq_adjclose", "s_dq_adjopen"])

获取指数权重
============

..  code-block::
    python

    # 获取中证500指数的免费权重
    wind.get_index_weight("AIndexHS300FreeWeight", "000905.SH")

获取A股特殊处理信息
===================

..  code-block::
    python

    # AShareST表示通过entry_dt和remove_dt来维护股票进入ST和离开ST的时间的
    # arrange_entry_table把该信息重新整理成以交易日为行、股票为列的“交易日”表
    # 最后把剩下的NA用False填充
    wind.arrange_entry_table("AShareST").fillna(False)

获取分析师预测数据
==================

..  code-block::
    python

    # 获取预测一年的平均每股收益
    wind.get_consensus_data('eps_avg', 1)

获取股票行业分类
================

..  code-block::
    python

    # 获取中国A股中信行业分类 （一级分类）
    wind.get_stock_industries("AShareIndustriesClassCITICS", 1)

