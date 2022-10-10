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
        n = Validation.validate_non_negative_int(argv[0])
        a = Validation.validate_int(argv[1])
        b = Validation.validate_int(argv[2])
        a, b = Validation.validate_range(a, b)
        iterator = RandomIterator(n, a, b)
        for i in iterator:
            lis.insert(pos, i)
            pos += 1
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
                print("error in {} element in the file:".format(i), str(e))
                continue
        f.close()
        return lis
