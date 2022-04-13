# alien_colour = 'yellow'

# if alien_colour == 'green':
#     points = 5
# elif alien_colour == 'yellow':
#     points = 10
# elif alien_colour == 'red':
#     points = 15

# print("Congratulations, you've earned " + str(points) + " points!")

age = 14

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
elif age >= 65:
    stage = 'pensioner'

print ("Their age is " + str(age) + ", so that makes them a " + str(stage) + ".")
