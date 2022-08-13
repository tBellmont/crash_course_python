# sandwich_orders = ['ham', 'tuna', 'cheese', 'chorizo', 'pastrami', 'pastrami', 'pastrami']
# finished_sandwiches = []

# print("The deli has run out of pastrami sandwiches!!")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()

#     print("Currently making a " + current_sandwich + " sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\nThe following sandwiches have been made: ")
# for finished_sandwich in finished_sandwiches:
#     print("A " + finished_sandwich + " sandwich.")

## Dream vacation

dream_vacation = {}

polling_active = True

while polling_active:
    name = input("What's your name? ")
    response = input("Where is your dream vacation? ")

    dream_vacation[name] = response

    repeat = input("Is anybody else participating in the poll? ")
    if repeat == 'no':
        polling_active = False
    
print("---Vacation Poll Results---")
for name, response in dream_vacation.items():
    print("\t" + name.title() + " would love to go to " + response + "!")

