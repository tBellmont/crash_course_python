requested_toppings = ['pepperoni', 'peppers','olives','mushrooms']
banned_topping = 'mushrooms'

if banned_topping in requested_toppings:
    print(f'No {banned_topping.title()} bro, they are rank.')
else:
    print('Carry on!')



