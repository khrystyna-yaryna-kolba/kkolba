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
        strat = Validation.validate_strategy(strat)
        self._strategy = strat
