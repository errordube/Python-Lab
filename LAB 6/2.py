class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def area(self):
        return self.length*self.width
new = Rectangle(12,10)
print(new.area())
