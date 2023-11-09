from math import gcd, pow

class Rational:
    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError("Denominator cannot be zero.")
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
            raise ValueError("Cannot divide by zero.")
        new_numer = self.numer * other.denom
        new_denom = self.denom * other.numer
        return Rational(new_numer, new_denom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if isinstance(power, int):
            if power >= 0:
                new_numer = pow(self.numer, power)
                new_denom = pow(self.denom, power)
            else:
                new_numer = pow(self.denom, -power)
                new_denom = pow(self.numer, -power)
            return Rational(new_numer, new_denom)
        else:
            # For real (floating-point) powers, return a float
            return pow(float(self.numer), power) / pow(float(self.denom), power)

    def __rpow__(self, base):
        return pow(base, self.numer / self.denom)
