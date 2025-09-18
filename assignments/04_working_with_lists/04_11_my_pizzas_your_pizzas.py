# 4-11, my pizzas your pizzas, Pg 103


# Original pizza list
pizzas = ["pepperoni", "cheese", "meatlovers"]

# Copy the list into a new one for a friend
friend_pizzas = pizzas[:]

# Add a new pizza to the original list
pizzas.append("hawaiian")

# Add another pizza to the friend's list
friend_pizzas.append("veggie")

# Print my favorite pizzas
print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

# Friend's favorite pizzas
print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)