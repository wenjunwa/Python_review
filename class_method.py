# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself

# Instance methods = Best for operations on instance of the class(object)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data of require access to class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # class method
    @classmethod
    def get_count(cls):
        return f"The total # of student: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The class average GPA: {cls.total_gpa / cls.count:.2f}"

print(Student.get_count())
print(Student.get_average_gpa())
student1 = Student("Sally", 3.6)
student2 = Student("Jimmy", 3)

print(student2.get_info())
print(student1.get_info())
print(Student.get_count())
print(Student.get_average_gpa())
