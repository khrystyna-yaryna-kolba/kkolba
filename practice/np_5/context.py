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
        if strat is not None and not isinstance(strat, Strategy):
            raise ValueError("Not strategy object. Error while trying initialize Context object")
        self._strategy = strat

    def execute_strategy(self, *args):
        if self.strategy is None:
            raise ValueError("Context object is not initialized with strategy yet!. Cannot perform strategy method!")
        return self.strategy.generate(*args)