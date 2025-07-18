from rabbits import iter

TEST_DATA = [1, 2, 3, 4, 6, 89, 1234, 22, 2, 7, 1, 0]

RESULTS_1 = []

for months in TEST_DATA:
    RESULTS_1.append(iter.pairs(months))

def test_cache():
    for idx in range(len(RESULTS_1)):
        assert iter.pairs(TEST_DATA[idx]) == RESULTS_1[idx]

 
