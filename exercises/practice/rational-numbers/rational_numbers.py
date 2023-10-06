class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

        if isinstance(self, Rational) and isinstance(other, Rational):
            return self.numer == other.numer and self.denom == other.denom
        return False
        return f'{self.numer}/{self.denom}'
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

        new_numer = self.numer * other.denom - other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

        new_numer = self.numer * other.numer
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

        new_numer = self.numer * other.denom
        new_denom = self.denom * other.numer
        return Rational(new_numer, new_denom)

        new_numer = abs(self.numer)
        new_denom = abs(self.denom)
        return Rational(new_numer, new_denom)

        new_numer = self.numer ** power
        new_denom = self.denom ** power
        return Rational(new_numer, new_denom)

        return base ** (self.numer / self.denom)