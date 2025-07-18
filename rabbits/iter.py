MATURITY = 3

CACHE = [1, 1, 1]

def fill_cache(months: int):
    while months >= len(CACHE):
        CACHE.append(CACHE[-1] + CACHE[-MATURITY])

def pairs(months: int) -> int:
    assert months >= 0, "Months must be non-negative"
    if months < len(CACHE):
        return CACHE[months]
    fill_cache(months)
    return CACHE[-1]

