# 9-4, number served, pg 204 


class restauraunt:

    def __init__(self, restauraunt_name, cuisine_type):

        self.restauraunt_name = restauraunt_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restauraunt(self):

        print(f"{self.restauraunt_name} serves {self.cuisine_type} cuisine.")

    def open_restauraunt(self):

        print(f"{self.restauraunt_name} is now open!")
    
    def set_number_served(self, number_served):

        self.number_served = number_served

    def increment_number_served(self, additional_served):
        
        self.number_served += additional_served

    

restaurant = restauraunt('mamas', 'pizza')
restaurant.describe_restauraunt()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 500
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1000)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(250)
print(f"Number served: {restaurant.number_served}")