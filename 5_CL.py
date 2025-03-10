import math
class Fraction:
    
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
    
    def __setattr__(self, key, value):
        # Проверка, чтобы знаменатель не равен 0
        if key == 'denominator' and value == 0:
            raise AttributeError("Знаменатель не должен быть равен 0")
        if type(value) != int:
            raise AttributeError("Все числа при вводе должны быть целыми")
        if key not in ('denominator', 'numerator'):
            raise AttributeError("Local attributes are not allowed")        
        super().__setattr__(key, value)
        
    def __str__(self):  # Для print()
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        # if new_numerator % new_denominator == 0:

        return Fraction(new_numerator, new_denominator)        
        
         
        
    # def exact_value(self):

    def __mul__(self, other): #Умножение
        
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)  
    def __truediv__(self, other): #Деление  
          return Fraction(self.numerator * other.denominator, self.denominator * other.numuretor)  

f1 = Fraction(2, 2)
f2 = Fraction(3, 4)   
print(f1)
print(f2)
print(f1 * f2) 

