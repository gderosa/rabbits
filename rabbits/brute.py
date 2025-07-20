'''
Brute force approach. No analytical formula is used to predict the population.
Rather, at each "reproduction", a new object is literally created, and appended to a "pool"
i.e. a list if which we simply take the length.

Terrible performance but "it simply implements the problem", directly.
Can be used to compare with more analytical methods.
'''

from .constants import MATURITY

# Obtained empirically: beyond this, on a recent laptop (2023~2025), performance is less practical
MAX_MONTHS = 43


class RabbitPair:
    def __init__(self, pool):
        self.months = 0
        self.pool = pool
    
    def generate(self):
        self.pool.pairs.append(RabbitPair(self.pool))

    def progress(self):
        self.months += 1
        if self.months >= MATURITY:
            self.generate()
        


class RabbitPool:
    def __init__(self):
        self.pairs = [RabbitPair(self)]
    
    def progress(self):
        for n in range(self.N()):
            self.pairs[n].progress()
        # `for pair in self.pairs` may not work as expected as
        # looping over a list that gets new elements added while looping over it...
    
    def N(self):
        return len(self.pairs)
    
    def age(self):
        return self.pairs[0].months

