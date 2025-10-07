# 6-9, Favorite Places, pg 149


favorite_places = {
    'Mr. Rice': ['eagle mountain', 'death valley', 'iceland'],
    'Mrs. Kardoley': ['new jersey', 'deleware'],
    'Gabe': ['the pagoda', 'the playground', 'north carolina']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")
        