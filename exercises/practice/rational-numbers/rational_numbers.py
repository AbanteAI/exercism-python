class Rational:
from math import gcd

def __init__(self, numer, denom):
    if denom == 0:
        raise ValueError("Denominator cannot be zero")
    common_divisor = gcd(numer, denom)
    self.numer = numer // common_divisor
    self.denom = denom // common_divisor
    if self.denom < 0:
        self.numer = -self.numer
        self.denom = -self.denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other):
        if other.numer == 0:
            raise ValueError("Cannot divide by zero")
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return Rational(numer, denom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power >= 0:
            return Rational(self.numer ** power, self.denom ** power)
        else:
            return Rational(self.denom ** abs(power), self.numer ** abs(power))

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)
