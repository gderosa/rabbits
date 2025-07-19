# TODO: DRY

MATURITY = 3 
CACHE = [1] * MATURITY

def pairs(months: int) -> int:
    global CACHE
    assert months >= 0, "Months must be non-negative"
    if months >= len(CACHE):
        CACHE += months * [None]  # more than enough
    if not CACHE[months]:
        CACHE[months] = pairs(months - 1) + pairs(months - MATURITY)
    return CACHE[months]

