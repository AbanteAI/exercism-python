class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.hour = hour
        self.minute = minute
        pass

    def __repr__(self):
        return f"Clock({self.hour:02d}, {self.minute:02d})"
        pass

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"
        pass

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute
        pass

    def __add__(self, minutes):
        new_hour = (self.hour + (self.minute + minutes) // 60) % 24
        new_minute = (self.minute + minutes) % 60
        return Clock(new_hour, new_minute)
        new_minute = (self.minute + minutes) % 60
        return Clock(new_hour, new_minute)
        pass

    def __sub__(self, minutes):
        new_hour = (self.hour + (self.minute - minutes) // 60) % 24
        new_minute = (self.minute - minutes) % 60
        return Clock(new_hour, new_minute)
        new_minute = (self.minute - minutes) % 60
        return Clock(new_hour, new_minute)
        pass
