from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        # Проверка целых чисел
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")
        
        # Приводим дробь к наименьшим целым числам
        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor
        
        # Если знаменатель отрицательный, переносим знак в числитель
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        # Сложение дробей
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        # Вычитание дробей
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        # Умножение дробей
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        # Деление дробей
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    @property
    def value(self):
        # Получаем точное значение дроби
        return round(self.numerator / self.denominator, 3)

    @staticmethod
    def from_string(fraction_str):
        # Статический метод для создания дроби из строки вида "a/b"
        numerator, denominator = map(int, fraction_str.split("/"))
        return Fraction(numerator, denominator)

    @classmethod
    def one(cls):
        # Класс-метод для создания дроби 1/1
        return cls(1, 1)




class FractionMatrix:
    def __init__(self, matrix):
        if not all(isinstance(row, list) and len(row) == len(matrix[0]) for row in matrix):
            raise ValueError("All rows must have the same length")
        if not all(isinstance(fraction, Fraction) for row in matrix for fraction in row):
            raise TypeError("All elements must be instances of the Fraction class")
        self.matrix = matrix
    
    def __str__(self):
        return "\n".join(" ".join(str(fraction) for fraction in row) for row in self.matrix)
    
    def __add__(self, other):
        if not isinstance(other, FractionMatrix):
            return NotImplemented
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must have the same dimensions")
        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return FractionMatrix(result)

    def __sub__(self, other):
        if not isinstance(other, FractionMatrix):
            return NotImplemented
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must have the same dimensions")
        result = [
            [self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return FractionMatrix(result)

    def __mul__(self, other):
        if not isinstance(other, FractionMatrix):
            return NotImplemented
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Number of columns of the first matrix must equal number of rows of the second matrix")
        
        result = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                for j in range(len(other.matrix[0]))
            ]
            for i in range(len(self.matrix))
        ]
        return FractionMatrix(result)

    def transpose(self):
        result = [
            [self.matrix[j][i] for j in range(len(self.matrix))]
            for i in range(len(self.matrix[0]))
        ]
        return FractionMatrix(result)

    @property
    def determinant(self):
        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError("Matrix must be square")
        
        # Определитель для 2x2 матрицы
        if len(self.matrix) == 2:
            a, b = self.matrix[0]
            c, d = self.matrix[1]
            return a * d - b * c
        
        # Для более крупных матриц вычисление детерминанта не реализовано в этом примере.
        raise NotImplementedError("Determinant calculation is only implemented for 2x2 matrices.")

    @staticmethod
    def identity(size):
        # Статический метод для создания единичной матрицы
        return FractionMatrix([[Fraction(1, 1) if i == j else Fraction(0, 1) for j in range(size)] for i in range(size)])



m1 = FractionMatrix([
    [Fraction(1, 2), Fraction(1, 3)],
    [Fraction(2, 5), Fraction(3, 4)]
])
m2 = FractionMatrix([
    [Fraction(1, 3), Fraction(2, 3)],
    [Fraction(1, 2), Fraction(2, 5)]
])

print(m1 + m2)  # Сложение матриц

print(m1.transpose())  # Транспонирование матрицы
print(m1.determinant)  # Определитель

# Создание единичной матрицы 2x2
identity_matrix = FractionMatrix.identity(2)
print(identity_matrix)
