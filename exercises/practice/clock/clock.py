class Clock:
    def __init__(self, hour, minute):
        self.total_minutes = (hour * 60 + minute) % (24 * 60)
        pass

    def __repr__(self):
        return f"Clock({self.total_minutes // 60}, {self.total_minutes % 60})"
        pass

    def __str__(self):
        return f"{self.total_minutes // 60:02d}:{self.total_minutes % 60:02d}"
        pass

    def __eq__(self, other):
        return self.total_minutes == other.total_minutes
        pass

    def __add__(self, minutes):
        return Clock(0, self.total_minutes + minutes)
        pass

    def __sub__(self, minutes):
        return Clock(0, self.total_minutes - minutes)
        pass
