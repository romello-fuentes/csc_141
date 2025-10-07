# 6-10, favorite numbers, pg 149


# 6-2, Favorite Numbers, pg 136

# Value with key-value pairs 
favorite_numbers = {
    'Gabe': [11,14],
    'Efrain': [65,82],
    'Kenly': [99,64],
    'Victor': [69,48],
    'Romello': [62,55]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"  {number}")