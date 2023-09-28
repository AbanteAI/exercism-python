class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        if pins < 0:
            raise ValueError("Rolls cannot score negative points")
        if self.current_roll >= 20 and not (self.is_spare(18) or self.is_strike(18)):
            raise IndexError("Cannot roll if game already has ten frames")
        if self.current_roll == 21 and not self.is_strike(18):
            raise IndexError("Cannot roll after bonus roll for spare")
        if self.current_roll == 22:
            raise IndexError("Cannot roll after bonus rolls for strike")
        if self.current_roll == 21 and self.is_strike(18) and self.rolls[-2] != 10 and pins == 10:
            raise ValueError("The second bonus roll after a strike in the last frame cannot be a strike if the first one is not a strike")
        if self.current_roll == 21 and self.is_strike(18) and self.rolls[-2] + pins > 10:
            raise ValueError("Two bonus rolls after a strike in the last frame cannot score more than 10 points")
        self.rolls.append(pins)
        if pins > 10:
            raise ValueError("A roll cannot score more than 10 points")
        if self.current_roll > 21:
            raise IndexError("Cannot roll after bonus rolls")
        if self.current_roll == 21 and not (self.is_spare(18) or self.is_strike(18)):
            raise IndexError("Cannot roll after bonus roll for spare")
        if self.current_roll == 20 and self.is_strike(18) and pins > 10:
            raise ValueError("Bonus roll after a strike in the last frame cannot score more than 10 points")
        self.current_roll += 1

    def score(self):
        score = 0
        frame_index = 0
        for frame in range(10):
            if self.is_strike(frame_index):
                score += 10 + self.strike_bonus(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                score += 10 + self.spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self.frame_score(frame_index)
                frame_index += 2
        return score

    def is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def frame_score(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]
