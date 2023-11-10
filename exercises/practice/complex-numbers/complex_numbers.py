import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imaginary)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denominator = other.real**2 + other.imaginary**2
            real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
            imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
            return ComplexNumber(real_part, imaginary_part)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real / other, self.imaginary / other)
        else:
            return NotImplemented

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        a = self.real
        b = self.imaginary
        real_part = math.exp(a) * math.cos(b)
        imaginary_part = math.exp(a) * math.sin(b)
        return ComplexNumber(real_part, imaginary_part)
