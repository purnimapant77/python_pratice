import math

class Circle:
    shapes_created = 0                         

    def __init__(self, radius):
        if radius <= 0:                         
            raise ValueError("radius must be positive")
        self.radius = radius
        Circle.shapes_created += 1          

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def __str__(self):
        return f"Circle(r={self.radius})"


    @staticmethod
    def cm_to_inch(cm):
        return round(cm * 0.3937, 3)

    @staticmethod
    def is_valid_dimension(val):
        return val > 0


    @classmethod
    def total_created(cls):
        return f"Circles created: {cls.shapes_created}"


class Rectangle:
    shapes_created = 0                          

    def __init__(self, width, height):
        if width <= 0 or height <= 0:         
            raise ValueError("dimensions must be positive")
        self.width = width
        self.height = height
        Rectangle.shapes_created += 1        

    
    def area(self):
        return round(self.width * self.height, 2)

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def is_square(self):
        return self.width == self.height


    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


    @staticmethod
    def cm_to_inch(cm):
        return round(cm * 0.3937, 3)

    @staticmethod
    def is_valid_dimension(val):
        return val > 0

    @classmethod
    def total_created(cls):
        return f"Rectangles created: {cls.shapes_created}"


if __name__ == "__main__":
    c1 = Circle(5)
    c2 = Circle(3)
    c3 = Circle(7)
    r1 = Rectangle(4, 6)
    r2 = Rectangle(5, 5)

    print(" __str__ ")
    print(c1)                               
    print(r1)                               

    print("\nAreas ")
    for shape in [c1, c2, c3, r1, r2]:
        print(f"{shape} → area = {shape.area()}")

    print("\n Perimeters")
    print(c1.perimeter())                  
    print(r1.perimeter())                  

    print("\n is_square ")
    print(r1.is_square())                  
    print(r2.is_square())              

    print("\n Static methods ")
    print(Circle.cm_to_inch(10))            
    print(Rectangle.is_valid_dimension(-2)) 
    print(Rectangle.is_valid_dimension(5))  

    print("\nClass methods ")
    print(Circle.total_created())           
    print(Rectangle.total_created())      
    print("\nalidation (ValueError)")
    for test in [("Circle(-3)", lambda: Circle(-3)),
                 ("Rectangle(0, 5)", lambda: Rectangle(0, 5))]:
        try:
            test[1]()
        except ValueError as e:
            print(f"  {test[0]} →  ValueError: {e}")