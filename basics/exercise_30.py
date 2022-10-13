import json



try:
    filename = 'json_files/fav_numb.json'
    with open(filename) as f_obj:
        favourite_number = json.load(f_obj)
except FileNotFoundError:
    filename = 'json_files/fav_numb.json'
    favourite_number = input("What is your favourite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(favourite_number, f_obj)
        print("Thanks for giving us the number: " + favourite_number + "!")
else:
    print("Ya number is: " + favourite_number)
