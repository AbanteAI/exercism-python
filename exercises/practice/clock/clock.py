class Clock:
        self.hour = hour
        self.minute = minute
        pass

        return f"Clock({self.hour:02d}, {self.minute:02d})"

        return f"{self.hour:02d}:{self.minute:02d}"

        return self.total_minutes == other.total_minutes

        self.total_minutes += minutes
        self.total_minutes %= 24 * 60
        return self

        self.total_minutes -= minutes
        self.total_minutes %= 24 * 60
        return self
