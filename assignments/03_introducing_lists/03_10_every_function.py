# 3-10, Every function, Pg 83

items = ["Mount Everest", "Nile", "Python", "Tokyo", "French"]

# Print original list
print("Original list:")
print(items)

# sorted()
print("\nAlphabetical order (sorted()):")
print(sorted(items))

# sorted(reverse=True)
print("\nReverse alphabetical order (sorted()):")
print(sorted(items, reverse=True))

# reverse()
items.reverse()
print("\nList after reverse():")
print(items)

# reverse() again to restore
items.reverse()
print("\nList restored to original order:")
print(items)

# sort()
items.sort()
print("\nList after sort():")
print(items)

# sort(reverse=True)
items.sort(reverse=True)
print("\nList after sort(reverse=True):")
print(items)

# append()
items.append("Sahara Desert")
print("\nAfter append():")
print(items)

# insert()
items.insert(2, "Amazon")
print("\nAfter insert():")
print(items)

# pop()
popped_item = items.pop()
print(f"\nPopped item: {popped_item}")
print("List now:", items)

# remove()
items.remove("Python")
print("\nAfter remove('Python'):")
print(items)

# del
del items[0]
print("\nAfter del items[0]:")
print(items)

# len()
print("\nLength of list:", len(items))