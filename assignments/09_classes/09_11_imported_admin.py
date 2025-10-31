# 9-11 imported admin, pg 217

from admin import Admin


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
