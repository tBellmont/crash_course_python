file = 'text_files/learning_python.txt'

# with open(file) as file_open:
#     file_content = file_open.read()

# print(file_content)


with open(file) as file_open:
    lines = file_open.readlines()

file_string = ''

for line in lines:
    file_string += line

file_string = file_string.replace('python', 'C')

print(file_string)
