# 7-4, pizza toppings, pg 161


while True:
    topping = input("Enter a pizza topping or done to stop: ")
    if topping.lower() == 'done':
        break
    print(f"I'll add {topping} to your pizza!")
        