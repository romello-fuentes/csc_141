# 7-5, movie tickets, pg 161


while True:
    age_input = input("Enter your age (or 'quit' to stop): ")
    if age_input.lower() == 'quit':
        break
    age = int(age_input)
    
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
