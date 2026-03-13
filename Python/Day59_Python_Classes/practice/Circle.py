class Circle:
    pi = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return Circle.pi * (self.radius ** 2)

c = Circle(5)
print(f"Area of circle (r=5): {c.area()}")