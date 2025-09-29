# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)
from pydoc import ModuleScanner


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEAK!")


dog = Dog("Scoopy")
cat = Cat("Tom")
mouse = Mouse("Micky")

animals = (dog, cat, mouse)

for animal in animals:
    print(f"{animal.name} is {animal.is_alive}")
    animal.eat()
    animal.sleep()
    animal.speak()

