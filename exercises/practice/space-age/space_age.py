class SpaceAge:
    def __init__(self, seconds):
        pass
        self.seconds = seconds
        self.earth_years = seconds / 31557600
        self.conversion_factors = {
            "earth": 1,
            "mercury": 0.2408467,
            "venus": 0.61519726,
            "mars": 1.8808158,
            "jupiter": 11.862615,
            "saturn": 29.447498,
            "uranus": 84.016846,
            "neptune": 164.79132,
        }

    def on_earth(self):
        return round(self.earth_years, 2)

    def on_mercury(self):
        return round(self.earth_years / self.conversion_factors["mercury"], 2)

    def on_venus(self):
        return round(self.earth_years / self.conversion_factors["venus"], 2)

    def on_mars(self):
        return round(self.earth_years / self.conversion_factors["mars"], 2)

    def on_jupiter(self):
        return round(self.earth_years / self.conversion_factors["jupiter"], 2)

    def on_saturn(self):
        return round(self.earth_years / self.conversion_factors["saturn"], 2)

    def on_uranus(self):
        return round(self.earth_years / self.conversion_factors["uranus"], 2)

    def on_neptune(self):
        return round(self.earth_years / self.conversion_factors["neptune"], 2)