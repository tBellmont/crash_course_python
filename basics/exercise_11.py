# user_names = ['admin', 'tbellz', 'st4cy123', 'infinite_orange11','bozzman666']
# admin_users = ['admin']


# if user_names:
#     for user_name in user_names:
#         if user_name in admin_users:
#             print("Hello " + user_name + " , would you like to the see the daily reports?")
#         else:
#             print("Hello " + user_name + " great to see you again today.")
#     print("Done!")
# else:
#     print("No users there that I can see?")

# current_users = ['admin', 'tbellz', 'st4cy123', 'infinite_orange11','bozzman666']
# new_users = ['yellowsn0', 'TBELLZ', 'infinite_orange11','bozzman666']

# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print("Sorry! The username: " + new_user + ", has been taken!")
#     else:
#         print("Username: " + new_user + " is available!")


ord_numbers = [1,2,3,4,5,6,7,8,9]

for ord_number in ord_numbers:
    if ord_number < 2:
        print(str(ord_number) + "st")
    elif ord_number < 3:
        print(str(ord_number) + "nd")
    elif ord_number < 4:
        print(str(ord_number) + "rd")
    else:
        print(str(ord_number) + "th")
