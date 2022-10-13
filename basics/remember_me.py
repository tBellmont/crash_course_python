import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

def get_stored_username():
    """Get stored usernam if available."""
    filename = 'json_files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'json_files/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    answer = input("Is " + username + " the current user?\nEnter y or n")
    if answer == "y":
        if username:
            print("Welcome back, " + username + "!")
        else:
            username = input("What is your name? ")
            filename = 'json_files/username.json'
            with open (filename, 'w') as f_obj:
                json.dump(username, f_obj)
                print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
        
greet_user()