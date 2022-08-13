from restaurant import Restaurant
from user_module import User
from admin_module import Privileges, Admin

restaurant_1 = Restaurant('the anchor', 'gatro pub')
# restaurant_1.describe_restaurant()

user_1 = Admin('tom', 'bellmont', 20534)

user_1.privileges.show_privileges()