class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

        if isinstance(other, int):
            return ComplexNumber(self.real + other, self.imaginary)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    def __radd__(self, other):
        return self.__add__(other)

        if isinstance(other, int):
            return ComplexNumber(self.real * other, self.imaginary * other)
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)
    def __rsub__(self, other):
        return ComplexNumber(other - self.real, -self.imaginary)

        if isinstance(other, int):
            return ComplexNumber(self.real - other, self.imaginary)
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

        if isinstance(other, int):
            return ComplexNumber(self.real / other, self.imaginary / other)
        denominator = other.real**2 + other.imaginary**2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real, imaginary)
    def __rmul__(self, other):
        return self.__mul__(other)

    def __abs__(self):
        return (self.real**2 + self.imaginary**2)**0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        import math
        real = math.exp(self.real) * math.cos(self.imaginary)
        imaginary = math.exp(self.real) * math.sin(self.imaginary)
        return ComplexNumber(real, imaginary)

    def __rtruediv__(self, other):
        return ComplexNumber(other, 0).__truediv__(self)