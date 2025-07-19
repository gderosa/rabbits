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
        for pair in self.pairs:
            pair.progress()
    
    def N(self):
        return len(self.pairs)
    
    def age(self):
        return self.pairs[0].months
    


if __name__ == '__main__':
    pool = RabbitPool()
    for n in range(12):
        print(n, pool.age(), pool.N())
        pool.progress()
        print(n, pool.age(), pool.N())

