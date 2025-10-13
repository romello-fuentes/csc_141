# 7-4, multiples of ten, pg 155


number = input("What is your number?")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
