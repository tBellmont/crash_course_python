# Slicing a List
players = ['tom','bill','paula','rita','xavier']

# Whole list
print(players)

# 1st until the 4th (1,2,3)
print(players[0:3])

# 3rd until the 5th (3,4)
print(players[2:4])

# Start until the 4th (1,2,3)
print(players[:3])

# 4th until the end (1,2,3)
print(players[3:])

# Last 3
print(players[-3:])

# Looping through a slice

print("Here are the first three players on my team!! LOL")
for player in players[:3]:
    print(player.title())
