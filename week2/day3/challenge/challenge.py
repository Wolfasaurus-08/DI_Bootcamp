import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self._radius = radius
        elif diameter is not None:
            self._radius = diameter / 2
        else:
            raise ValueError("A radius or diameter must be provided.")
    
    def get_radius(self):
        return self._radius
    
    def get_diameter(self):
        return self._radius * 2
    
    def get_area(self):
        return math.pi * (self._radius ** 2)
    
    def __str__(self):
        return f"Circle(radius={self.get_radius()}, diameter={self.get_diameter()}, area={self.get_area():.2f})"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.get_radius() + other.get_radius())
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.get_radius() < other.get_radius()
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.get_radius() == other.get_radius()
        return NotImplemented
    
    def __repr__(self):
        return f"Circle(radius={self.get_radius()})"

# Examples
circle1 = Circle(radius=5)
circle2 = Circle(diameter=20)
print(circle1)
print(circle2) 
circle3 = circle1 + circle2
print(circle3) 
print(circle1 < circle2)  
print(circle1 == circle2)  
circles = [circle1, circle2, circle3]
sorted_circles = sorted(circles)
print(sorted_circles) 