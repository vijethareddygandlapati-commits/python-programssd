class Shape:
    def __init__(self, color):
        self.color = color
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
# Object creation
circle1 = Circle("Red", 5)
rectangle1 = Rectangle("Blue", 4, 6)
print("Circle area:", circle1.area())
print("Rectangle area:", rectangle1.area())
