# 10-13, verify user, pg 244 


import json

filename = 'user_info.json'

name = input("What's your name? ")
age = input("How old are you? ")
color = input("What's your favorite color? ")

user_data = {
    'name': name,
    'age': age,
    'favorite_color': color
}

with open(filename, 'w') as f:
    json.dump(user_data, f)

with open(filename) as f:
    stored = json.load(f)
    print("\nHere's what I remember about you:")
    print(f"Name: {stored['name']}")
    print(f"Age: {stored['age']}")
    print(f"Favorite Color: {stored['favorite_color']}")
