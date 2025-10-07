# 6-11, Cities, pg 149


cities = {
    'wildwood': {
        'country': 'united states',
        'population': 5_113,
        'fun fact': 'Wildwood welcome over 9 million visitors a year making it the number one family resort at the Jersey Shore.',
        },
    'Lewes': {
        'country': 'united states',
        'population': 3_794,
        'fun fact': 'Lewes was the site of the first European settlement in Delaware established in 1631',
        },
    'cape may': {
        'country': 'united states',
        'population': 2_752,
        'fun fact': 'Cape May Lighthouse: Constructed in 1859, the Cape May Lighthouse stands at 157 feet tall and is a significant landmark.',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fun_fact = city_info['fun fact'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"It has a population of about {population}.")
    print(f"The {fun_fact}.")