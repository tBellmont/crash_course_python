filename = 'text_files/pi_digits.txt'

# with open(filename) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

