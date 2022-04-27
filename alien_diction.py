# alien_0 = {'color': 'green', 'points': 5}

# new_points = alien_0['points']
# print("Well done! You just earned " + str(new_points) + " points!")


# alien_0 = {}
# print(alien_0)
# alien_0 = {'color': 'green', 'points': 5}

# alien_0['x_pos'] = 0
# alien_0['y_pos'] = 25
# print(alien_0)

# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")
# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")

# Create alien dictionary, define position and speed
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))

# # Move the alien to the right.
# # Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# # The new position is the old position PLUS the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print("The new position of the alien is: " + str(alien_0['x_position']))

# alien_0 = {'colour': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)