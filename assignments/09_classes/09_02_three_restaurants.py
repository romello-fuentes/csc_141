# 9-2, three restraunts, pg 200 


class restauraunt:

    def __init__(self, restauraunt_name, cuisine_type):

        self.restauraunt_name = restauraunt_name
        self.cuisine_type = cuisine_type

    def describe_restauraunt(self):

        print(f"{self.restauraunt_name} serves {self.cuisine_type} cuisine.")

    def open_restauraunt(self):

        print(f"{self.restauraunt_name} is now open!")


restaurant = restauraunt('mamas', 'pizza')
restaurant1 = restauraunt("papa johns", "pizza")
restaurant2 = restauraunt("pizza hut", "pizza")
restaurant3 = restauraunt("dominos", "pizza")

restaurant.describe_restauraunt()
restaurant1.describe_restauraunt()
restaurant2.describe_restauraunt()
restaurant3.describe_restauraunt()
