# 5-8, Hello Admin, pg 126


usernames = ['admin', 'jaden', 'maria', 'sophia', 'lucas']

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
