quant.backtest
==============

..  currentmodule:: quant.backtest

Get Started
-----------

一个简单的股票回测程序只需要继承一个抽象策略类，定义一个选股策略就可以，一个简单的例子是:

..  code-block:: python

    from quant.backtest.stock.strategy import AbstractStrategy


    class SimpleStrategy(AbstractStrategy):
        start_date = "2017-03-01"
        def handle(self, today, universe):
            self.change_position({universe[0]: 0.1})

这个简单的策略定义了从2017年3月开始回测，每天选择可选股票池中的第一只股票买入10%的仓位。
运行`SimpleStrategy().run()`运行回测，几秒钟后，会输出简单的年化收益率、年化波动率和夏普率信息。