class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        earth_years = self.seconds / 31557600
        return round(earth_years, 2)