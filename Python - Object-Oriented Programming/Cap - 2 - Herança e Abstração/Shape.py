from abc import ABC, abstractmethod
import math


class Shape:
    def __init__(self, color):
        self.color = color
        
    def __str__(self):
        return f"{self.color}"
    
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        
    def __str__(self):
        return f"Cor: {super().__str__()}, Raio: {self.radius}"
    
    def area(self):
        area_circle = math.pi * (self.radius ** 2)
        return area_circle
    
    
class Rectangle(Shape):
    def __init__(self, color,  width, height):
        super().__init__(color)
        self.width = width
        self.height = height
       
    def __str__(self):
        return f"Cor: {super().__str__()}, Largura: {self.width}, Altura: {self.height}"
       
    def area(self):
        area_rectangle = self.width * self.height
        return area_rectangle

