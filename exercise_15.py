# rental_car = input("What car would you like to rent? ")
# print("Ok let me see if we have a " + rental_car + " available.")

# dinner_group = input("How many people are in your dinner group? ")
# dinner_group = int(dinner_group)

# if dinner_group >= 8:
#     print(f"Sorry, {dinner_group} is too many, you'll have to wait or book I'm afriad.")
# else:
#     print(f"Sure we can accomodate for {dinner_group}. Come right this way!")


number = input("What number have you chosen? ")
number = int(number)

if number % 10 == 0:
    print("Your number is a multiple of 10!")
else:
    print("Your number is not a multiple of 10.")
