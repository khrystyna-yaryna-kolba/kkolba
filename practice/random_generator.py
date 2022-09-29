from kkolba.helpers import*
import random
def random_generator(n,a,b):
    for i in range(n):
        yield random.randrange(a, b + 1)

