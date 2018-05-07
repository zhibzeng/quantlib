"""
插件模块
========

回测可用的插件，通过Strategy类的MODS成员载入，可通过注册回测过程中的事件钩子来对干预回测过程、或收集回测中的数据以便分析。

自带模块
--------

+------------------+-----------------------------------------------------------+
|Mod Name          |Purpose                                                    |
+==================+===========================================================+
|NoSTUniverse*     |Remove ST stocks from universe                             |
+------------------+-----------------------------------------------------------+
|NoIPOUniverse*    |Remove new stocks from universe                            |
+------------------+-----------------------------------------------------------+
|NoUpLimitUniverse*|Remove stocks that reach up-limit from universe            |
+------------------+-----------------------------------------------------------+
|ActivelyTraded*   |Remove inactive stocks (daily amount<10million)            |
+------------------+-----------------------------------------------------------+
|ShowBasicResults* |Show simple statistic infomation after backtest            |
+------------------+-----------------------------------------------------------+
|Abigale*          |Generate analytical details for abigale2                   |
+------------------+-----------------------------------------------------------+
|Output            |Save position information to 'output.h5'                   |
+------------------+-----------------------------------------------------------+
|Visualizer        |Show details of backtest in webpage (abigale is preferred) |
+------------------+-----------------------------------------------------------+

星号表达模块默认被加载
"""
from .valid_universe import *
from .results import *
# from .visualize import *
from .output import *
from .abigale import AbigaleMod
