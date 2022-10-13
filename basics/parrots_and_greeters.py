# special_word = "Grass"

# answer = input("Guess the word...:")

# if answer == special_word:
#     print("Well done!")
# else:
#     print("Doh! Try again.")

# name = input("Please enter your name: ")

# print("Hello " + name + "!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print("\nHello, " + name + "!")

# age = input("How old are you? ")
# # print("You are: " + age + " years old!")
# age = int(age)
# age >= 18


# prompt = "\nTell me something and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "

# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)


prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)