"""A set of classes used to represent gas and electric cars."""


# Define the class name
class Car(): 
    #Give the class a descriptions
    """A simple attempt to represent a car."""
    # Define the init method with the self variable and the attributes.
    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        # Assign the attribute variables to 'self'
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Prints the car's milage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer silly!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Fills the gas tank"""
        print("You filled your gas!")

my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()


# my_prius.battery.get_range()
# my_prius.battery.upgrade_battery()
# my_prius.battery.get_range()