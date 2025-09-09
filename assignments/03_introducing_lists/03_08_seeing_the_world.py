# 3-8, Seeing The World, Pg 83

locations = ["Japan", "Brazil", "Italy", "Kenya", "Canada"]

print("Original list:")
print(locations)

print("\nAlphabetical order (using sorted()):")
print(sorted(locations))

print("\nOriginal list still unchanged:")
print(locations)

print("\nReverse alphabetical order (using sorted()):")
print(sorted(locations, reverse=True))

print("\nOriginal list still unchanged:")
print(locations)

print("\nReversing the list order (using reverse()):")
locations.reverse()
print(locations)

print("\nReversing the list again to restore original order:")
locations.reverse()
print(locations)

print("\nSorting the list alphabetically (using sort()):")
locations.sort()
print(locations)

print("\nSorting the list in reverse alphabetical order (using sort(reverse=True)):")
locations.sort(reverse=True)
print(locations)