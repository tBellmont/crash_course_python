
# class Restaurant():
#     """A restaurant that stores the name and cuisine type."""
    
#     def __init__(self, restaurant_name, cuisine_type, number_served=0):

#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = number_served

#     def describe_restaurant(self):
#         print("The restaurant is called " + self.restaurant_name.title() + ".")
#         print("It serves " + self.cuisine_type.title() + " cuisine.")

#     def open_restaurant(self):
#         print(self.restaurant_name.title() + " is open!")

#     def set_number_served(self, number_served):
#         """Set the number of customers that have been served.""" 
#         self.number_served = number_served
#         print("The number of people served has updated to: " + str(self.number_served))

#     def increment_number_served(self, numbers):
#         """Increments
#         the number of customers who've been served."""
#         self.number_served += numbers


# restaurant = Restaurant('the little garden house', 'french')
# restaurant_1 = Restaurant('the little garden house', 'french')
# restaurant_2 = Restaurant('looking glass', 'thai')
# restaurant_3 = Restaurant('the brown paper bag', 'american')

# restaurant.set_number_served(10)
# restaurant.increment_number_served(4)
# print(restaurant.number_served)

class User():
    """The user class."""

    def __init__(self, first_name, last_name, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.login_attempts = 0

    def describe_user(self):
        """A method which describes the user."""
        print("The users name is: " + self.first_name.title() + " " + self.last_name.title())
        print("The users id number is: " + str(self.user_id))

    def greet_user(self):
        """Method that greets the user."""
        print("Hello user " + str(self.user_id) + ", how are you today?")

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts"""
        self.login_attempts = 0

user_1 = User('tom', 'bellmont', 4752)

print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)