import math
class Shape:
    def __init__(self):
        pass
    def area():
        raise NotImplementedError("для базового класса конкретные формулы не известны")
    def perimeter():
        raise NotImplementedError("для базового класса конкретные формулы не известны")
    @staticmethod
    def check_(something):
        if not isinstance(something, int or float):
            raise TypeError("Только Int или Float сюда принимаются")        
        if something < 0:
            raise ValueError("Числа не должны быть отрицательными") 
class Circle(Shape):
    def __init__(self, r):
            self.r =r 
            self.check_(r)
    def area(self):
        return(math.pi * self.r**2)
    def perimeter(self):
        return(2 * math.pi*self.r)
    
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a =a
        self.check_(a)
        self.b =b 
        self.check_(b)


    def area(self):
        return(self.a*self.b)
    def perimeter(self):
        return(2*(self.a+self.b))
circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

rectangle = Rectangle(5, 6)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())