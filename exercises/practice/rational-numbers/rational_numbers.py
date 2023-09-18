from math import gcd
class Rational:
    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError("Denominator cannot be zero")
        divisor = gcd(numer, denom)
        self.numer = numer // divisor
        self.denom = denom // divisor
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
            numer = self.numer ** power
            denom = self.denom ** power
        else:
            numer = self.denom ** abs(power)
            denom = self.numer ** abs(power)
        return Rational(numer, denom)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)
