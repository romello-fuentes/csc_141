# 10-6, addition, pg 238

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    total = num1 + num2
    print(f"The sum is: {total}")
except ValueError:
    print("Oops! Please enter valid numbers only.")
