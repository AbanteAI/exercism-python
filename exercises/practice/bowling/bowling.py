class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins: Pins must be between 0 and 10.")
        if len(self.rolls) >= 21:
            raise Exception("Cannot roll after the game is over.")
        if len(self.rolls) >= 19 and sum(self.rolls[-2:]) < 10 and len(self.rolls) % 2 == 1:
            raise Exception("Cannot roll after the game is over.")
        if len(self.rolls) % 2 == 1 and self.rolls[-1] + pins > 10 and len(self.rolls) < 19:
            raise ValueError("Invalid number of pins: Frame score cannot exceed 10.")
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        frame_index = 0

        for frame in range(10):
            if self.is_strike(frame_index):
                total_score += 10 + self.strike_bonus(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                total_score += 10 + self.spare_bonus(frame_index)
                frame_index += 2
            else:
                total_score += self.frame_score(frame_index)
                frame_index += 2

        return total_score

    def is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def frame_score(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]