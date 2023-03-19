from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return f"{math.pi * self.__radius ** 2:.2f}"

    def calculate_perimeter(self):
        return f"{2 * math.pi * self.__radius:.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return f"{self.__width * self.__height:.2f}"

    def calculate_perimeter(self):
        return f"{2 * (self.__width + self.__height):.2f}"


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())