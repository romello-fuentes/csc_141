# 6-12, extensions, pg 149 


pet1 = {
    'animal type': 'python',
    'name': 'Blanco',
    'owner': 'Laws',
    'weight': 12,
    'eats': 'bugs',
    'age': 5,
    'favorite_toy': 'hoop chain'
}

pet2 = {
    'animal type': 'chicken',
    'name': 'Clarence',
    'owner': 'Tom',
    'weight': 2,
    'eats': 'seeds',
    'age': 2,
    'favorite_toy': 'Mirror'
}

pet3 = {
    'animal type': 'dog',
    'name': 'Smokey',
    'owner': 'Eric',
    'weight': 37,
    'eats': 'shoes',
    'age': 4,
    'favorite_toy': 'ball',
}
pets = [pet1,pet2,pet3]

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
