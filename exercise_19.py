# def make_shirt(message, size='Large'):
#     """Accepts the size and message that
#     will be printed on a shirt"""
#     print("The size of the shirt is " + size.title())
#     print("On the shirt the message will be '" + message +"'.")

# make_shirt('Just do it', 'large')
# make_shirt(message="Just do it", size='medium')

def describe_city(city, country='England'):
    """Accepts the name and country of a city
    and prints it out in a message."""
    output = print(city + " is in " + country + ".")
    return output

describe_city('London')
describe_city('Bangkok', 'Thailand')
describe_city(city='Genoa', country='Italy')
