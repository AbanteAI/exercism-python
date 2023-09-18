class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imaginary)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real * other, self.imaginary * other)
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real / other, self.imaginary / other)
        denominator = other.real ** 2 + other.imaginary ** 2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real, imaginary)
    def __rtruediv__(self, other):
        return other * self.__truediv__(1)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        from math import exp, cos, sin
        e_to_real = exp(self.real)
        real = e_to_real * cos(self.imaginary)
        imaginary = e_to_real * sin(self.imaginary)
        return ComplexNumber(real, imaginary)
