from collections import OrderedDict
from random import randint

class Dice():
    """A class that defines a Dice."""
    def __init__(self):
        """Initialising the Dice attributes."""
        self.sides = 6

    def roll_dice(self):
        """Prints a random number between 1 and the number of sides the die has.
        """
        roll = randint(1, self.sides)
        print("The dice has landed on " + str(roll) + "!")

# roll_1 = Dice(10)
# roll_1.roll_dice()
# roll_2 = Dice(20)
# roll_2.roll_dice()
roll_3 = Dice()
roll_3.roll_dice()


# glossary = OrderedDict()

# glossary['integer'] = 'A whole number'
# glossary['string'] = 'Text information'
# glossary['float'] = 'A decimal number'



# # glossary = {
# #     'integer': 'A whole number',
# #     'string': 'Text information',
# #     'float': "A decimal number"
# # }

# print("My glossary:")

# for key, value in glossary.items():
#     print("The definition of " + key.title() + ' is "' + value + '".')
