# 4-13, buffet, Pg 98


# Step 1: Create a tuple with 5 foods
buffet_foods = ("pizza", "salad", "pasta", "soup", "bread")

# Step 2: Use a for loop to print each food
print("Original buffet menu:")
for food in buffet_foods:
    print(food)

# Step 3: Try to modify one of the items (this will cause an error if uncommented)
# buffet_foods[0] = "sushi"   # Tuples cannot be changed! Python will reject this.

# Step 4: Rewrite the tuple with two changed items
buffet_foods = ("sushi", "salad", "pasta", "tacos", "bread")

# Step 5: Print the revised menu
print("\nRevised buffet menu:")
for food in buffet_foods:
    print(food)
