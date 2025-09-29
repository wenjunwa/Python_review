# multiple inheritance = inherit from more than one parent class
#                       C(A, B)
# multilevel inheritance  = inherit from a parent which inherits from another parent
#                       C(B) <- B(A) <- A
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing.")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Harry")
hawk = Hawk("Hawky")
fish = Fish("Nemo")

print(f"{rabbit.name}")
rabbit.eat()