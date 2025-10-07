# 6-7, People, Pg 149


people = []

person = {
    'first_name': 'Gabe',
    'last_name': 'Laws',
    'age': 18,
    'city': 'Reading',
    }
people.append(person)

person = {'first_name': 'Romie',
    'last_name': 'Valentine',
    'age': 18,
    'city': 'Reading'}
people.append(person)

person = {
    'first_name': 'Efrain',
    'last_name': 'Bonilla',
    'age': 17,
    'city': 'Reading',
    }
people.append(person)


for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")
