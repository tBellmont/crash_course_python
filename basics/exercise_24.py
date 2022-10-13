
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



# class IceCreamStand(Restaurant):
#     """A child class of Restaurant which is an ice cream stand."""

#     def __init__(self, restaurant_name, cuisine_type, number_served=0):
#         """
#         Initialise attributes of the parent class.
#         Then initialize attributes specific to an ice cream stand.
#         """
#         super().__init__(restaurant_name,cuisine_type,number_served)
#         self.flavours = ['mint', 'rum & raisin', 'chocolate chip', 'vanilla']


#     def display_flavours(self):
#         """Method that displays all ice cream flavours"""

#         print("The ice crem flavours we have on offer are:")
#         for flavour in self.flavours:
#             print("\t- "+flavour.title())

# restaurant_2 = IceCreamStand('the little garden house', 'french')

# restaurant_2.display_flavours()


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


class Privileges():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self):
        """Initialise the battery's attributes."""
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """
        Function that displays the admin privileges."""
        print("You got these privileges:")
        for privilege in self.privileges:
            print("\t" + privilege.capitalize())


class Admin(User):
    """Admin child class."""

    def __init__(self, first_name, last_name, user_id):
        """
        Initialise attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(first_name, last_name, user_id)
        self.privileges = Privileges()




user_1 = Admin('tom', 'bellmont', 4752)

user_1.privileges.show_privileges()