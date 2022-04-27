# person_0 = {'first_name': 'laura', 'last_name': 'palmer', 'age': 21, 'city': 'twin peaks'}

# print(person_0['first_name'].title() + " " + person_0['last_name'].title())
# print(person_0['age'])
# print(person_0['city'].title())


# favourite_numbers = {
#     'tom': 64,
#     'gem': 12,
#     'brandon': 675
# }

# print("Tom's favourite number is " + 
#     str(favourite_numbers['tom']) + 
#     "."
#     )

# print("Gem's favourite number is " + 
#     str(favourite_numbers['gem']) + 
#     "."
#     )

# print("Brandon's favourite number is " + 
#     str(favourite_numbers['brandon']) + 
#     "."
#     )

glossary = {
    'integer': 'A whole number',
    'string': 'Text information',
    'float': "A decimal number"
}

print("My glossary:")

for key, value in glossary.items():
    print("The definition of " + key.title() + ' is "' + value + '".')