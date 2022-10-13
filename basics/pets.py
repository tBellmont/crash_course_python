# pets = ['rabbit', 'goldfish', 'dog', 'pig', 'rabbit']
# print(pets)

# while 'rabbit' and 'dog' in pets:
#     pets.remove('rabbit')
#     print(pets)
#     pets.remove('dog')

# print(pets)

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='butterfly', pet_name='jonny')
describe_pet(pet_name='wilf', animal_type='dog')