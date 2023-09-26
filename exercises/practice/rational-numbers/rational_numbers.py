class Rational:
    def __init__(self, numer, denom):
        self.numer = None
        self.denom = None

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)
        pass

        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)
        pass

        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)
        pass

        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return Rational(numer, denom)
        pass

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        return Rational(numer, denom)

        numer = self.numer ** power
        denom = self.denom ** power
        return Rational(numer, denom)
        pass

        numer = self.numer ** power
        denom = self.denom ** power
        return numer / denom
        pass
        return base ** (self.numer / self.denom)