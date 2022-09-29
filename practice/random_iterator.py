import random

class RandomIterator:
    def __init__(self, n, a, b):
        self._n = n
        self._a = a
        self._b = b
    def __iter__(self):
        return self
    def __next__(self):
        if self._n == 0:
            raise StopIteration
        else:
            self._n -= 1
            return random.randrange(self._a, self._b + 1)
