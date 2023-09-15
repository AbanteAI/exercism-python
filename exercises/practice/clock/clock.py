class Clock:
    def __init__(self, hour, minute):
        self.hour = hour % 24
        self.minute = minute % 60
        self.hour += minute // 60
        self.hour %= 24

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        total_minutes = self.hour * 60 + self.minute + minutes
        return Clock(total_minutes // 60, total_minutes % 60)

    def __sub__(self, minutes):
        total_minutes = self.hour * 60 + self.minute - minutes
        return Clock(total_minutes // 60, total_minutes % 60)
