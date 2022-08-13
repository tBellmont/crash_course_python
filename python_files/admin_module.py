from user_module import User

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