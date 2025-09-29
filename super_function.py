# super() = Function used in a child class to call methods from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"its {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with area of {3.14 * (self.radius ** 2)} cm^2.")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with area of {self.width ** 2} cm^2.")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

        print(f"It is a triangle with area of {self.width * self.height / 2} cm^2.")
        super().describe()

circle = Circle(color="red", is_filled="True", radius=5)

print(f"Color is {circle.color}")
print(f"Filling is {circle.is_filled}")
print(f"radius is {circle.radius}")
circle.describe()