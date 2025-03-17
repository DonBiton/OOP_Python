#1 Класс "Настройки с валидацией"
class Settings:
    def __init__(self,max_users):
        self.max_users = max_users

    @property
    def max_users(self):
        return self._max_users
    
    @max_users.setter
    def max_users(self, value):
        if not isinstance(value, int) or value <= 0:
            raise TypeError("max_users должно быть целым числом > 0")
        self._max_users = value 
        print("ОК")


s = Settings(5)  # OK  
print(s.max_users)
# s.max_users = -3  # ValueError  
# s = Settings(0)   # ValueError  

#2  Класс "Денежная сумма"
class Money:
    def __init__(self, money):
        if not isinstance(money, int or float):
            raise TypeError("Int или Float сюда принимаются")
        self.money = money
    def __add__(self, other):
        return (self.money + other)   
    def __radd__(self, other):
        return (other + self.money ) 

m = Money(100)  
print(m + 50)  # Money(150)  
print(50 + m)  # Money(150)  
# m + "50"  # TypeError  
# Money("100")  # TypeError  