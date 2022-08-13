# def sandwich_fillings(*fillings):
#     """Print sandwich toppings."""
#     print("\nYou're sandwich has these fillings: ")
#     for filling in fillings:
#         print("- " + filling)

# sandwich_fillings('butter')
# sandwich_fillings('butter', 'ham')
# sandwich_fillings('butter', 'ham', 'tomatos')

# def build_profile(first, last, **user_info):
#     """Build a dictionary containing
#     everything we know about a user."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# user_profile = build_profile('Tom', 'Bellmont',
#                             location='Bristol',
#                             field='data analysis',
#                             hair='brown')

# print(user_profile)

def make_car(manufacturer, model, **specs):
    """Stores info about a car"""
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    for key, value in specs.items():
        car_info[key] = value
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)