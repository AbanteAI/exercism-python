class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real, imaginary)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        r = math.exp(self.real)
        real = r * math.cos(self.imaginary)
        imaginary = r * math.sin(self.imaginary)
        return ComplexNumber(real, imaginary)