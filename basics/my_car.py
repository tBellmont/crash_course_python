from car import Car
from electric_car import ElectricCar

my_new_car = Car('VW', 'polo', 2006)
print(my_new_car.get_descriptive_name())

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())