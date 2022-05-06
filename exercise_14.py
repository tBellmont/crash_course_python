

person_0 = {
    'first_name': 'laura', 
    'last_name': 'palmer', 
    'age': 21, 'city': 
    'twin peaks'
    },
person_1 = {
    'first_name': 'tom', 
    'last_name': 'bellmont', 
    'age': 29, 
    'city': 'bristol'
    }
    
people = [person_0, person_1]

for person in people:
    for column, value in person.items():
        full_name =  person['first_name'] + " " + person['last_name']
        print(full_name)