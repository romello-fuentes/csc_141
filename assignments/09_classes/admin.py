# import admin 9-11

from user import User


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