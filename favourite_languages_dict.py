# favourite_languages = {
#     'bob': 'c',
#     'jenny': 'java',
#     'brooke': 'sql',
#     'philip': 'c'
# }

# print("Jenny's favourite language is " + 
#     favourite_languages['jenny'].title() + 
#     "."
#     )

# for name, language in favourite_languages.items():
#     print(name.title() + "'s favourite language is " +
#         language.title() + ".")

# friends = ['bob','philip']

# for name in favourite_languages.keys():
#     print(name.title())

#     if name in friends:
#         print(" Hi " + name.title() +
#             ", I see your favorite language is " +
#                 favourite_languages[name].title() + "!")

# if 'erin' not in favourite_languages.keys():
#     print("Erin, please take our poll!")


# for name in sorted(favourite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll! So helpful!! lol.")

# print("The following languages have been mentioned:")
# for name in favourite_languages.values():
#     print(name.title())

# A set will remove any duplicates from a list
# for language in set(favourite_languages.values()):
#     print(language.title())

favourite_languages = {
    'bob': 'c',
    'jenny': 'java',
    'brooke': 'sql',
    'philip': 'c'
}

people = ['brooke', 'matilda', 'ben', 'jenny']

for person in people:
    if person in favourite_languages:
        print("Thanks for taking the poll, " + person.title() + "!")
    else:
        print("Hey, " + person.title() + ". Please can you take the poll!")