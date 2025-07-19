MATURITY = 3


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
    


if __name__ == '__main__':
    MAX_MONTHS = 43
    TRUNCATE_AT = 29
    print(f"Rabbit pair ages, truncating at {TRUNCATE_AT} rabbit pairs:")
    pool = RabbitPool()
    print([ pair.months for pair in pool.pairs ])
    for _ in range(MAX_MONTHS):
        pool.progress()
        print([ pair.months for pair in pool.pairs[:TRUNCATE_AT] ])
        

