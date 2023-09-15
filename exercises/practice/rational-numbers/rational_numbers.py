class Rational:
    def __init__(self, numer, denom):
        self.numer = None
        self.denom = None
class Rational:
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def normalize(numer, denom):
    if denom < 0:
        numer, denom = -numer, -denom
    divisor = gcd(numer, denom)
    return numer // divisor, denom // divisor

class Rational:
    def __init__(self, numer, denom):
        self.numer, self.denom = normalize(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = lcm(self.denom, other.denom)
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = lcm(self.denom, other.denom)
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other):
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