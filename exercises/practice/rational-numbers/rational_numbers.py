from math import gcd

class Rational:
    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError("Denominator cannot be zero")
        self.numer = numer
        self.denom = denom
        self.reduce()

    def reduce(self):
        common_divisor = gcd(self.numer, self.denom)
        self.numer //= common_divisor
        self.denom //= common_divisor
        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __sub__(self, other):
        new_numer = self.numer * other.denom - other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __mul__(self, other):
        new_numer = self.numer * other.numer
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __truediv__(self, other):
        if other.numer == 0:
            raise ValueError("Cannot divide by zero")
        new_numer = self.numer * other.denom
        new_denom = self.denom * other.numer
        return Rational(new_numer, new_denom)

    def __abs__(self):
        new_numer = abs(self.numer)
        new_denom = abs(self.denom)
        return Rational(new_numer, new_denom)

    def __pow__(self, power):
        if not isinstance(power, int):
            raise ValueError("Power must be an integer")
        new_numer = self.numer ** power
        new_denom = self.denom ** power
        return Rational(new_numer, new_denom)

    def __rpow__(self, base):
        if self.numer < 0 and self.denom % 2 == 0:
            raise ValueError("Cannot calculate negative base to even root")
        return base ** (self.numer / self.denom)