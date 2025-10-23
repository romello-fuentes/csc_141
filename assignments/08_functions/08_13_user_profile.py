# 8-13, user profile, pg 187


def build_profile(first, middle, last, year, sport, **user_info):
    """Build a dictionary containing everything we know about a user."""     
    user_info['first_name'] = first
    user_info['middle_name']  = middle
    user_info['last_name'] = last
    user_info['birth_year'] = year
    user_info['sport'] = sport

    return user_info

user_profile = build_profile('romello', 'robert', 'fuentes', '2006', 'wrestler', location='reading', field='comp sci')

print(user_profile)
