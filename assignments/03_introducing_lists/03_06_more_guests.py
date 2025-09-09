# 3-6, More Guests, Pg 80

guests = ["Bruce Lee", "Mike Tyson", "Leonardo da Vinci"]

print("Good news! I found a bigger dinner table, so more people can join us.\n")

# Insert at the beginning
guests.insert(0, "Nikola Tesla")

# Insert in the middle
guests.insert(len(guests)//2, "Galileo Galilei")

# Append to the end
guests.append("Ada Lovelace")

# New invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place!")
