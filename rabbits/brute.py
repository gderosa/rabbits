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
        self.months = 0
    
    def progress(self):
        self.months += 1
        for pair in self.pairs:
            pair.progress()
    
    def N(self):
        return len(self.pairs)

