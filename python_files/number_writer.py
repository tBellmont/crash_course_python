import json

# numbers = [2, 3, 5, 7, 11, 13]

filename = 'json_files/numbers.json'
# with open(filename, 'w') as file_objects:
#     json.dump(numbers, file_objects)

with open(filename) as file_objects:
    numbers = json.load(file_objects)

print(numbers)