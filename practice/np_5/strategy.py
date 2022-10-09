from abc import ABC, abstractmethod
from random_iterator import *
from linked_list import *
import json
from validation import Validation
class Strategy(ABC):
    @abstractmethod
    def generate(self, lis, pos, *argv):
        pass


class FirstStrategy(Strategy):
    def generate(self, lis, pos, *argv):
        n = argv[0]
        a = argv[1]
        b = argv[2]
        iterator = RandomIterator(n, a, b)
        for i in iterator:
            lis.insert(pos, i)
            pos+=1
        return lis


class SecondStrategy(Strategy):
    def generate(self, lis, pos, *argv):
        f = argv[0]
        f = Validation.validate_file_name(f, "json")
        f = open(Validation.validate_existing_file(f), encoding='utf-8')
        file = json.load(f)
        for i, el in enumerate(file):
            try:
                e = Validation.validate_int(el)
                lis.insert(pos, e)
                pos+=1
            except ValueError as e:
                print(str(e))
                continue
        f.close()
        return lis
