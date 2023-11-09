class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Pins must have a value from 0 to 10")
        if self.current_roll >= 20:
            if self.current_roll == 20 and (self.rolls[-1] == 10 or sum(self.rolls[-2:]) == 10):
                pass  # Allow bonus roll(s) in the tenth frame
            else:
                raise IndexError("Cannot roll after game is over")
        if self.current_roll > 0 and self.current_roll % 2 == 1 and self.rolls[self.current_roll - 1] + pins > 10 and self.rolls[self.current_roll - 1] != 10:
            raise ValueError("Pin count exceeds pins on the lane")
        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        if self.current_roll < 12:
            raise IndexError("Score cannot be taken until the end of the game")
        score = 0
        roll_index = 0
        for frame in range(10):
            if self.rolls[roll_index] == 10:  # Strike
                score += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1
            elif sum(self.rolls[roll_index:roll_index + 2]) == 10:  # Spare
                score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            else:  # Open frame
                score += sum(self.rolls[roll_index:roll_index + 2])
                roll_index += 2
        return score
