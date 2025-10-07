# 6-8, Pets, 149


pet1 = {
    'animal type': 'python',
    'name': 'Blanco',
    'owner': 'Laws',
    'weight': 12,
    'eats': 'bugs',
}

pet2 = {
    'animal type': 'chicken',
    'name': 'Clarence',
    'owner': 'Tom',
    'weight': 2,
    'eats': 'seeds'
}

pet3 = {
    'animal type': 'dog',
    'name': 'Smokey',
    'owner': 'Eric',
    'weight': 37,
    'eats': 'shoes'
}
pets = [pet1,pet2,pet3]

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")