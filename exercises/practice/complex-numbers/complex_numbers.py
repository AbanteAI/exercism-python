class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        else:
            return ComplexNumber(self.real + other, self.imaginary)
    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denominator = other.real**2 + other.imaginary**2
            real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
            imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        else:
            real = self.real / other
            imaginary = self.imaginary / other
        return ComplexNumber(real, imaginary)
    def __rtruediv__(self, other):
        if isinstance(other, ComplexNumber):
            return self.__truediv__(other)
        else:
            return ComplexNumber(other) / self

    def __abs__(self):
        return (self.real**2 + self.imaginary**2)**0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        import math
        real = math.exp(self.real) * math.cos(self.imaginary)
        imaginary = math.exp(self.real) * math.sin(self.imaginary)
        return ComplexNumber(real, imaginary)
