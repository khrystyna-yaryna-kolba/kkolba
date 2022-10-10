from validation import Validation
from strategy import *
class Context:
    def __init__(self, strat = None):
        self.strategy = strat

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strat):
        if strat and not isinstance(strat, SecondStrategy) and not isinstance(strat,FirstStrategy):
            raise ValueError("Not strategy object")
        self._strategy = strat
