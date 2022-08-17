filename = 'text_files/programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I like doing stuff.\n")