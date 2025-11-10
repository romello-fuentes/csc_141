# 10-7, addition calc, pg 238

print("Enter 'q' at any time to quit.")

while True:
    num1 = input("Enter the first number: ")
    if num1.lower() == 'q':
        break
    num2 = input("Enter the second number: ")
    if num2.lower() == 'q':
        break

    try:
        total = int(num1) + int(num2)
        print(f"The sum is: {total}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
