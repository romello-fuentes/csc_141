# 9-7, admin, pg 211


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


class admin(user):
    def __init__(self, first_name, last_name, username, email, bio):

        super().__init__(first_name, last_name, username, email, bio)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivledges:")
        for priviledge in self.privileges:
            print(f"-{priviledge}")

romie = admin('romie', 'fuentes', 'r_fuentes', 'r_fuentes@gmail.com', 'Reading')
romie.describe_user()

romie.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

romie.show_privileges()