# 9-13, ordered direct redux, pg 218

from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number = randint(1, self.sides)
        print(number)

# 6 sided dice 
d6 = Die()
print("Rolling a 6-sided die:")
for _ in range(10):
    print(d6.roll_die())

# Roll a 10-sided die 10 times
d10 = Die(10)
print("\nRolling a 10-sided die:")
for _ in range(10):
    print(d10.roll_die())

# Roll a 20-sided die 10 times
d20 = Die(20)
print("\nRolling a 20-sided die:")
for _ in range(10):
    print(d20.roll_die())