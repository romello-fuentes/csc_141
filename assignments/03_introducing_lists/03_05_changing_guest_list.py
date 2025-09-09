# 3-5, Changing Guest List, Pg 80

guests = ["Bruce Lee", "Mike Tyson", "Leonardo da Vinci"]

# Original invitations
print(f"Dear {guests[0]}, you are invited to dinner at my place!")
print(f"Dear {guests[1]}, you are invited to dinner at my place!")
print(f"Dear {guests[2]}, you are invited to dinner at my place!")

# One guest can't make it
print(f"\nUnfortunately, {guests[1]} can’t make it to dinner.")

# Replace guest
guests[1] = "Isaac Newton"

# New invitations
print(f"\nDear {guests[0]}, you are still invited to dinner at my place!")
print(f"Dear {guests[1]}, you are invited to dinner at my place!")
print(f"Dear {guests[2]}, you are still invited to dinner at my place!")
