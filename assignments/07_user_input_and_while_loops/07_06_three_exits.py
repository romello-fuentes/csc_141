# 7-6, three exits, pg 161


topping = ""
while topping != "quit":
    topping = input("Enter a pizza topping (or 'quit' to stop): ")
    if topping != "quit":
        print(f"I'll add {topping} to your pizza!")

# 7-6b. Using an active variable
active = True
while active:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza!")

# 7-6c. Using break
while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")
    if topping.lower() == 'quit':
        break
    print(f"I'll add {topping} to your pizza!")
