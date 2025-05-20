# Abstract Classes and Methods
# _____________________________ Assignment 9 _____________________________
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

print("\n\t_____________________________ OUTPUT _____________________________")
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
# Create an instance of the Rectangle class
rectangle = Rectangle(5, 3)
# Call the area method to calculate the area of the rectangle
print(f"\n Area: {rectangle.area()}")

# In the above code, we have created an abstract class Shape with an abstract method area().
# The Rectangle class inherits from Shape and implements the area() method.
# When we create an instance of the Rectangle class and call the area() method, it calculates the area of the rectangle using the formula length * width.
# The abc module is used to create abstract classes and methods in Python.
# The abstract class Shape cannot be instantiated directly, and any class that inherits from it must implement the abstract method area().
# This ensures that all subclasses of Shape provide their own implementation of the area() method.
# This is useful for creating a common interface for different shapes while allowing each shape to define its own area calculation.