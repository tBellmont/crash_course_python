age = 68

# if age >= 21:
#     print("You're old enough to drink in the USA!")
#     print("Have one on me!")
# else:
#     print("Sorry, you have to wait a bit before you can drink.")

# if age < 12:
#     print("You can only watch kids movies.")
# elif age < 15:
#     print("Some swearing is allowed.")
# elif age < 18:
#     print("I'll allow some violence.")
# else:
#     print("Whatever you want.")

if age < 12:
    price = 0
elif age < 15:
    price = 4
elif age < 18:
    price = 10
elif age < 65:
    price = 15
elif age >= 65:
    price = 0


print("The price you pay is £" + str(price) + ".")