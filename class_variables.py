# class variables = shared among all instances of a class
#                   Define outside the constructor
#                   Allow you to share data among all objects created from that class
#                   def __init__(self, X, Y), "self" refer to the object we currently work on
from ast import Suite


class Student:
    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
print(Student.num_students)
student2 = Student("Patrick", 35)
print(Student.num_students)
student3 = Student("Sandy", 27)
print(Student.num_students)

students =(student1, student2, student3)
for student in students:
    print(student.name, end=" ")
    print(student.age,end=" ")
    print(student.class_year, end= " ")
    print()

