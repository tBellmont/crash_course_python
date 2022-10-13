# filename = 'text_files/user_name2.txt'

# print("Enter 'quit' when you are finished.")
# while True:
#     user_name = input("Please enter your name: ")
#     if user_name == 'quit':
#         break
#     else:
#         with open(filename, 'a') as file_object:
#             file_object.write(user_name + "\n")
#         print("Hi " + user_name + ", you've been added to the guest book.")



filename = 'text_files/poll.txt'
print("Enter 'quit' when you're done.")
while True:
    reason = input("Why do you like programming?")
    if reason == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(reason + "\n")
            