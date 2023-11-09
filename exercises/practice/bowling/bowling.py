class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins")
        if self.current_roll >= 20 and not (self.current_roll == 20 and self.rolls[-1] == 10) and not (self.current_roll == 21 and self.rolls[-2] == 10 and self.rolls[-1] < 10):
            raise IndexError("Cannot roll after game is over")
        if self.current_roll > 0 and self.rolls[-1] != 10 and self.rolls[-1] + pins > 10:
            raise ValueError("Pin count exceeds pins on the lane")
        self.rolls.append(pins)
        if pins == 10 and self.current_roll < 18:
            self.rolls.append(0)
        self.current_roll += 1
        if self.current_roll == 20 and self.rolls[-2] + self.rolls[-1] < 10:
            self.current_roll += 1

    def score(self):
        if self.current_roll < 20 or (self.current_roll == 20 and self.rolls[-2] + self.rolls[-1] == 10):
            raise IndexError("Score cannot be taken until the end of the game")
        score = 0
        roll_index = 0
        for frame in range(10):
            if self.rolls[roll_index] == 10:
                score += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1
            elif self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:
                score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            else:
                score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2
        return score