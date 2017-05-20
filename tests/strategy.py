from quant.backtest.stock.strategy import AbstractStrategy
import cProfile


class Test(AbstractStrategy):
    start_date = "2017-03-01"
    def handle(self, today, universe):
        self.change_position({universe[0]: 0.5})


if __name__ == "__main__":
    strategy = Test()
    cProfile.run("strategy.run()", "profile")
    strategy.run()
