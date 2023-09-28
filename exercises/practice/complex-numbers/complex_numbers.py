class ComplexNumber:
    def __init__(self, real, imaginary):
        pass

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if isinstance(other, int):
            real = self.real + other
            imaginary = self.imaginary
        else:
            real = self.real + other.real
            imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)
    def __sub__(self, other):
        if isinstance(other, int):
            real = self.real - other
            imaginary = self.imaginary
        else:
            real = self.real - other.real
            imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        if isinstance(other, int):
            denominator = other
            real = self.real / denominator
            imaginary = self.imaginary / denominator
        else:
            denominator = other.real ** 2 + other.imaginary ** 2

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        import math
        real = math.exp(self.real) * math.cos(self.imaginary)
        imaginary = math.exp(self.real) * math.sin(self.imaginary)
        return ComplexNumber(real, imaginary)