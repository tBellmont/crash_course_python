

# person_0 = {
#     'first_name': 'laura', 
#     'last_name': 'palmer', 
#     'age': 21, 'city': 
#     'twin peaks'
#     }
# person_1 = {
#     'first_name': 'tom', 
#     'last_name': 'bellmont', 
#     'age': 29, 
#     'city': 'bristol'
#     }
# person_2 = {
#     'first_name': 'danielle', 
#     'last_name': 'batten', 
#     'age': 27, 
#     'city': 'bristol'
#     }
    
# people = [person_0, person_1, person_2]

# for person in people:
#     print(person)

# favoruite_places = {
#     'tom': 'india', 
#     'ross': 'wales', 
#     'rosie': 'peru',
#     }
    
# for person, place in favoruite_places.items():
#     print(person.title() + "'s favourite place is " + place.title() + ".")

# favourite_numbers = {
#     'tom': [64, 45],
#     'gem': [12],
#     'brandon': [675],
# }

# for person, numbers in favourite_numbers.items():
#     if len(numbers) == 1:
#         print(person.title() + "'s favourite number is: ")
#         for number in numbers:
#             print(f"\t{number}")
#     else:
#         print(person.title() + "'s favourite numbers are: ")
#         for number in numbers:
#             print(f"\t{number}")

cities = {
    'london': {
        'country':'uk',
        'population': '6,000,000',
        'fact': 'It is very wet'
    },
    'tokyo': {
        'country':'japan',
        'population': '14,000,000',
        'fact': 'It is in Asia'
    },
    'barcelona': {
        'country':'spain',
        'population': '3,000,000',
        'fact': 'They speak Spanish'
    }
}

for city, info in cities.items():
    print(city.title())
    country = info['country']
    fact = info['fact']

    print("\tCountry: " + country.title())
    print("\tFact: " + fact)