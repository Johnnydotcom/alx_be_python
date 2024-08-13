import math
class Shape:
    def __init__(self, area):
        self.area = area
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
        
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
        
class Circle(Shape):
    def __init__(self, area, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius