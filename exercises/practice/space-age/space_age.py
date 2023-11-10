from decimal import Decimal, ROUND_HALF_UP
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_year_in_seconds = 31557600

    def on_earth(self):
        return float(Decimal(self.seconds / self.earth_year_in_seconds).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))

    def on_mercury(self):
        return float(Decimal(self.on_earth() / 0.2408467).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))

    def on_venus(self):
        return float(Decimal(self.on_earth() / 0.61519726).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))

    def on_mars(self):
        return float(Decimal(self.on_earth() / 1.8808158).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))

    def on_jupiter(self):
        return float(Decimal(self.on_earth() / 11.862615).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))

    def on_saturn(self):
        return float(Decimal(self.on_earth() / 29.447498).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))

    def on_uranus(self):
        return float(Decimal(self.on_earth() / 84.016846).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))

    def on_neptune(self):
        return float(Decimal(self.on_earth() / 164.79132).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))
