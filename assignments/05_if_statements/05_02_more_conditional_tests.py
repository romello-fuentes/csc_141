# 5-2, more conditional test, pg 116


# String equality and inequality
fruit = "apple"
print("Is fruit == 'apple'? I predict True.")
print(fruit == "apple")  # True

print("\nIs fruit == 'orange'? I predict False.")
print(fruit == "orange")  # False

print("\nIs fruit != 'banana'? I predict True.")
print(fruit != "banana")  # True

print("\nIs fruit != 'apple'? I predict False.")
print(fruit != "apple")  # False


# Using the lower() method
name = "Alice"
print("\nIs name.lower() == 'alice'? I predict True.")
print(name.lower() == "alice")  # True

print("\nIs name.lower() == 'ALICE'? I predict False.")
print(name.lower() == "ALICE")  # False

# Numerical Test
age = 21
print("\nIs age == 21? I predict True.")
print(age == 21)  # True

print("\nIs age != 21? I predict False.")
print(age != 21)  # False

print("\nIs age > 18? I predict True.")
print(age > 18)  # True

print("\nIs age < 18? I predict False.")
print(age < 18)  # False

print("\nIs age >= 21? I predict True.")
print(age >= 21)  # True

print("\nIs age <= 20? I predict False.")
print(age <= 20)  # False


# Tests using 'and' and 'or'
x = 10
y = 5
print("\nIs x > 5 and y < 10? I predict True.")
print(x > 5 and y < 10)  # True

print("\nIs x < 5 and y < 10? I predict False.")
print(x < 5 and y < 10)  # False

print("\nIs x < 5 or y < 10? I predict True.")
print(x < 5 or y < 10)  #
