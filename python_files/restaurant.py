"""A class that can be used to represent a restaurant."""

class Restaurant():
    """A restaurant that stores the name and cuisine type."""
    
    def __init__(self, restaurant_name, cuisine_type, number_served=0):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print("The restaurant is called " + self.restaurant_name.title() + ".")
        print("It serves " + self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open!")

    def set_number_served(self, number_served):
        """Set the number of customers that have been served.""" 
        self.number_served = number_served
        print("The number of people served has updated to: " + str(self.number_served))

    def increment_number_served(self, numbers):
        """Increments
        the number of customers who've been served."""
        self.number_served += numbers