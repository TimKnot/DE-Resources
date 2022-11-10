from abc import ABC, abstractmethod
from typing import List
from math import pi

class Shape(ABC):
    pass
    @abstractmethod
    def calculate_area_sqm(self) -> int:
        pass

class Rectangle(Shape):
    def __init__(self, x_meters, y_meters):
        self.x_meters = x_meters
        self.y_meters = y_meters
        
    def calculate_area_sqm(self) -> int:
        return self.x_meters * self.y_meters
    
    def is_square(self):
        return self.x_meters == self.y_meters

class Circle(Shape):
    
    def __init__(self, radius_meters):
        self.radius_meters = radius_meters
        
    def calculate_area_sqm(self) -> int:
        return pi * self.radius_meters * self.radius_meters

def print_areas(shapes: List[Shape]):
    for shape in shapes:
        print(f"{shape.calculate_area_sqm()} square meters")

c = Circle(10)
r = Rectangle(5,5)
# s = Shape() # TypeError - Can't instantiate abstract base class 

# We can call is_square on r as an instance of Rectangle, but not on C which doesn't implement it
print(r.is_square())
# print(c.is_square()) # raises AttributeError

# Circle and Rectangle act polymorhpically here as print_areas does not know what type
# of shape is actually passed in, only that it will implement calculate_area_sqm()
shapes = [c, r]
print_areas(shapes)
