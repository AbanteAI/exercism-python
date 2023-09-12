from math import gcd
class Rational:
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

        return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)
        pass

        return Rational(self.numer * other.numer, self.denom * other.denom)
        pass

        return Rational(self.numer * other.denom, self.denom * other.numer)
        pass

        return Rational(abs(self.numer), abs(self.denom))
        pass

        return Rational(self.numer ** power, self.denom ** power)
        pass

        return base ** (self.numer / self.denom)
        pass
