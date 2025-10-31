# 9-15, lottery analysis, pg 218

import random
from lottery import Lottery

my_ticket = ['1', 'b', '7', 'd']

attempts = 0
won = False

while not won:
    attempts += 1
    drawn = random.sample(Lottery, 4)
    if sorted(drawn) == sorted(my_ticket):
        won = True

print(f"\nYour ticket {my_ticket} won after {attempts} attempts!")
