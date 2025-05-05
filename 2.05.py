import numpy as np
import scipy.stats as stats
#2
# Данные
temperature_C = np.array([
    100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
    110, 111, 112, 113, 114, 115, 116, 117, 118, 119
])
inverse_eps = np.array([
    4.16E-05, 4.29E-05, 4.45E-05, 4.57E-05, 4.93E-05,
    5.08E-05, 5.21E-05, 5.32E-05, 5.51E-05, 5.64E-05,
    5.92E-05, 6.13E-05, 6.41E-05, 6.65E-05, 6.81E-05,
    7.15E-05, 7.45E-05, 7.74E-05, 8.00E-05, 8.33E-05
])

# Линейная аппроксимация: y = kx + b, где k = 1/A
slope, intercept, r_value, p_value, std_err = stats.linregress(temperature_C, inverse_eps)

print(f"Коэффициент 1/A = {slope:.3e}")
print(f"Погрешность (стандартная) = {std_err:.3e}")


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator, FuncFormatter

# Данные
temperature_C = np.array([
    100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
    110, 111, 112, 113, 114, 115, 116, 117, 118, 119
])
inverse_eps = np.array([
    4.16E-05, 4.29E-05, 4.45E-05, 4.57E-05, 4.93E-05,
    5.08E-05, 5.21E-05, 5.32E-05, 5.51E-05, 5.64E-05,
    5.92E-05, 6.13E-05, 6.41E-05, 6.65E-05, 6.81E-05,
    7.15E-05, 7.45E-05, 7.74E-05, 8.00E-05, 8.33E-05
])

# Аппроксимация
inv_A = 2.156e-06
mean_x = np.mean(temperature_C)
mean_y = np.mean(inverse_eps)
b = mean_y - inv_A * mean_x

# Расчёт T_c (пересечение с осью X)
T_c = -b / inv_A

# Данные для линии
T_fit = np.linspace(80, temperature_C.max() + 10, 300)
inv_eps_fit = inv_A * T_fit + b

# Масштаб для оси Y: всё переводим в 10^-5
inverse_eps_scaled = inverse_eps / 1e-5
inv_eps_fit_scaled = inv_eps_fit / 1e-5
y_min = 0
y_max = inverse_eps_scaled.max()
fig, ax = plt.subplots(figsize=(11, 7.5))

# Точки и аппроксимация
ax.scatter(temperature_C, inverse_eps_scaled, color='blue', label='1/ε vs T')
ax.plot(T_fit, inv_eps_fit_scaled, color='red', linestyle='--', linewidth=2,
        label='Аппроксимация: 1/ε = (1/A)·T + b')

# Нумерация точек
for i, (x, y) in enumerate(zip(temperature_C, inverse_eps_scaled), start=21):
    ax.text(x + 0.1, y + 0.1, str(i), fontsize=6, color='black')

# Обозначение точки Tc
ax.plot(T_c, 0, 'ko')  # Точка на оси X
ax.text(T_c + 0.5, 0.4, r'$T_c$', fontsize=12, color='black')

# Сетка и деления
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.grid(which='major', linestyle='-', linewidth=0.75, alpha=0.8)
ax.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)

ax.tick_params(axis='both', which='major', length=7, width=1.2)
ax.tick_params(axis='both', which='minor', length=4, width=1)

# Деления по оси X внизу
ax.spines['bottom'].set_position(('data', y_min))
ax.spines['bottom'].set_visible(False)
ax.tick_params(axis='x', which='both', direction='out', bottom=True, top=False)

# Убираем ненужные оси
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)

# Границы
ax.set_xlim(80, temperature_C.max() + 2)
ax.set_ylim(y_min, y_max * 1.05)

# Стрелки
ax.annotate('', xy=(temperature_C.max() + 1.5, y_min), xytext=(80, y_min),
            arrowprops=dict(arrowstyle='->', color='black', linewidth=1.5),
            annotation_clip=False)
ax.annotate('', xy=(80, y_max * 1.04), xytext=(80, y_min),
            arrowprops=dict(arrowstyle='->', color='black', linewidth=1.5),
            annotation_clip=False)

# Подписи осей у концов стрелок
ax.text(temperature_C.max() + 2.9, y_min - 0.3, 'T (°C)', fontsize=12, ha='center')
ax.text(79, y_max * 1.045, r'$1/\varepsilon$  (×10$^{-5}$)', fontsize=12, va='center')

# Заголовок и легенда
ax.set_title('Рис 2. Зависимость 1/ε от T в областях T > $T_c$ ', fontsize=14)
# ax.legend()
plt.tight_layout()
plt.savefig("graph.png", dpi=600, bbox_inches='tight')
plt.show()




# df = pd.read_excel('2.08д (3В).xlsx')

# plt.figure(figsize=(28.3, 19.65))
# ax = plt.gca()

# plt.scatter(df['X'], df['Y'], color='black', s=10, zorder=3)

# plt.scatter(0.65, 520, color='black', s=10, zorder=3)

# plt.plot([0, 0.65], [520, 520], 
#          color='black', 
#          linewidth=1.5)

# plt.plot([0.65, 2.2], 
#          [-300*0.65 + 715, -300*2.2 + 715],
#          color='black', 
#          linewidth=1.5,
#          linestyle='-')

# plt.plot([0.65, 0.65], [0, 520], 
#          color='black', 
#          linewidth=1,
#          linestyle=':')

# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['left'].set_position('zero')
# ax.spines['bottom'].set_position('zero')

# ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, markersize=8)
# ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, markersize=8)

# ax.text(0.04, 1.02, r'$I_a$, мкА', transform=ax.transAxes, ha='right', va='bottom')
# ax.text(1.01, 0.01, r'$I_L$, А', transform=ax.transAxes, ha='left', va='top')

# ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
# ax.yaxis.set_major_locator(plt.MultipleLocator(50))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(12.5))

# plt.grid(True, linestyle='-', alpha=0.7, which='major')
# plt.grid(True, linestyle=':', alpha=0.5, which='minor')

# ax.annotate('0.65', xy=(0.65, 0), xytext=(0.67, -0.02), 
#             textcoords=ax.get_xaxis_transform(),
#             ha='center', va='top', fontsize=9)

# plt.title(r'Рис 1. Зависимость $I_a$ от $I_L$ при анодном напряжении 3В')
# plt.xlim(0, 2.25)
# plt.ylim(0, 550)
# # plt.subplots_adjust(left=0.12, right=0.95, bottom=0.15, top=0.95)

# plt.show()




#1
import matplotlib.pyplot as plt
import numpy as np

# Данные
t = [
    35, 40, 44, 47, 50, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100,
    101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120
]
C = [
    7.8, 7.8, 7.8, 7.7, 7.8, 7.8, 7.8, 7.9, 8.0, 8.2, 8.4, 8.7, 9.02, 9.5, 10.3, 11.4,
    14.3, 20.6, 29.7, 34.6, 34.0, 33.0, 31.8, 31.0, 28.7, 27.9, 27.2, 26.6, 25.7, 25.1,
    23.9, 23.1, 22.1, 21.3, 20.8, 19.8, 19.0, 18.3, 17.7, 17.0, 16.3
]

# Построение графика
fig, ax = plt.subplots(figsize=(10, 6))

# Основной график
ax.plot(t, C, marker='o', color='b', label='Ёмкость')

# Добавление минорной сетки
ax.grid(which='major', linestyle='-', linewidth=0.75)
ax.grid(which='minor', linestyle=':', linewidth=0.5)
ax.minorticks_on()

# Стрелки на концах осей
ax.annotate('', xy=(max(t) + 2, 0), xytext=(min(t), 0),
            arrowprops=dict(arrowstyle='->', color='black', linewidth=1.5),
            annotation_clip=False)

ax.annotate('', xy=(min(t), max(C) + 2), xytext=(min(t), min(C)),
            arrowprops=dict(arrowstyle='->', color='black', linewidth=1.5),
            annotation_clip=False)

# Подписи и стили
ax.set_xlabel('Температура (°C)', fontsize=12)
ax.set_ylabel('Ёмкость (nF)', fontsize=12)
ax.set_title('Зависимость ёмкости от температуры', fontsize=14)

# Легенда
ax.legend()

# Настройка графика
plt.tight_layout()

# Показать график
plt.show()
