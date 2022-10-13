# fruit = ['banana','apple','grape','pear','raspberry']

# print("The first three fruits in the list are: ")
# print(fruit[:3])

# print("\nThe three fruits from the middle of the list are: ")
# print(fruit[1:4])

# print("\nThe last three fruits in the list are: ")
# print(fruit[-3:])

my_fruits = ['banana','apple','grape']
friend_fruits = my_fruits[:]
#'pear','raspberry'

print(my_fruits)
print(friend_fruits)

my_fruits.append('pear')
friend_fruits.append('raspberry')


print('\nMy favourite fruits are: ')
for my_fruit in my_fruits:
    print(my_fruit)

print('\nMy friends favourite fruits are: ')
for friend_fruit in friend_fruits:
    print(friend_fruit)
