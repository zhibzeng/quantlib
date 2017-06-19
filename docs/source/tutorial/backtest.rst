quant.backtest
**************

..  currentmodule:: quant.backtest

Get Started
===========

一个简单的股票回测程序只需要继承一个抽象策略类，定义一个选股策略就可以，一个简单的例子是:

..  code-block:: python

    from quant.backtest.stock.strategy import AbstractStrategy


    class SimpleStrategy(AbstractStrategy):
        start_date = "2017-03-01"
        def handle(self, today, universe):
            self.change_position({universe[0]: 0.1})

这个简单的策略定义了从2017年3月开始回测，每天选择可选股票池中的第一只股票买入10%的仓位。
运行``SimpleStrategy().run()``运行回测，几秒钟后，会输出简单的年化收益率、年化波动率和夏普率信息。
同时，还会生成一个以策略名和运行时间命名的网页，记录着回测的详细信息。如果是在视窗环境下的话，浏览器会自动打开该网页。如图所示。

..  image:: _static/backtest_web.jpg

Data
====

原则上，在回测中可以使用普通的quant.data.wind接口获取数据，但是这样难以控制获取未来数据的风险，
为了在一定程度上减轻这个问题，用户可以使用``quant.backtest.common.market.get_wind_data``来代替
原有的``quant.data.wind.get_wind_data``，该函数会自动对获取的数据进行截取，来确保不会出现未来函数。


Mods
====

本回测框架提供一些可选模块来支持扩展特性，同时也允许用户自定义模块。默认提供的模块有：

+-----------------+---------------------------------------------------+
|Mod Name         |Purpose                                            |
+=================+===================================================+
|NoSTUniverse     |Remove ST stocks from universe                     |
+-----------------+---------------------------------------------------+
|NoIPOUniverse    |Remove new stocks from universe                    |
+-----------------+---------------------------------------------------+
|NoUpLimitUniverse|Remove stocks that reach up-limit from universe    |
+-----------------+---------------------------------------------------+
|ActivelyTraded   |Remove inactive stocks (daily amount<10million)    |
+-----------------+---------------------------------------------------+
|ShowBasicResults |Show simple statistic infomation after backtest    |
+-----------------+---------------------------------------------------+
|WebVisualizer    |Show detailed information in webpage after backtest|
+-----------------+---------------------------------------------------+
|Output           |Save position information to 'output.h5'           +
+-----------------+---------------------------------------------------+

默认以上所有模块都会自动被加载，用户也可以在策略类的mods属性中定义自己要使用的模块，如::

    class Strategy(AbstractStrategy):
        mods = ["ShowBasicResults"]
    
则以上策略只会显示简单的回测信息，且不会对可选股票池作任何变化。


Developer
=========

To be expected.
