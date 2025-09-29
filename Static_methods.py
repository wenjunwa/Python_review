# Static methods = A method that belong to a class rather than any object from that class(instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        positions = ["Manager", "Casher", "Cook", "Janitor"]
        return position in positions

employee1 = Employee("Spongebob", "Cook")
employee2 = Employee("Squidward", "Casher")
employee3 = Employee("Eugune", "Manager")
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(Employee.is_valid_position("Scientist"))



