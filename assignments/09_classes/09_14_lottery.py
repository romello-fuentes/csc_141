#9-14, lottery, pg 218


import random

Lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = random.sample(Lottery,4)

print("\nWinning ticket:", winning_ticket)
print("If your ticket matches any of these 4 numbers or letters YOU WIN!!!")
