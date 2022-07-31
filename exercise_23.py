
from pydoc import describe


class Restaurant():
    """A restaurant that stores the name and cuisine type."""
    
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant is called " + self.restaurant_name.title() + ".")
        print("It serves " + self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open!")

restaurant_1 = Restaurant('the little garden house', 'french')
restaurant_2 = Restaurant('looking glass', 'thai')
restaurant_3 = Restaurant('the brown paper bag', 'american')

class User():
    """The user class."""

    def __init__(self, first_name, last_name, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id

    def describe_user(self):
        """A method which describes the user."""
        print("The users name is: " + self.first_name.title() + " " + self.last_name.title())
        print("The users id number is: " + str(self.user_id))

    def greet_user(self):
        """Method that greets the user."""
        print("Hello user " + str(self.user_id) + ", how are you today?")

user_1 = User('tom', 'bellmont', 4752)

user_1.describe_user()
user_1.greet_user()
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# restaurant_1.describe_restaurant()
# restaurant_1.open_restaurant()

# restaurant_2.describe_restaurant()
# restaurant_2.open_restaurant()

# restaurant_3.describe_restaurant()
# restaurant_3.open_restaurant()