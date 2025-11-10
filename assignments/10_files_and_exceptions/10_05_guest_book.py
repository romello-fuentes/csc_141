# 10-5, Guest book, pg 230

print("Enter 'quit' to stop entering names.")

with open("C:/Users/romfu/Desktop/csc_141/assignments/10_files_and_exceptions/guest_book.txt", "a") as file:
    while True:
        name = input("What is your name? ")
        if name.lower() == 'quit':
            break
        file.write(name + "\n")
        print(f"Hello, {name}! You've been added to the guest book.")
