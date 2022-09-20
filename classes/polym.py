
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * (self.x + self.y)
    
class Square(Shape):
    def __init__(self, x):
        super().__init__(x, x)
        
    def area(self):
        return self.x * self.x
    
    def perimeter(self):
        return 4 * self.x
    
class Circle(Shape):
    def __init__(self, x):
        super().__init__(x, x)
        
    def area(self):
        return 3.14 * self.x * self.x
    
    def perimeter(self):
        return 2 * 3.14 * self.x
    
class Triangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def area(self):
        return 0.5 * self.x * self.y
    
    def perimeter(self):
        return self.x + self.y + self.x
    
# polymorphism is the ability to use the same interface for different forms (data types)