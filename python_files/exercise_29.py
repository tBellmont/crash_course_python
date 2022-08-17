# print("Enter quit when ever you want to quit.")
# while True:
#     try:
#         x = input("Give me a number: ")
#         if x == 'quit':
#             break
#         x = int(x)

#         y = input("Give me another number: ")
#         if y == 'quit':
#             break
#         y = int(y)

#     except ValueError:
#         print("Sorry, I really needed a number.")

#     else:
#         sum = x + y
#         print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
# print("Program has ended!")

# filenames = ['text_files/catss.txt', 'text_files/dogs.txt']

# for filename in filenames:
#     try:
#         with open(filename) as file_object:
#             contents = file_object.read()
#     except FileNotFoundError:
#         # msg = "Sorry, the file or file and path " + filename + " does not exist."
#         # print(msg)
#         pass
#     else:
#         print(contents)

# line = "Row, row, row your boat."
# count = line.lower().count('row')
# print(count)

filenames = ['text_files/alice_in_wonderland.txt', 'text_files/the_soul_of_lilith.txt']

for filename in filenames:

    with open(filename) as file_object:
        contents = file_object.read()
        count = contents.lower().count('the')
        print(filename + " contains the word 'the' " + str(count) + " amount of times.")
        