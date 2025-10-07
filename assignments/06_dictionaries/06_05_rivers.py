# 6-5, Rivers, 143


rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'schuylkill': 'Uniited States'
}

# Sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")


# River names
print("\n\nRivers included:")
for river in rivers.keys():
    print(f"- {river.title()}")


# Country names
print("\n\nCountries included:")
for country in rivers.values():
    print(f"- {country.title()}")
