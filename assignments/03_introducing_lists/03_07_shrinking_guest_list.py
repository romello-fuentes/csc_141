# 3-7, Shrinking List, Pg 80

# shrinking_guest_list.py

guests = ["Nikola Tesla", "Bruce Lee", "Galileo Galilei", 
          "Isaac Newton", "Leonardo da Vinci", "Ada Lovelace"]

print("Unfortunately, I can only invite two people for dinner.\n")

# Remove guests until only 2 remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can’t invite you to dinner.")

print("\nThe guests who are still invited:")
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner at my place!")

# Clear the list
del guests[:]

print("\nFinal guest list:", guests)  # Should be empty
