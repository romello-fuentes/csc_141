# 5-9, No User, pg 126

#Empty list
usernames = [] 

if usernames:
    for user in usernames:
        print(f"Hello {user.title()}")
else:
    print("We need to find some users!")
