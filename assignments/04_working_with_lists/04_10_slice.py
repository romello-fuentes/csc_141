# 4-10, slice, Pg 103


# Start with a pizza list
pizzas = ["pepperoni", "margherita", "bbq chicken", "hawaiian", "veggie"]

# Print the first three items
print("The first three items in the list are:")
print(pizzas[:3])  # Slice from index 0 up to (but not including) 3

# Print three items from the middle of the list
print("\nThree items from the middle of the list are:")
middle_index = len(pizzas) // 2  # Find the middle index
print(pizzas[middle_index-1:middle_index+2])  # Take 3 items around the middle

# Print the last three items
print("\nThe last three items in the list are:")
print(pizzas[-3:])  # Slice the last 3 items
