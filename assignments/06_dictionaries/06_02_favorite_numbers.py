# 6-2, Favorite Numbers, pg 136

# Value with key-value pairs 
favorite_numbers = {
    'Gabe': 11,
    'Efrain': 65,
    'Kenly': 99,
    'Victor': 69,
    'Romello': 62
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")
