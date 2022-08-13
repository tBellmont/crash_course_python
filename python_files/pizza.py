# def make_pizza(*toppings):
#     """Print the list of toppins that have been requested."""
#     print(toppings)

# make_pizza('peppers')
# make_pizza('mushies', 'sausage', 'onions')

def make_pizza(size, *toppings):
    """Summarise the pizza we are about to make."""
    print("\nMaking a size " + str(size) + " pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

