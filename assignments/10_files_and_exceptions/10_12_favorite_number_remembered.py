# 10-12, favorite number remembered, pg 244


import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
        print(f"I know your favorite number! It’s {number}.")
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("Got it! I'll remember that.")
