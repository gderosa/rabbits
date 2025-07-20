from rabbits import iterative, brute

def test_iter_vs_brute():
    pool = brute.RabbitPool()
    for n in range(brute.MAX_MONTHS):
        assert pool.N() == iterative.pairs(n)
        pool.progress()

