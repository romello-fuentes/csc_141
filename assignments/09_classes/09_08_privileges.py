# 9-8, privledges, pg 211


class User: 
    def __init__(self, first_name, last_name, username, email, bio):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.bio = bio
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Bio: {self.bio}")

    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- No privileges assigned.")


class Admin(User):
    def __init__(self, first_name, last_name, username, email, bio):
        super().__init__(first_name, last_name, username, email, bio)
        self.privileges = Privileges()


romie = Admin('romie', 'fuentes', 'r_fuentes', 'r_fuentes@gmail.com', 'Reading')
romie.describe_user()
romie.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
romie.privileges.privileges = eric_privileges
romie.privileges.show_privileges()
