import math

class ComplexNumber:

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.imaginary * other.real + self.real * other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) / denominator,
                             (self.imaginary * other.real - self.real * other.imaginary) / denominator)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        a = self.real
        b = self.imaginary
        return ComplexNumber(math.exp(a) * math.cos(b), math.exp(a) * math.sin(b))
