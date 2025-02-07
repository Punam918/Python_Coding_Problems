'''4. create a base class called Shape and then create child classes like Circle and Rectangle.
Implement methods for calculating area and perimeter, and show how inheritance can be used
effectively.'''

import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius    
    def area(self):
        return math.pi * self.radius ** 2    
    def perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width    
    def area(self):
        return self.length * self.width    
    def perimeter(self):
        return 2 * (self.length + self.width)
circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

