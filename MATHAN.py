# import matplotlib
# from sympy import symbols, Eq, expand, solve

# # Определим переменные
# x, A, B, C, D = symbols('x A B C D')

# # Разложим выражение на простые дроби
# lhs = 5*x**3 + 4*x**2 - 6*x
# rhs = A*(x+2)*(x-4)*(x+1) + B*(x-4)*(x+1) + C*(x+2)**2*(x+1) + D*(x+2)**2*(x-4)

# # Раскроем скобки
# rhs_expanded = expand(rhs)

# # Составим систему уравнений, приравняв коэффициенты при одинаковых степенях x
# equations = [Eq(rhs_expanded.coeff(x, i), lhs.coeff(x, i)) for i in range(4)]

# # Решим систему уравнений
# solution = solve(equations, [A, B, C, D])
# print(solution)
# import numpy as np

# # Коэффициенты системы уравнений
# # A + B + C = 1
# # -3A - 2B - C + D = 0
# # 7A + 5B - D = 0
# # -5A = -5
# A, B, C, D = 1, -1, 1, 2  # Начальные значения для проверки

# # Формируем матрицу коэффициентов системы
# A_matrix = np.array([
#     [1, 1, 1, 0],
#     [-3, -2, -1, 1],
#     [7, 5, 0, -1],
#     [-5, 0, 0, 0]
# ])

# # Формируем вектор правых частей
# B_vector = np.array([1, 0, 0, -5])

# # Решаем систему уравнений
# solution = np.linalg.solve(A_matrix, B_vector)

# # Выводим результат
# print("Решение системы:")
# print(f"A = {solution[0]}, B = {solution[1]}, C = {solution[2]}, D = {solution[3]}")
from sympy import symbols, Eq, solve

# Объявляем переменные для коэффициентов A, B, C, D
x, A, B, C, D = symbols('x A B C D')

# Левая часть (числитель)
numerator = 2*x**3 + (9/4)*x**2 + (1/4)*x - 4

# Правая часть (разложение)
rhs = A/(x) + B/(x+1) + (C*x + D)/(x**2 + 2)

# Умножаем обе части на общий знаменатель (x^2 + 2) * x * (x + 1)
rhs_multiplied = rhs * (x**2 + 2) * x * (x + 1)

# Упрощаем правую часть
rhs_expanded = rhs_multiplied.expand()

# Разворачиваем и упрощаем левую часть
lhs_expanded = numerator

# Теперь приравниваем обе части и получаем систему уравнений
equation = Eq(lhs_expanded, rhs_expanded)

# Решаем систему для A, B, C, D
solution = solve(equation, (A, B, C, D))

# Выводим решение
print("Решение системы для коэффициентов A, B, C, D:")
for var, value in solution.items():
    print(f"{var} = {value}")

from sympy import symbols, Eq, solve

# Объявляем переменные
x, A, B, C, D = symbols('x A B C D')

# Левая часть (числитель)
numerator = 2*x**3 + (9/4)*x**2 + (1/4)*x - 4

# Правая часть (разложение)
rhs = A/(x) + B/(x+1) + (C*x + D)/(x**2 + 2)

# Умножаем обе части на общий знаменатель (x^2 + 2) * x * (x + 1)
rhs_multiplied = rhs * (x**2 + 2) * x * (x + 1)

# Упрощаем правую часть
rhs_expanded = rhs_multiplied.expand()

# Разворачиваем и упрощаем левую часть
lhs_expanded = numerator

# Теперь приравниваем обе части и получаем систему уравнений
equation = Eq(lhs_expanded, rhs_expanded)

# Решаем систему для A, B, C, D
solution = solve(equation, (A, B, C, D))

# Выводим решение
print("Решение системы для коэффициентов A, B, C, D:")
for var, value in solution.items():
    print(f"{var} = {value}")
