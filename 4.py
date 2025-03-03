#2

from pyclbr import Class


class Counter:
    value = 0

    def __init__(self):
        self._attributes = {}  # Словарь для хранения атрибутов

    def __getattr__(self, item):
        # print("Доступ к атрибуту " + item)
        return print(("Нет доступа к атрибуту " + item))
c = Counter()
c.value = 5         # Атрибут value будет добавлен
print(c.value)      # Доступ к атрибуту value → 5
print(c.name)       # Доступ к атрибуту name → None

#3
class Car:
    def __init__(self, make = '', mark = ''):
        self.make = make
        self.mark = mark
    def __getattr__(self, item):
        # Если атрибут не найден, возвращаем соответствующее сообщение
        return "This attribute is not available"
                

c = Car("Toyota", "Corolla")
print(c.make)      # Toyota
print(c.color)     # This attribute is not available

#4
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        # Проверка, чтобы запр созд н лок атр
        if key not in ('width', 'height'):
            raise AttributeError("Local attributes are not allowed")


r = Rectangle(10, 20)
r.width = 15  # Успешно
r.height = 25 # Успешно
r.color = 'red'  # AttributeError: Local attributes are not allowed
