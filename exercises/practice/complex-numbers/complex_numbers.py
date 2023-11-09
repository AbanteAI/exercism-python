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
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.imaginary * other.real + self.real * other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denominator = other.real**2 + other.imaginary**2
            return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) / denominator,
                                 (self.imaginary * other.real - self.real * other.imaginary) / denominator)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real / other, self.imaginary / other)
        else:
            return NotImplemented

    def __abs__(self):
        return (self.real**2 + self.imaginary**2)**0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        from math import exp, cos, sin
        return ComplexNumber(exp(self.real) * cos(self.imaginary), exp(self.real) * sin(self.imaginary))
