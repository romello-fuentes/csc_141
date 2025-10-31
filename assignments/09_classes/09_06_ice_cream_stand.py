# 9-6, ice cream stand, pg 211


class restauraunt:

    def __init__(self, restauraunt_name, cuisine_type, ):

        self.restauraunt_name = restauraunt_name
        self.cuisine_type = cuisine_type

    def describe_restauraunt(self):

        print(f"{self.restauraunt_name} serves {self.cuisine_type} cuisine.")

    def open_restauraunt(self):

        print(f"{self.restauraunt_name} is now open!")
    
class IceCreamStand(restauraunt):

    def __init__(self, name, cuisine_type='ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restauraunt()
big_one.show_flavors()