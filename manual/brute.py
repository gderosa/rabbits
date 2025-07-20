# TODO: avoid import path tweaks/boilerplate: `pip install -e` ? make this a proper package?
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rabbits

TRUNCATE_AT = 29

print(f"Rabbit pair ages, truncating at {TRUNCATE_AT} rabbit pairs:")
pool = rabbits.brute.RabbitPool()
print([ pair.months for pair in pool.pairs ])
for _ in range(rabbits.brute.MAX_MONTHS):
    pool.progress()
    print([ pair.months for pair in pool.pairs[:TRUNCATE_AT] ])
        
