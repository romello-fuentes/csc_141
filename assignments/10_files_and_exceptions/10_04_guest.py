# 10-4, guest, pg 230 


name = input("What is your name? ")

with open("C:/Users/romfu/Desktop/csc_141/assignments/10_files_and_exceptions/guest.txt", "w") as file:
    file.write(name)

print(f"Welcome, {name}! Your name has been recorded.")
