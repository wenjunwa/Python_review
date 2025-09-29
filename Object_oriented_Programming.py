# object = A "bundle" of related attributes (variable) and methods (function)
#          ex. phone, cup, book
#          Yor need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object
from car import Car
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("charger", 2026, "yellow", True)
cars = (car1, car2, car3)

for car in cars:
    car.describe()
    car.drive()
    car.stop()

