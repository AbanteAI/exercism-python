class Rational:
    def __init__(self, numer, denom):
        gcd = self.gcd(abs(numer), abs(denom))
        self.numer = numer // gcd
        self.denom = denom // gcd

        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)
        pass

    def __sub__(self, other):
        new_numer = self.numer * other.denom - other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)
        pass

    def __mul__(self, other):
        new_numer = self.numer * other.numer
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)
        pass

    def __truediv__(self, other):
        new_numer = self.numer * other.denom
        new_denom = self.denom * other.numer
        return Rational(new_numer, new_denom)
        pass

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))
        pass

    def __pow__(self, power):
        if power >= 0:
            new_numer = self.numer ** power
            new_denom = self.denom ** power
        else:
            new_numer = self.denom ** abs(power)
            new_denom = self.numer ** abs(power)
        return Rational(new_numer, new_denom)
        pass

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
        pass
