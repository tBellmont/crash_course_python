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



