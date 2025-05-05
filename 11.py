#1 Конструирование классов Point2D и Point3D
# class Point2d():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
# class Point3d(Point2d):
#     __slots__ = ('_z',)
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self._z = z  # Инициализация происходит только один раз
#     @property
#     def z(self):
#         return self._z

#     @z.setter
#     def z(self, value):
#         # Запрещаем изменение атрибута z после инициализации
#         raise AttributeError("Изменение атрибута z запрещено!")
    
# pt3 = Point3d(10, 20, 30)
# print("pt3.z =", pt3.z)
# print("pt3.__slots__:", pt3.__slots__)
# print("pt3.x = ", pt3.x, "pt3.y = ", pt3.y)

# try:
#     pt3.z = 40  # Попытка изменить значение должна вызвать ошибку.
# except AttributeError as e:
#     print("Ошибка при изменении pt3.z:", e)

# # Попытка обратиться к __dict__ вызовет ошибку, т.к. у объекта нет динамического словаря.
# try:
#     print(pt3.__dict__)
# except AttributeError as e:
#     print("Ошибка при обращении к pt3.__dict__:", e)



#2 Сравнение производительности и памяти
from re import S
import timeit
import sys
class NormalPoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy        
    
class SlotPoint():
    __slots__ = ('x','y', )
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy     
a=NormalPoint(1,2)
   
print(a.__dict__)
import timeit

# Инициализация объектов
normal_points = [NormalPoint(i, i) for i in range(1000)]
slot_points = [SlotPoint(i, i) for i in range(1000)]

# Время на вызов move
normal_time = timeit.timeit(
    stmt='[p.move(1, 1) for p in normal_points]',
    globals=globals(),
    number=1000
)

slot_time = timeit.timeit(
    stmt='[p.move(1, 1) for p in slot_points]',
    globals=globals(),
    number=1000
)

print(f"NormalPoint time: {normal_time:.4f} сек")
print(f"SlotPoint time:   {slot_time:.4f} сек")


import sys

normal_sample = NormalPoint(1, 2)
slot_sample = SlotPoint(1, 2)

print(f"Размер NormalPoint: {sys.getsizeof(normal_sample)} байт")
print(f"Размер SlotPoint:   {sys.getsizeof(slot_sample)} байт")
print(f"Размер __dict__ NormalPoint: {sys.getsizeof(normal_sample.__dict__)} байт")

#3 «Студенческий журнал»
class Student:
    __slots__ = ('name', 'age', 'grade')

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student("Анна", 20, 85),
    Student("Борис", 21, 90),
    Student("Виктор", 19, 78),
    Student("Галина", 22, 92),
    Student("Дмитрий", 20, 88)
]
def average_grade(student_list):
    if not student_list:
        return 0
    total = sum(student.grade for student in student_list)
    return total / len(student_list)

avg = average_grade(students)
print(f"Средняя оценка студентов: {avg}")

#4 
class Product:
    __slots__ = ('name', 'price', 'quantity')

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


inventory = {
    "Ноутбук": Product("Ноутбук", 75000, 5),
    "Смартфон": Product("Смартфон", 45000, 10),
    "Наушники": Product("Наушники", 3000, 25),
    "Монитор": Product("Монитор", 22000, 7),
    "Клавиатура": Product("Клавиатура", 2500, 15)
}


def expensive_products(product_dict, price_threshold):
    return [name for name, product in product_dict.items() if product.price > price_threshold]

threshold = 20000
result = expensive_products(inventory, threshold)

print(f"Товары дороже {threshold} руб.: {', '.join(result)}")