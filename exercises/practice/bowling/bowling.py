class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")
        if len(self.rolls) < 18 and len(self.rolls) % 2 == 1 and self.rolls[-1] + pins > 10:
            raise ValueError("Frame score cannot exceed 10")
        if len(self.rolls) >= 21:
            raise ValueError("Cannot roll after the 10th frame")
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        roll_index = 0

        for frame in range(10):
            if self.rolls[roll_index] == 10:  # Strike
                total_score += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1
            elif self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:  # Spare
                total_score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            else:  # Open frame
                total_score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2

        return total_score
