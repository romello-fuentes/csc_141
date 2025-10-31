# 9-5, login attempts, pg 205


class user: 
    def __init__(self, first_name, last_name, username, email, bio):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.bio = bio
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name}, {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Bio: {self.bio}")


    def greet_user(self):
        print(f"\n Welcome back {self.username}")

    def incriment_login_attemps(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = user('gabe', 'laws', 'guppy', 'glaws@gmail.com', 'self taught')
user1.describe_user()
user1.greet_user()

print("\nMaking 2 login attempts...")
user1.incriment_login_attemps()
user1.incriment_login_attemps()
print(f"  Login attempts: {user1.login_attempts}")

print("Resetting login attempts...")
user1.reset_login_attempts()
print(f"  Login attempts: {user1.login_attempts}")