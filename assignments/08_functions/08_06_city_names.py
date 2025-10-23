# 8-6, city names, pg 179


def city_country(city, country):
    """Return string like 'Santiago, Chile'"""
    return f"{city.title()}, {country.title()}"

city = city_country('santiago', 'chile')
print(city)
