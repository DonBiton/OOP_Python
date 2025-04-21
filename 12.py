#1
# class DefenderVector:
#     def __init__(self, v):
#         self.__v = v  # Оригинальный список

#     def __enter__(self):
#         self.__temp = self.__v[:]  # Создаем копию
#         return self.__temp

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.__v[:] = self.__temp
#         return False
    

#2 
def find_elements_by_index(values, indices):
    result = []
    try:
        for index in indices:
            result.append(values[index])
        return result
    except IndexError as e:
        return f"Ошибка индекса: {e}"
    
values = [10, 20, 30, 40, 50]
indices = [1, 3, 5]

print(find_elements_by_index(values, indices))

#3 
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * self.radius ** 2
try:
    c = input("Введите радиус: ")
    c = Circle(c)
except TypeError:
    print("Радиус должен быт числом")
print(c)
    
#4 
class Employee:
    def __init__(self):
        self._employees = []

    def add_employee(self, name, salary):
        self._employees.append({"name": name, "salary": salary})

    @property
    def average_salary(self):
        total_salary = sum(emp["salary"] for emp in self._employees)
        return total_salary / len(self._employees) if self._employees else 0

    def get_sorted_employees(self):
        return sorted(self._employees, key=lambda emp: emp["salary"])
try:
    company = Employee()
    company.add_employee("Alice", 50000)
    company.add_employee("Bob", 60000)
    company.add_employee("Charlie", 55000) 
except TypeError:
    print("Зарплата должна быть числом")


print("Средняя зарплата:", company.average_salary)

print("Сотрудники по зарплате:")
for emp in company.get_sorted_employees():
    print(f"{emp['name']}: {emp['salary']}")