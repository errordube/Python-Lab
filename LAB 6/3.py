class Circle():
    def __init__(self,r):
        self.radius = r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*3.14*self.radius
new = Circle(8)
print(new.area())
print(new.perimeter())
        
