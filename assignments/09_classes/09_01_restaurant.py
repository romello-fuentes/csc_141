# 9-1, restraunt, pg 200 


class restauraunt:

    def __init__(self, restauraunt_name, cuisine_type):

        self.restauraunt_name = restauraunt_name
        self.cuisine_type = cuisine_type

    def describe_restauraunt(self):

        print(f"{self.restauraunt_name} serves {self.cuisine_type} cuisine.")

    def open_restauraunt(self):

        print(f"{self.restauraunt_name} is now open!")


restaurant = restauraunt('mamas', 'pizza')
print(restaurant.restauraunt_name)
print(restaurant.cuisine_type)



restaurant.describe_restauraunt()
restaurant.open_restauraunt()