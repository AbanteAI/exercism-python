class ComplexNumber:
    def __init__(self, real, imaginary):
        pass

    def __eq__(self, other):
        pass

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)
        pass

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)
        pass

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)
        pass

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real, imaginary)
        pass

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5
        pass

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)
        pass

    def exp(self):
        def exp(self):
            import math
            real = math.exp(self.real) * math.cos(self.imaginary)
            imaginary = math.exp(self.real) * math.sin(self.imaginary)
            return ComplexNumber(real, imaginary)
