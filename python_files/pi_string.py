filename = 'text_files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = '120372'
if birthday in pi_string:
    print("Yes it is!")
else:
    print('Nah...')