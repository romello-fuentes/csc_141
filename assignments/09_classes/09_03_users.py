# 9-3, users, pg 200

class user: 
    def __init__(self, first_name, last_name, username, email, bio):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.bio = bio

    def describe_user(self):
        print(f"\n{self.first_name}, {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Bio: {self.bio}")


    def greet_user(self):
        print(f"\n Welcome back {self.username}")

user1 = user('efrain', 'bonilla', 'big E', 'onlyE@gmail.com', 'the biggest E')
user2 = user('gabe', 'laws', 'guppy', 'glaws@gmail.com', 'self taught')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
