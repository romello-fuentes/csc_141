# 4-10, slice, Pg 103


# Pizza list
pizzas = ["pepperoni", "margherita", "bbq chicken", "hawaiian", "veggie"]

# Print the first three items
print("The first three items in the list are:")
print(pizzas[:3])  

# Print the next three items from the list
print("\nThree items from the middle of the list are:")
middle_index = len(pizzas) // 2  
print(pizzas[middle_index-1:middle_index+2]) 

# Print the last three items
print("\nThe last three items in the list are:")
print(pizzas[-3:])  
