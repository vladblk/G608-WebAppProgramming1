import math


class ComplexNumbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return complex(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)

    def __truediv__(self, other):
        return complex(self.real*other.real + self.imag*other.imag, self.imag*other.real - self.real*other.imag) / other.real**2 + other.imag**2

    def __mod__(self, other):
        return complex(math.sqrt(self.real**2 + self.imag**2), 0)


C_input = input().strip().split()
D_input = input().strip().split()

C = complex(*map(float, C_input))
D = complex(*map(float, D_input))

print(C + D)
print(C - D)
print(C * D)
print(C / D)
print(C.mod())
print(D.mod())

