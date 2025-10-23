#

#8-1
def display_message():
    """Display message about what we are learning"""
    msg = " I am learning to write functions "
    print(msg)
display_message()

#8-2
def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(f"{title} is one of my favorite books.")

favorite_book('The 48 Laws of Power')


#8-5
def describe_city(city, country='chile'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('santiago')
