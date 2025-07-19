from .constants import MATURITY

CACHE = [1] * MATURITY

def fill_cache(months: int):
    global CACHE
    while months >= len(CACHE):
        CACHE.append(CACHE[-1] + CACHE[-MATURITY])

def pairs(months: int) -> int:
    global CACHE
    assert months >= 0, "Months must be non-negative"
    if months < len(CACHE):
        return CACHE[months]
    fill_cache(months)
    return CACHE[-1]

