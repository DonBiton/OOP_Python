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
        print('Метод __add__ отрабатывает...')
        # s1    = other
        s1 = self.numerator
        print(s1)   
        
    # def exact_value(self):

    def __mul__(self, other):
        s1 = self.numerator
        return Fraction(self.numerator *self.numerator, self.denominator)        

f1 = Fraction(2, 2)
f2 = Fraction(3, 4)   
print(f1)
print(f2)
print(f1 * f2) 
