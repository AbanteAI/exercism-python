class SpaceAge:
    def __init__(self, seconds):
        pass
    EARTH_YEAR_SECONDS = 31557600
    MERCURY = 0.2408467
    VENUS = 0.61519726
    EARTH = 1.0
    MARS = 1.8808158
    JUPITER = 11.862615
    SATURN = 29.447498
    URANUS = 84.016846
    NEPTUNE = 164.79132

    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return round(self.seconds / (self.EARTH_YEAR_SECONDS * self.MERCURY), 2)

    def on_venus(self):
        return round(self.seconds / (self.EARTH_YEAR_SECONDS * self.VENUS), 2)

    def on_earth(self):
        return round(self.seconds / (self.EARTH_YEAR_SECONDS * self.EARTH), 2)

    def on_mars(self):
        return round(self.seconds / (self.EARTH_YEAR_SECONDS * self.MARS), 2)

    def on_jupiter(self):
        return round(self.seconds / (self.EARTH_YEAR_SECONDS * self.JUPITER), 2)

    def on_saturn(self):
        return round(self.seconds / (self.EARTH_YEAR_SECONDS * self.SATURN), 2)

    def on_uranus(self):
        return round(self.seconds / (self.EARTH_YEAR_SECONDS * self.URANUS), 2)

    def on_neptune(self):
        return round(self.seconds / (self.EARTH_YEAR_SECONDS * self.NEPTUNE), 2)
