# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)

#empty list append
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

#insert into list
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')
# print(motorcycles)

#delete from list
# motorcycles = ['honda', 'yamaha', 'suzuki']
# del motorcycles[1]
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']

# last_owned = motorcycles.pop(1)
# print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)

too_cheap = 'yamaha'
motorcycles.remove(too_cheap)
print(motorcycles)
print(f"\nA {too_cheap.title()} is too cheap for me.")