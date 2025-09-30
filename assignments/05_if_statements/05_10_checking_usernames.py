# 5-10, Checking Usernames, pg 126


current_users = ['admin', 'john', 'sarah', 'emma', 'lucas']
new_users = ['john', 'mike', 'emma', 'JASON', 'Admin']

# convert all current_users to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new one.")
    else:
        print(f"The username '{new_user}' is available!")
