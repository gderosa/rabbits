from rabbits import iterative, recursive, brute

# Experimenting on a reasonably modern laptop, this is the maxium without getting unreasonably slow...
MAX_MONTHS = 43

def test_iter_vs_brute():
    pool = brute.RabbitPool()
    for n in range(MAX_MONTHS):
        assert pool.N() == iterative.pairs(n)
        pool.progress()

