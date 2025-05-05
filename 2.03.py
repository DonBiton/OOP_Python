import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

import numpy as np
import matplotlib.pyplot as plt

# Данные (без последней лишней точки)
delta_U_over_Uv = np.array([
    125, 128.5714286, 128, 124.2105263, 120, 119.5402299,
    119.047619, 122.5, 123.0769231, 117.3333333, 116.6666667,
    113.3333333, 104, 90
])

Uv_over_U0 = np.array([
    41.66666667, 42.85714286, 42.66666667, 41.40350877, 40, 39.8467433,
    39.68253968, 40.83333333, 41.02564103, 39.11111111, 38.88888889,
    37.77777778, 34.66666667, 30
])

# Аппроксимация линейной функцией: y = ax + b
coeffs = np.polyfit(Uv_over_U0, delta_U_over_Uv, 1)  # 1 — степень полинома
a_fit, b_fit = coeffs

# Создание массива x для линии тренда
x_fit = np.linspace(min(Uv_over_U0), max(Uv_over_U0), 100)
y_fit = a_fit * x_fit + b_fit

# Построение графика
plt.figure(figsize=(10, 6))
plt.scatter(Uv_over_U0, delta_U_over_Uv, color='blue', label='Измеренные точки')
plt.plot(x_fit, y_fit, color='red', label=f'Аппроксимация: y = {a_fit:.2f}x + {b_fit:.2f}')
plt.xlabel("Uv / U0")
plt.ylabel("ΔU / Uv")
plt.title("График зависимости ΔU/Uv от Uv/U0 с аппроксимацией")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Также выведем коэффициенты аппроксимации
print(f"Аппроксимирующая прямая: y = {a_fit:.2f}x + {b_fit:.2f}")







# Данные
a = 3.00
U0 = 3  # Вольт
e = 1.602e-19  # Кулон
S = 0.05e-6  # мм² -> м²
R1 = 100e3  # кОм -> Ом
tau_p = 0.00852381  # секунд

# Расчёт по формуле
B = (a * U0 * e * S * R1) / tau_p
print(f"B = {B:.2e} (в единицах С/с)")


# Пример: если вы знаете B и Δa
B = ...  # ваше рассчитанное значение B
a = 3.00
delta_a = 0.01

# Расчёт погрешности B
delta_B = B * (delta_a / a)
print(f"Погрешность ΔB ≈ {delta_B:.3e}")

