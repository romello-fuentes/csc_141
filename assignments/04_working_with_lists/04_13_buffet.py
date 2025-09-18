# 4-13, buffet, Pg 98


# List of 5 foods
buffet_foods = ("pizza", "salad", "pasta", "soup", "bread")

# For loop to print each food
print("Original buffet menu:")
for food in buffet_foods:
    print(food)

# Try to modify one of the items ERROR
# buffet_foods[0] = "sushi"   Python will reject this

# Rewrite the tuple with two changed items
buffet_foods = ("sushi", "salad", "pasta", "tacos", "bread")

# Print the revised menu
print("\nRevised buffet menu:")
for food in buffet_foods:
    print(food)
