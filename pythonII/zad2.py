import math


class Complex:
    def __init__(self, re, im):
        self.real = re
        self.imag = im

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __abs__(self):
        return math.sqrt(pow(self.real, 2) + pow(self.imag, 2))

    def __str__(self):
        result = str(self.real)
        if self.imag < 0:
            return result + " - j" + str(abs(self.imag))
        return result + " + j" + str(self.imag)


x = Complex(3, 4)
y = Complex(0, -9)
print("x = ", x)
print("y = ", y)
print("x + y = ", x + y)
print("x - y = ", x - y)
print("abs(x) = ", abs(x))
