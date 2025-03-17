import numpy as np
import matplotlib.pyplot as plt

class Derivative:
    """Дескриптор для вычисления производной функции."""
    
    def __init__(self, h=1e-5):
        self.h = h

    def __get__(self, instance, owner):
        """Возвращает функцию для вычисления производной в точке x."""
        if instance is None:
            return self
        
        h = self.h
        def derivative_func(x):
            return (instance(x + h) - instance(x - h)) / (2 * h)
        return derivative_func

class ExponentialFunction:
    """Класс для представления функции f(x) = a * e^x."""
    
    derivative = Derivative()  # Дескриптор для вычисления производной

    def __init__(self, a):
        self.a = a

    def __call__(self, x):
        """Возвращает значение функции в точке x."""
        return self.a * np.exp(x)

    def plot(self):
        """Строит график функции и её производной."""
        x = np.linspace(-2, 2, 400)
        y = self(x)
        dy = self.derivative(x)  # Вызов через дескриптор
        
        plt.figure()
        plt.plot(x, y, label=f'f(x) = {self.a}⋅eˣ')
        plt.plot(x, dy, '--', label=f"f'(x)")
        plt.xlabel('x')
        plt.show()
exp_func = ExponentialFunction(a=2)
print(exp_func(0))          # 2.0
print(exp_func.derivative(0))  # 2.0 (производная 2e^x в x=0)

# Построение графиков
exp_func.plot()


