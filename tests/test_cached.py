from rabbits import iterative, recursive

TEST_DATA = [1, 2, 3, 4, 6, 89, 734, 22, 2, 7, 1, 0]

RESULTS_1 = []

for months in TEST_DATA:
    RESULTS_1.append(iterative.pairs(months))

def test_cache_iter():
    for idx in range(len(RESULTS_1)):
        assert iterative.pairs(TEST_DATA[idx]) == RESULTS_1[idx]

def test_iter_vs_recur():
    for nmonths in TEST_DATA:
        assert iterative.pairs(nmonths) == recursive.pairs(nmonths)

