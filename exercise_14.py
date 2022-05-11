

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

favoruite_places = {
    'tom': 'india', 
    'ross': 'wales', 
    'rosie': 'peru',
    }
    
for person, place in favoruite_places.items():
    print(person.title() + "'s favourite place is " + place.title() + ".")