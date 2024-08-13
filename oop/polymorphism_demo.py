class Shape:
    def __init__(self, area):
        self.area = area
        
class Rectangle(Shape):
    def __init__(self, area, length, width):
        super().__init__(area)
        self.length = length
        self.width = width
        
class Circle(Shape):
    def __init__(self, area, radius):
        self.radius = radius