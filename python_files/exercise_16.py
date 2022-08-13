
active = True
prompt = "\nEnter any topping's you'd like to add to the pizza!"
prompt += "\nWhen you're done just enter 'done'! "

while active:
    topping = input(prompt)

    if topping == 'done':
        active = False
    else:
        print("\nGood choice! I'll add " + topping + " to your pizza.") 

# prompt = "How old are you?"
# prompt += "\nEnter 'quit' when you are finished. "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)

#     if age <= 5:
#         print("  You get in free!")
#     elif age < 13:
#         print("  Your ticket is $10.")
#     else:
#         print("  Your ticket is $15.")